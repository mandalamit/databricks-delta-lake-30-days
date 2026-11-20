# Databricks notebook source
# MAGIC %md
# MAGIC # Day01: Managed vs. External Tables & _delta_log
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Provisioning raw order tables and auditing underlying Delta transaction log metadata.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create a managed Delta table `retail_lakehouse.orders_bronze` from `retail_lakehouse.orders_base`.
# MAGIC - Inspect its metadata using `DESCRIBE DETAIL` and `DESCRIBE EXTENDED`.
# MAGIC - Using PySpark, create an external Delta table at `/tmp/retail_lakehouse/ext_orders_bronze`.
# MAGIC - List and read the JSON commit log inside `_delta_log/` using `dbutils.fs.ls()`.
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
