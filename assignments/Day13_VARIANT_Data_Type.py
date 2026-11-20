# Databricks notebook source
# MAGIC %md
# MAGIC # Day13: VARIANT Data Type (Semi-Structured JSON)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Ingesting rapidly changing clickstream JSON payloads without slow string parsing or rigid schemas.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `clickstream_variant` with a `VARIANT` column (requires DBR 15.3+).
# MAGIC - Insert raw JSON using `parse_json()` and query nested fields with `:` notation.
# MAGIC - In PySpark, parse JSON strings from `/tmp/retail_lakehouse/raw_data/clickstream_json` using `F.parse_json()`.
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
