# Databricks notebook source
# MAGIC %md
# MAGIC # Day21: Shallow & Deep Clones
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Provisioning instant zero-copy QA/staging datasets from production tables.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_shallow_qa` using `CREATE OR REPLACE TABLE ... SHALLOW CLONE`.
# MAGIC - Create `orders_deep_backup` using `DEEP CLONE`.
# MAGIC - Modify `orders_shallow_qa` and verify `orders_base` is completely unaffected.
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
