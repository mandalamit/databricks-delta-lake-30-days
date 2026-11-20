# Databricks notebook source
# MAGIC %md
# MAGIC # Day14: Table Properties & Protocol Features
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Inspecting Delta protocol versions and downgrading a table feature for legacy external readers.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Set custom `TBLPROPERTIES` on `orders_props_demo` and enable a table feature (e.g., `delta.enableDeletionVectors = true`).
# MAGIC - Inspect `minReaderVersion`, `minWriterVersion`, `readerFeatures`, and `writerFeatures` via `DESCRIBE DETAIL`.
# MAGIC - Practice removing a feature with `ALTER TABLE ... DROP FEATURE`.
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
