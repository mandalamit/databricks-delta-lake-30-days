# Databricks notebook source
# MAGIC %md
# MAGIC # Day01 Solution: Managed vs. External Tables & _delta_log
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Provisioning raw order tables and auditing underlying Delta transaction log metadata.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
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

ext_path = "/tmp/retail_lakehouse/ext_orders_bronze"
df = spark.table("retail_lakehouse.orders_base")

df.write.format("delta").mode("overwrite").option("path", ext_path).saveAsTable("retail_lakehouse.ext_orders_bronze")

# Inspect _delta_log directory
display(dbutils.fs.ls(f"{ext_path}/_delta_log"))

# Read the first JSON commit file
log_df = spark.read.json(f"{ext_path}/_delta_log/00000000000000000000.json")
display(log_df)
