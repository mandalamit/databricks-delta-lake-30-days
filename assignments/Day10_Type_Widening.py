# Databricks notebook source
# MAGIC %md
# MAGIC # Day10: Type Widening
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Upgrading `order_id` from `INT` to `BIGINT` with zero downtime and no data rewrite.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_widening` with `order_id INT` and enable `delta.enableTypeWidening = true`.
# MAGIC - Alter `order_id` from `INT` to `BIGINT` in SQL.
# MAGIC - Append a PySpark DataFrame containing a `LongType` value exceeding 32-bit integer limits.
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
