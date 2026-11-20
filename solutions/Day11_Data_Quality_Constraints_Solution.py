# Databricks notebook source
# MAGIC %md
# MAGIC # Day11 Solution: Data Quality Constraints (NOT NULL & CHECK)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Blocking negative order totals from entering curated Silver tables and routing bad rows to quarantine.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_constrained (
# MAGIC   order_id INT NOT NULL,
# MAGIC   total_amount DOUBLE
# MAGIC ) USING DELTA;
# MAGIC 
# MAGIC ALTER TABLE orders_constrained ADD CONSTRAINT valid_amount CHECK (total_amount >= 0);
# MAGIC 
# MAGIC INSERT INTO orders_constrained VALUES (1, 100.0);
# MAGIC SELECT * FROM orders_constrained;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

bad_batch = spark.createDataFrame([(2, -50.0), (3, 75.0)], ["order_id", "total_amount"])

try:
    bad_batch.write.format("delta").mode("append").saveAsTable("retail_lakehouse.orders_constrained")
except Exception as e:
    print("Constraint violation caught! Routing bad rows to quarantine...")
    bad_batch.filter("total_amount < 0").write.format("delta").mode("overwrite").saveAsTable("retail_lakehouse.orders_quarantine")
    bad_batch.filter("total_amount >= 0").write.format("delta").mode("append").saveAsTable("retail_lakehouse.orders_constrained")

display(spark.table("retail_lakehouse.orders_quarantine"))
