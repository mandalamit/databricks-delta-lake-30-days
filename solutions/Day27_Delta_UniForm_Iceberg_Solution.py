# Databricks notebook source
# MAGIC %md
# MAGIC # Day27 Solution: Delta UniForm (Iceberg Interoperability)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Allowing external Iceberg engines (Snowflake, Trino, BigQuery) to read your Delta table without copying data.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_uniform (
# MAGIC   order_id BIGINT,
# MAGIC   region STRING,
# MAGIC   total_amount DOUBLE
# MAGIC ) USING DELTA
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg'
# MAGIC );
# MAGIC 
# MAGIC INSERT INTO orders_uniform SELECT order_id, region, total_amount FROM orders_base LIMIT 100;
# MAGIC DESCRIBE EXTENDED orders_uniform;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

display(spark.sql("SHOW TBLPROPERTIES retail_lakehouse.orders_uniform"))
