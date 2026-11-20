# Databricks notebook source
# MAGIC %md
# MAGIC # Day09: Column Mapping (Rename & Drop Columns)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Renaming poorly named legacy columns (`cust_nm` -> `customer_name`) without rewriting terabytes of Parquet files.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `legacy_customers` with column `cust_nm` and `unused_flag`.
# MAGIC - Enable `delta.columnMapping.mode = 'name'`.
# MAGIC - Rename `cust_nm` to `customer_name` and drop `unused_flag` using `ALTER TABLE`.
# MAGIC
# MAGIC > **Prerequisite:** Make sure you have run `Day00_Setup.py` once before running this notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC
# MAGIC -- TODO: Write your SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

# TODO: Write your PySpark solution below
