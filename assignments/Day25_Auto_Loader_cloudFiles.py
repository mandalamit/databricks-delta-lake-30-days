# Databricks notebook source
# MAGIC %md
# MAGIC # Day25: Auto Loader (cloudFiles)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Incrementally ingesting arriving CSV/JSON files from cloud storage with schema inference and rescue.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Use PySpark Auto Loader (`format("cloudFiles")`) to ingest `/Volumes/<catalog>/retail_lakehouse/raw_data/incoming_csv/orders_batch1`.
# MAGIC - Configure `cloudFiles.schemaLocation` and `checkpointLocation` inside your Unity Catalog Volume, with `schemaEvolutionMode = "rescue"`.
# MAGIC - Query the resulting Delta table and inspect `_rescued_data`.
# MAGIC
# MAGIC > **Prerequisite:** Make sure you have run `Day00_Setup.py` once before running this notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA retail_lakehouse;
# MAGIC
# MAGIC -- TODO: Write your SQL solution below

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

# TODO: Write your PySpark solution below
