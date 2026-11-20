# Databricks notebook source
# MAGIC %md
# MAGIC # Day30: Capstone: Production Medallion Pipeline
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Delivering an end-to-end Bronze -> Silver -> Gold e-commerce lakehouse combining Delta Lake best practices.
# MAGIC
# MAGIC ### Tasks
# MAGIC - **Bronze:** Ingest raw orders with CDF enabled (`capstone_orders_bronze`).
# MAGIC - **Silver:** Clean, deduplicate, and enforce `CHECK (total_amount >= 0)` (`capstone_orders_silver`) with Liquid Clustering.
# MAGIC - **Gold:** Build `capstone_gold_regional_kpi` aggregating revenue and order counts by `region` and `order_date`.
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
