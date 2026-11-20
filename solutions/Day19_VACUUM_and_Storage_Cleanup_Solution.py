# Databricks notebook source
# MAGIC %md
# MAGIC # Day19 Solution: VACUUM & Storage Cleanup
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Controlling cloud storage costs by purging stale unreferenced Parquet files.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_vacuum_demo AS SELECT * FROM orders_base LIMIT 100;
# MAGIC INSERT OVERWRITE orders_vacuum_demo SELECT * FROM orders_base LIMIT 100;
# MAGIC 
# MAGIC -- Preview files to be deleted (safe default 168 hours = 7 days)
# MAGIC VACUUM orders_vacuum_demo RETAIN 168 HOURS DRY RUN;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "retail_lakehouse.orders_vacuum_demo")
dt.vacuum(168)
print("VACUUM completed with 168-hour retention.")
