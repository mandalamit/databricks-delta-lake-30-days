# Databricks notebook source
# MAGIC %md
# MAGIC # Day27: Delta UniForm (Iceberg Interoperability)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Allowing external Iceberg engines (Snowflake, Trino, BigQuery) to read your Delta table without copying data.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_uniform` with Column Mapping enabled and `delta.universalFormat.enabledFormats = 'iceberg'`.
# MAGIC - Insert data and inspect `DESCRIBE EXTENDED orders_uniform` for Iceberg metadata.
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
