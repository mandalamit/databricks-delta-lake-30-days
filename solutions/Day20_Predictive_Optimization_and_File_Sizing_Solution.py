# Databricks notebook source
# MAGIC %md
# MAGIC # Day20 Solution: Predictive Optimization & Target File Sizing
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Configuring target file sizes and understanding automated Unity Catalog Predictive Optimization.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_tuned
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.targetFileSize' = '67108864', -- 64 MB
# MAGIC   'delta.autoOptimize.optimizeWrite' = 'true',
# MAGIC   'delta.autoOptimize.autoCompact' = 'true'
# MAGIC )
# MAGIC AS SELECT * FROM orders_base;
# MAGIC 
# MAGIC -- Unity Catalog workspaces only:
# MAGIC -- ALTER SCHEMA retail_lakehouse ENABLE PREDICTIVE OPTIMIZATION;
# MAGIC 
# MAGIC SHOW TBLPROPERTIES orders_tuned;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

# In Unity Catalog, you can monitor Predictive Optimization via system tables:
# display(spark.table("system.storage.predictive_optimization_operations_history").limit(10))
display(spark.sql("SHOW TBLPROPERTIES retail_lakehouse.orders_tuned"))
