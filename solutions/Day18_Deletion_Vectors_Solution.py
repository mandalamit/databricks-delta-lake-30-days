# Databricks notebook source
# MAGIC %md
# MAGIC # Day18 Solution: Deletion Vectors (Merge-on-Read)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Accelerating frequent row-level UPDATE/DELETE operations on large tables without rewriting Parquet files.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_dv
# MAGIC TBLPROPERTIES ('delta.enableDeletionVectors' = 'true')
# MAGIC AS SELECT * FROM orders_base;
# MAGIC 
# MAGIC DELETE FROM orders_dv WHERE order_id <= 10;
# MAGIC 
# MAGIC SELECT version, operation, operationMetrics
# MAGIC FROM (DESCRIBE HISTORY orders_dv)
# MAGIC LIMIT 3;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "retail_lakehouse.orders_dv")
dt.update(condition="order_id = 20", set={"status": "'REFUNDED'"})
display(dt.history(2).select("version", "operation", "operationMetrics"))
