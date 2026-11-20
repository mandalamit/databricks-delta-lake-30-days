# Databricks notebook source
# MAGIC %md
# MAGIC # Day21 Solution: Shallow & Deep Clones
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Provisioning instant zero-copy QA/staging datasets from production tables.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_shallow_qa SHALLOW CLONE orders_base;
# MAGIC CREATE OR REPLACE TABLE orders_deep_backup DEEP CLONE orders_base;
# MAGIC 
# MAGIC DELETE FROM orders_shallow_qa WHERE region = 'APAC';
# MAGIC 
# MAGIC SELECT 'base' AS tbl, COUNT(*) AS cnt FROM orders_base
# MAGIC UNION ALL
# MAGIC SELECT 'shallow_qa' AS tbl, COUNT(*) AS cnt FROM orders_shallow_qa;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable

base_dt = DeltaTable.forName(spark, "retail_lakehouse.orders_base")
base_dt.clone(target="retail_lakehouse.orders_shallow_pyspark", isShallow=True, replace=True)
print("Shallow clone count:", spark.table("retail_lakehouse.orders_shallow_pyspark").count())
