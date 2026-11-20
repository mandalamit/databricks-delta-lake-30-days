# Databricks notebook source
# MAGIC %md
# MAGIC # Day04: MERGE INTO (Upserts & Deduplication)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Syncing daily incremental order updates, new inserts, and cancellations from an OLTP database.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_silver` and a staging table `orders_cdc_stage` containing updated and new orders.
# MAGIC - Write a SQL `MERGE INTO` handling `WHEN MATCHED` (update) and `WHEN NOT MATCHED` (insert).
# MAGIC - Replicate the exact upsert in PySpark using `DeltaTable.forName(...).merge(...)`.
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
