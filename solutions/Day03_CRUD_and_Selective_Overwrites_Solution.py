# Databricks notebook source
# MAGIC %md
# MAGIC # Day03 Solution: CRUD & Selective Overwrites (replaceWhere)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Correcting regional tax calculations and status updates without rewriting the entire table.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_day03 AS SELECT * FROM orders_base;
# MAGIC 
# MAGIC -- INSERT
# MAGIC INSERT INTO orders_day03 VALUES (99999, 1, 'APAC', 'COMPLETED', 250.00, current_timestamp(), current_date());
# MAGIC 
# MAGIC -- UPDATE
# MAGIC UPDATE orders_day03 SET status = 'COMPLETED' WHERE order_id = 99999;
# MAGIC 
# MAGIC -- DELETE
# MAGIC DELETE FROM orders_day03 WHERE status = 'CANCELLED';
# MAGIC 
# MAGIC SELECT status, COUNT(*) FROM orders_day03 GROUP BY status;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from pyspark.sql import functions as F

apac_adjusted = (
    spark.table("retail_lakehouse.orders_day03")
    .filter("region = 'APAC'")
    .withColumn("total_amount", F.round(F.col("total_amount") * 1.05, 2))
)

(
    apac_adjusted.write
    .format("delta")
    .mode("overwrite")
    .option("replaceWhere", "region = 'APAC'")
    .saveAsTable("retail_lakehouse.orders_day03")
)

display(spark.table("retail_lakehouse.orders_day03").groupBy("region").count())
