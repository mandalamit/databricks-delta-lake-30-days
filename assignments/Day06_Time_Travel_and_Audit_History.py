# Databricks notebook source
# MAGIC %md
# MAGIC # Day06: Time Travel & Audit History
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Reproducing last month's financial report for an audit by querying historical table versions.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Perform two updates on `retail_lakehouse.orders_timetravel`.
# MAGIC - Run `DESCRIBE HISTORY` to view version numbers and timestamps.
# MAGIC - Query Version 0 vs. latest version in SQL using `VERSION AS OF`.
# MAGIC - In PySpark, load Version 0 and Version 1 using `.option("versionAsOf", ...)` and find the exact diff using `.exceptAll()`.
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
