# Databricks notebook source
# MAGIC %md
# MAGIC # Day20: Predictive Optimization & Target File Sizing
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Configuring target file sizes and understanding automated Unity Catalog Predictive Optimization.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Configure `delta.targetFileSize` on `orders_tuned`.
# MAGIC - Review the SQL syntax for `ALTER SCHEMA ... ENABLE PREDICTIVE OPTIMIZATION` (Unity Catalog).
# MAGIC - Inspect table properties in PySpark.
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
