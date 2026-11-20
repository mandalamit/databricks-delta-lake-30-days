# Databricks notebook source
# MAGIC %md
# MAGIC # Day22 Solution: Change Data Feed (CDF)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Propagating only changed rows from Bronze to Silver instead of full-table scans.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_cdf
# MAGIC TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true')
# MAGIC AS SELECT * FROM orders_base LIMIT 50;
# MAGIC 
# MAGIC UPDATE orders_cdf SET status = 'SHIPPED' WHERE order_id = 1;
# MAGIC DELETE FROM orders_cdf WHERE order_id = 2;
# MAGIC 
# MAGIC SELECT order_id, status, _change_type, _commit_version
# MAGIC FROM table_changes('orders_cdf', 1);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

cdf_df = (
    spark.read.format("delta")
    .option("readChangeFeed", "true")
    .option("startingVersion", 1)
    .table("retail_lakehouse.orders_cdf")
)
display(cdf_df.select("order_id", "status", "_change_type", "_commit_version"))
