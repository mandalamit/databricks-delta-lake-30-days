# Databricks notebook source
# MAGIC %md
# MAGIC # Day29: Auto TTL & GDPR Compliance
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Fulfilling Right-to-be-Forgotten (GDPR) requests by deleting user PII and purging stale files.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `customers_gdpr` from `dim_customers`.
# MAGIC - Delete PII for `customer_id = 42` across the table, log the deletion in an audit table, and run `VACUUM`.
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
