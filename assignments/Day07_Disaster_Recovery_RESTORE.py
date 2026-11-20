# Databricks notebook source
# MAGIC %md
# MAGIC # Day07: Disaster Recovery (RESTORE)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Rolling back an accidental DELETE without a WHERE clause in production.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_restore_demo`, then accidentally delete all rows (`DELETE FROM orders_restore_demo`).
# MAGIC - Verify the table has 0 rows.
# MAGIC - Roll back the table using SQL `RESTORE TABLE ... TO VERSION AS OF 0`.
# MAGIC - Repeat a bad update and roll back programmatically using PySpark `DeltaTable.restoreToVersion()`.
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
