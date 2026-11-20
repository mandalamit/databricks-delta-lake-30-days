# Databricks notebook source
# MAGIC %md
# MAGIC # Day05: SCD Type 2 Pattern
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Tracking historical customer city and tier changes for compliance and analytics.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `dim_customers_scd2` with `effective_start`, `effective_end`, and `is_current` columns.
# MAGIC - Simulate incoming changes for `customer_id` 1 and 2.
# MAGIC - Implement SCD Type 2 in SQL and PySpark: expire the old active record and insert the new active version.
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
