# Databricks notebook source
# MAGIC %md
# MAGIC # Day17: Liquid Clustering
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Replacing rigid Hive partitioning with adaptive Liquid Clustering for evolving query patterns.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_liquid` with `CLUSTER BY (region, order_date)`.
# MAGIC - Run `OPTIMIZE orders_liquid`.
# MAGIC - Evolve the clustering keys without rewriting existing data using `ALTER TABLE orders_liquid CLUSTER BY (customer_id)`.
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
