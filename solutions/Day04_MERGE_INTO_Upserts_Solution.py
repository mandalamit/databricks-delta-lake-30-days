# Databricks notebook source
# MAGIC %md
# MAGIC # Day04 Solution: MERGE INTO (Upserts & Deduplication)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Syncing daily incremental order updates, new inserts, and cancellations from an OLTP database.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_silver AS SELECT * FROM orders_base WHERE order_id <= 1000;
# MAGIC 
# MAGIC CREATE OR REPLACE TEMP VIEW orders_cdc_stage AS
# MAGIC SELECT 1 AS order_id, 2 AS customer_id, 'APAC' AS region, 'SHIPPED' AS status, 999.99 AS total_amount, current_timestamp() AS order_ts, current_date() AS order_date
# MAGIC UNION ALL
# MAGIC SELECT 1001, 5, 'EMEA', 'PENDING', 150.00, current_timestamp(), current_date();
# MAGIC 
# MAGIC MERGE INTO orders_silver AS t
# MAGIC USING orders_cdc_stage AS s
# MAGIC ON t.order_id = s.order_id
# MAGIC WHEN MATCHED THEN UPDATE SET *
# MAGIC WHEN NOT MATCHED THEN INSERT *;
# MAGIC 
# MAGIC SELECT * FROM orders_silver WHERE order_id IN (1, 1001);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable
from pyspark.sql import functions as F

target = DeltaTable.forName(spark, "retail_lakehouse.orders_silver")
updates_df = spark.sql("""
    SELECT 2 AS order_id, 3 AS customer_id, 'NA' AS region, 'COMPLETED' AS status, 888.88 AS total_amount, current_timestamp() AS order_ts, current_date() AS order_date
    UNION ALL
    SELECT 1002, 10, 'LATAM', 'PENDING', 320.50, current_timestamp(), current_date()
""")

(
    target.alias("t")
    .merge(updates_df.alias("s"), "t.order_id = s.order_id")
    .whenMatchedUpdateAll()
    .whenNotMatchedInsertAll()
    .execute()
)

display(spark.table("retail_lakehouse.orders_silver").filter("order_id IN (2, 1002)"))
