# Databricks notebook source
# MAGIC %md
# MAGIC # Day02: Convert to Delta & COPY INTO
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Migrating legacy Parquet archives in-place and loading daily CSV drops idempotently.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Copy `/Volumes/<catalog>/retail_lakehouse/raw_data/legacy_parquet/orders` to a working folder inside your Volume and convert it in-place using `DeltaTable.convertToDelta()`.
# MAGIC - Create an empty Delta table `orders_csv_bronze` and load `/Volumes/<catalog>/retail_lakehouse/raw_data/incoming_csv/orders_batch1` using `COPY INTO`.
# MAGIC - Re-run `COPY INTO` to verify idempotency (0 new rows loaded).
# MAGIC
# MAGIC > **Prerequisite:** Make sure you have run `Day00_Setup.py` once before running this notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA retail_lakehouse;
# MAGIC
# MAGIC -- TODO: Write your SQL solution below (replace 'workspace' if using a different catalog)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

# TODO: Write your PySpark solution below
