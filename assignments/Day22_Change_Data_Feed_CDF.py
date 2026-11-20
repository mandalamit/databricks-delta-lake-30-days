# Databricks notebook source
# MAGIC %md
# MAGIC # Day22: Change Data Feed (CDF)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Propagating only changed rows from Bronze to Silver instead of full-table scans.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_cdf` with `delta.enableChangeDataFeed = true`.
# MAGIC - Run an `INSERT`, `UPDATE`, and `DELETE`.
# MAGIC - Query `table_changes('orders_cdf', 1)` in SQL and read CDF incrementally in PySpark.
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
