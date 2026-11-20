# Databricks notebook source
# MAGIC %md
# MAGIC # Day23: Row Tracking
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Tracking stable row lineage across OPTIMIZE, MERGE, and clustering operations.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_row_tracking` with `delta.enableRowTracking = true`.
# MAGIC - Query hidden metadata columns `_metadata.row_id` and `_metadata.row_commit_version`.
# MAGIC - Update a row and verify `_metadata.row_id` stays constant while `_metadata.row_commit_version` increments.
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
