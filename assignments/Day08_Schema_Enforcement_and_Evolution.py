# Databricks notebook source
# MAGIC %md
# MAGIC # Day08: Schema Enforcement & Evolution
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Handling upstream API payloads that suddenly add a `discount_code` column.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_schema_demo` and attempt to append a DataFrame with an extra `discount_code` column (observe the schema mismatch error).
# MAGIC - Re-run the append with `.option("mergeSchema", "true")` to evolve the schema safely.
# MAGIC - Test `MERGE WITH SCHEMA EVOLUTION` in SQL.
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
