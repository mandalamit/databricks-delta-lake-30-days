# Databricks notebook source
# MAGIC %md
# MAGIC # Day08 Solution: Schema Enforcement & Evolution
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Handling upstream API payloads that suddenly add a `discount_code` column.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_schema_demo AS SELECT order_id, customer_id, total_amount FROM orders_base LIMIT 10;
# MAGIC 
# MAGIC CREATE OR REPLACE TEMP VIEW incoming_with_coupon AS
# MAGIC SELECT 9001 AS order_id, 10 AS customer_id, 120.00 AS total_amount, 'SAVE20' AS coupon_code;
# MAGIC 
# MAGIC MERGE WITH SCHEMA EVOLUTION INTO orders_schema_demo t
# MAGIC USING incoming_with_coupon s
# MAGIC ON t.order_id = s.order_id
# MAGIC WHEN MATCHED THEN UPDATE SET *
# MAGIC WHEN NOT MATCHED THEN INSERT *;
# MAGIC 
# MAGIC SELECT * FROM orders_schema_demo WHERE order_id = 9001;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from pyspark.sql import functions as F

extra_col_df = (
    spark.table("retail_lakehouse.orders_base")
    .select("order_id", "customer_id", "total_amount")
    .limit(5)
    .withColumn("discount_code", F.lit("WELCOME10"))
)

# 1. Observe Schema Enforcement
try:
    extra_col_df.write.format("delta").mode("append").saveAsTable("retail_lakehouse.orders_schema_demo")
except Exception as e:
    print("Schema Enforcement blocked write as expected:", str(e)[:120])

# 2. Enable Schema Evolution
extra_col_df.write.format("delta").mode("append").option("mergeSchema", "true").saveAsTable("retail_lakehouse.orders_schema_demo")
display(spark.table("retail_lakehouse.orders_schema_demo").filter("discount_code IS NOT NULL"))
