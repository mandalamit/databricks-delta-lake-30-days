# Databricks notebook source
# MAGIC %md
# MAGIC # Day19: VACUUM & Storage Cleanup
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Controlling cloud storage costs by purging stale unreferenced Parquet files.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Perform several overwrites on `orders_vacuum_demo`.
# MAGIC - Run `VACUUM orders_vacuum_demo RETAIN 168 HOURS DRY RUN` to preview files slated for deletion.
# MAGIC - Run `DeltaTable.vacuum(168)` in PySpark.
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
