# Databricks notebook source
# MAGIC %md
# MAGIC # Day23 Solution: Row Tracking
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Tracking stable row lineage across OPTIMIZE, MERGE, and clustering operations.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_row_tracking
# MAGIC TBLPROPERTIES ('delta.enableRowTracking' = 'true')
# MAGIC AS SELECT * FROM orders_base LIMIT 20;
# MAGIC 
# MAGIC UPDATE orders_row_tracking SET total_amount = total_amount + 10 WHERE order_id = 1;
# MAGIC 
# MAGIC SELECT order_id, total_amount, _metadata.row_id, _metadata.row_commit_version
# MAGIC FROM orders_row_tracking
# MAGIC WHERE order_id IN (1, 2);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from pyspark.sql import functions as F

df = (
    spark.table("retail_lakehouse.orders_row_tracking")
    .select("order_id", "total_amount", F.col("_metadata.row_id").alias("row_id"), F.col("_metadata.row_commit_version").alias("commit_ver"))
    .filter("order_id IN (1, 2)")
)
display(df)
