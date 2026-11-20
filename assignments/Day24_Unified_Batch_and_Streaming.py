# Databricks notebook source
# MAGIC %md
# MAGIC # Day24: Unified Batch & Streaming
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Processing live order events incrementally from a Delta table with exactly-once guarantees.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Stream from `retail_lakehouse.orders_base` into `retail_lakehouse.orders_stream_sink` using `spark.readStream.table()`.
# MAGIC - Use `.trigger(availableNow=True)` and a dedicated `checkpointLocation`.
# MAGIC - Verify the sink table row count in SQL.
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
