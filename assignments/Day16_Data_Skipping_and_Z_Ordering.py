# Databricks notebook source
# MAGIC %md
# MAGIC # Day16: Data Skipping & Z-Ordering
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Speeding up point lookups on high-cardinality columns (`customer_id`) in partitioned tables.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create a partitioned table `orders_zorder` partitioned by `region`.
# MAGIC - Run `OPTIMIZE orders_zorder ZORDER BY (customer_id)`.
# MAGIC - Execute `DeltaTable.optimize().executeZOrderBy("customer_id")` in PySpark and inspect `DESCRIBE HISTORY` metrics.
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
