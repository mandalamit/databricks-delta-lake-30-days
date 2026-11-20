# Databricks notebook source
# MAGIC %md
# MAGIC # Day07 Solution: Disaster Recovery (RESTORE)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Rolling back an accidental DELETE without a WHERE clause in production.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_restore_demo AS SELECT * FROM orders_base WHERE order_id <= 500;
# MAGIC DELETE FROM orders_restore_demo;
# MAGIC SELECT COUNT(*) AS count_after_accident FROM orders_restore_demo;
# MAGIC 
# MAGIC RESTORE TABLE orders_restore_demo TO VERSION AS OF 0;
# MAGIC SELECT COUNT(*) AS count_after_restore FROM orders_restore_demo;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "retail_lakehouse.orders_restore_demo")
dt.delete("order_id <= 250")
print("Count after accidental PySpark delete:", spark.table("retail_lakehouse.orders_restore_demo").count())

dt.restoreToVersion(0)
print("Count after PySpark restore:", spark.table("retail_lakehouse.orders_restore_demo").count())
