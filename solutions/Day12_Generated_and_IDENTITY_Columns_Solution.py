# Databricks notebook source
# MAGIC %md
# MAGIC # Day12 Solution: Generated & IDENTITY Columns
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Auto-generating surrogate keys and deriving `order_date` from `order_ts` automatically on write.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_identity (
# MAGIC   surrogate_id BIGINT GENERATED ALWAYS AS IDENTITY,
# MAGIC   order_ts TIMESTAMP,
# MAGIC   order_date DATE GENERATED ALWAYS AS (CAST(order_ts AS DATE)),
# MAGIC   amount DOUBLE
# MAGIC ) USING DELTA;
# MAGIC 
# MAGIC INSERT INTO orders_identity (order_ts, amount) VALUES (TIMESTAMP '2026-05-01 10:15:00', 250.0);
# MAGIC SELECT * FROM orders_identity;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from pyspark.sql import functions as F

new_orders = spark.createDataFrame([(150.5,), (320.0,)], ["amount"]).withColumn("order_ts", F.current_timestamp())
new_orders.write.format("delta").mode("append").saveAsTable("retail_lakehouse.orders_identity")
display(spark.table("retail_lakehouse.orders_identity"))
