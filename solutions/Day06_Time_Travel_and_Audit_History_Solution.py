# Databricks notebook source
# MAGIC %md
# MAGIC # Day06 Solution: Time Travel & Audit History
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Reproducing last month's financial report for an audit by querying historical table versions.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_timetravel AS SELECT * FROM orders_base WHERE order_id <= 100;
# MAGIC UPDATE orders_timetravel SET total_amount = total_amount + 100 WHERE order_id <= 5;
# MAGIC DELETE FROM orders_timetravel WHERE order_id = 100;
# MAGIC 
# MAGIC DESCRIBE HISTORY orders_timetravel;
# MAGIC 
# MAGIC SELECT 'v0' AS ver, COUNT(*) AS cnt, SUM(total_amount) AS total FROM orders_timetravel VERSION AS OF 0
# MAGIC UNION ALL
# MAGIC SELECT 'latest' AS ver, COUNT(*) AS cnt, SUM(total_amount) AS total FROM orders_timetravel;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

df_v0 = spark.read.format("delta").option("versionAsOf", 0).table("retail_lakehouse.orders_timetravel")
df_v1 = spark.read.format("delta").option("versionAsOf", 1).table("retail_lakehouse.orders_timetravel")

print("Rows changed between v0 and v1:")
display(df_v1.exceptAll(df_v0))
