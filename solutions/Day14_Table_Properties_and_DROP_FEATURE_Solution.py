# Databricks notebook source
# MAGIC %md
# MAGIC # Day14 Solution: Table Properties & Protocol Features
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Inspecting Delta protocol versions and downgrading a table feature for legacy external readers.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_props_demo
# MAGIC USING DELTA
# MAGIC TBLPROPERTIES ('owner' = 'data_eng_team', 'delta.enableDeletionVectors' = 'true')
# MAGIC AS SELECT * FROM orders_base LIMIT 100;
# MAGIC 
# MAGIC DESCRIBE DETAIL orders_props_demo;
# MAGIC 
# MAGIC -- Disable and drop feature (DBR 14.1+)
# MAGIC ALTER TABLE orders_props_demo SET TBLPROPERTIES ('delta.enableDeletionVectors' = 'false');
# MAGIC -- ALTER TABLE orders_props_demo DROP FEATURE 'deletionVectors' TRUNCATE HISTORY;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

detail_df = spark.sql("DESCRIBE DETAIL retail_lakehouse.orders_props_demo")
display(detail_df.select("name", "minReaderVersion", "minWriterVersion", "properties"))
