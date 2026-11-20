# Databricks notebook source
# MAGIC %md
# MAGIC # Day11: Data Quality Constraints (NOT NULL & CHECK)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Blocking negative order totals from entering curated Silver tables and routing bad rows to quarantine.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_constrained` with `order_id INT NOT NULL`.
# MAGIC - Add a `CHECK` constraint `valid_amount` enforcing `total_amount >= 0`.
# MAGIC - In PySpark, attempt to write a negative row, catch the exception, and write invalid rows to `orders_quarantine`.
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
