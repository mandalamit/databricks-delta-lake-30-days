# Databricks notebook source
# MAGIC %md
# MAGIC # Day26: Concurrency & Isolation Levels
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Configuring isolation levels and preventing ConcurrentAppendException on overlapping writes.
# MAGIC
# MAGIC ### Tasks
# MAGIC - Create `orders_concurrency` and inspect/set `delta.isolationLevel` (`WriteSerializable` vs `Serializable`).
# MAGIC - Demonstrate safe concurrent-style disjoint writes using `replaceWhere` on separate regions (`APAC` vs `EMEA`).
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
