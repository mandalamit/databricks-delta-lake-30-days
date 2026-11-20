# Databricks notebook source
# MAGIC %md
# MAGIC # Day05 Solution: SCD Type 2 Pattern
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Tracking historical customer city and tier changes for compliance and analytics.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE dim_customers_scd2 AS
# MAGIC SELECT customer_id, customer_name, tier, city, email,
# MAGIC        DATE('2026-01-01') AS effective_start,
# MAGIC        DATE('9999-12-31') AS effective_end,
# MAGIC        TRUE AS is_current
# MAGIC FROM dim_customers;
# MAGIC 
# MAGIC CREATE OR REPLACE TEMP VIEW customer_updates AS
# MAGIC SELECT 1 AS customer_id, 'Customer_1' AS customer_name, 'Gold' AS tier, 'Hyderabad' AS city, 'user1@example.com' AS email;
# MAGIC 
# MAGIC -- Step 1: Expire changed records
# MAGIC MERGE INTO dim_customers_scd2 AS t
# MAGIC USING customer_updates AS s
# MAGIC ON t.customer_id = s.customer_id AND t.is_current = TRUE
# MAGIC WHEN MATCHED AND (t.city <> s.city OR t.tier <> s.tier) THEN
# MAGIC   UPDATE SET t.effective_end = current_date(), t.is_current = FALSE;
# MAGIC 
# MAGIC -- Step 2: Insert new active versions
# MAGIC INSERT INTO dim_customers_scd2
# MAGIC SELECT s.customer_id, s.customer_name, s.tier, s.city, s.email, current_date(), DATE('9999-12-31'), TRUE
# MAGIC FROM customer_updates s;
# MAGIC 
# MAGIC SELECT * FROM dim_customers_scd2 WHERE customer_id = 1 ORDER BY effective_start;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable
from pyspark.sql import functions as F

scd_table = DeltaTable.forName(spark, "retail_lakehouse.dim_customers_scd2")
updates = spark.createDataFrame(
    [(2, "Customer_2", "Gold", "Pune", "user2@example.com")],
    ["customer_id", "customer_name", "tier", "city", "email"]
)

# Expire old record
(
    scd_table.alias("t")
    .merge(updates.alias("s"), "t.customer_id = s.customer_id AND t.is_current = true")
    .whenMatchedUpdate(
        condition="t.city <> s.city OR t.tier <> s.tier",
        set={"effective_end": F.current_date(), "is_current": F.lit(False)}
    )
    .execute()
)

# Insert new active version
new_versions = (
    updates
    .withColumn("effective_start", F.current_date())
    .withColumn("effective_end", F.to_date(F.lit("9999-12-31")))
    .withColumn("is_current", F.lit(True))
)
new_versions.write.format("delta").mode("append").saveAsTable("retail_lakehouse.dim_customers_scd2")

display(spark.table("retail_lakehouse.dim_customers_scd2").filter("customer_id = 2"))
