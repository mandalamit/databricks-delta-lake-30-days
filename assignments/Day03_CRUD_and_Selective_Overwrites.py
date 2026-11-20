# Databricks notebook source
# MAGIC %md
# MAGIC # Day03: CRUD & Selective Overwrites (replaceWhere)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Correcting regional tax calculations and status updates without rewriting the entire table.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Run `INSERT`, `UPDATE`, and `DELETE` on `retail_lakehouse.orders_day03`.
# MAGIC - In PySpark, selectively overwrite only `region = 'APAC'` using `.option("replaceWhere", "region = 'APAC'")` to apply a 5% tax adjustment.
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
