# Databricks notebook source
# MAGIC %md
# MAGIC # Day18: Deletion Vectors (Merge-on-Read)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Accelerating frequent row-level UPDATE/DELETE operations on large tables without rewriting Parquet files.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_dv` with `delta.enableDeletionVectors = true`.
# MAGIC - Run a targeted `DELETE` of 10 rows.
# MAGIC - Inspect `operationMetrics` in `DESCRIBE HISTORY` to verify `numDeletionVectorsAdded`.
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
