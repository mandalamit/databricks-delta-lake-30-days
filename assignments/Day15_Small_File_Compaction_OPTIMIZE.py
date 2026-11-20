# Databricks notebook source
# MAGIC %md
# MAGIC # Day15: Small File Compaction (OPTIMIZE)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Fixing query slowness caused by thousands of tiny streaming/micro-batch files.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_fragmented` and append 20 tiny batches to create many small files.
# MAGIC - Check `numFiles` in `DESCRIBE DETAIL`.
# MAGIC - Run `OPTIMIZE` in SQL and `DeltaTable.optimize().executeCompaction()` in PySpark, then compare `numFiles`.
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
