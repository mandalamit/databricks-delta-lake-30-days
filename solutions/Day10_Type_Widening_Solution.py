# Databricks notebook source
# MAGIC %md
# MAGIC # Day10 Solution: Type Widening
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Upgrading `order_id` from `INT` to `BIGINT` with zero downtime and no data rewrite.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_widening (
# MAGIC   order_id INT,
# MAGIC   amount FLOAT
# MAGIC ) USING DELTA
# MAGIC TBLPROPERTIES ('delta.enableTypeWidening' = 'true');
# MAGIC 
# MAGIC INSERT INTO orders_widening VALUES (101, 49.99);
# MAGIC 
# MAGIC ALTER TABLE orders_widening ALTER COLUMN order_id TYPE BIGINT;
# MAGIC ALTER TABLE orders_widening ALTER COLUMN amount TYPE DOUBLE;
# MAGIC 
# MAGIC INSERT INTO orders_widening VALUES (3000000000, 199.999999);
# MAGIC SELECT * FROM orders_widening;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, LongType, DoubleType

schema = StructType([
    StructField("order_id", LongType(), True),
    StructField("amount", DoubleType(), True)
])
wide_df = spark.createDataFrame([(4000000000, 299.123456)], schema)
wide_df.write.format("delta").mode("append").saveAsTable("retail_lakehouse.orders_widening")
display(spark.table("retail_lakehouse.orders_widening"))
