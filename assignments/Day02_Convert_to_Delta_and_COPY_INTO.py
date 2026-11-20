# Databricks notebook source
# MAGIC %md
# MAGIC # Day02: Convert to Delta & COPY INTO
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Migrating legacy Parquet archives in-place and loading daily CSV drops idempotently.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Copy `/tmp/retail_lakehouse/raw_data/legacy_parquet/orders` to a working path and convert it in-place using `CONVERT TO DELTA`.
# MAGIC - Create an empty Delta table `orders_csv_bronze` and load `/tmp/retail_lakehouse/raw_data/incoming_csv/orders_batch1` using `COPY INTO`.
# MAGIC - Re-run `COPY INTO` to verify idempotency (0 new rows loaded).
# MAGIC - In PySpark, convert a Parquet folder using `DeltaTable.convertToDelta()`.
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
