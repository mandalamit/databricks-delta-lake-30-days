# Databricks notebook source
# MAGIC %md
# MAGIC # Day01 Solution: Managed Tables, Path-Based Delta & _delta_log
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Provisioning raw order tables and auditing underlying Delta transaction log metadata.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_bronze
# MAGIC USING DELTA
# MAGIC AS SELECT * FROM orders_base;
# MAGIC 
# MAGIC DESCRIBE DETAIL orders_bronze;
# MAGIC DESCRIBE EXTENDED orders_bronze;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

catalog = spark.sql("SELECT current_catalog()").collect()[0][0]
delta_path = f"/Volumes/{catalog}/retail_lakehouse/raw_data/delta_files_orders"

df = spark.table(f"{catalog}.retail_lakehouse.orders_base")

# Write path-based Delta files into the Volume (works on Databricks Free Edition)
df.write.format("delta").mode("overwrite").save(delta_path)

# Inspect _delta_log directory
display(dbutils.fs.ls(f"{delta_path}/_delta_log"))

# Read the first JSON commit file
log_df = spark.read.json(f"{delta_path}/_delta_log/00000000000000000000.json")
display(log_df)
