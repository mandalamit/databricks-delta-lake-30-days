# Databricks notebook source
# MAGIC %md
# MAGIC # Day09 Solution: Column Mapping (Rename & Drop Columns)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Renaming poorly named legacy columns (`cust_nm` -> `customer_name`) without rewriting terabytes of Parquet files.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE legacy_customers (
# MAGIC   cust_id INT, cust_nm STRING, unused_flag STRING
# MAGIC ) USING DELTA
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.minReaderVersion' = '2',
# MAGIC   'delta.minWriterVersion' = '5',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC );
# MAGIC 
# MAGIC INSERT INTO legacy_customers VALUES (1, 'Aarav', 'N'), (2, 'Meera', 'Y');
# MAGIC 
# MAGIC ALTER TABLE legacy_customers RENAME COLUMN cust_nm TO customer_name;
# MAGIC ALTER TABLE legacy_customers DROP COLUMN unused_flag;
# MAGIC 
# MAGIC SELECT * FROM legacy_customers;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

# Inspect table properties in PySpark
props = spark.sql("SHOW TBLPROPERTIES retail_lakehouse.legacy_customers")
display(props)
display(spark.table("retail_lakehouse.legacy_customers"))
