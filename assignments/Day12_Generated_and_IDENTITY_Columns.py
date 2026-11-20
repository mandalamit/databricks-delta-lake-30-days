# Databricks notebook source
# MAGIC %md
# MAGIC # Day12: Generated & IDENTITY Columns
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Auto-generating surrogate keys and deriving `order_date` from `order_ts` automatically on write.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_identity` using `GENERATED ALWAYS AS IDENTITY` for `surrogate_id` and `GENERATED ALWAYS AS (CAST(order_ts AS DATE))` for `order_date`.
# MAGIC - Insert rows via SQL and PySpark without specifying the generated/identity columns.
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
