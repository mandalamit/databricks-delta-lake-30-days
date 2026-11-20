# Databricks notebook source
# MAGIC %md
# MAGIC # Day26 Solution: Concurrency & Isolation Levels
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Configuring isolation levels and preventing ConcurrentAppendException on overlapping writes.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_concurrency
# MAGIC TBLPROPERTIES ('delta.isolationLevel' = 'WriteSerializable')
# MAGIC AS SELECT * FROM orders_base;
# MAGIC 
# MAGIC SHOW TBLPROPERTIES orders_concurrency;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

# Disjoint writes using replaceWhere avoid conflicts
for r in ["APAC", "EMEA"]:
    df_r = spark.table("retail_lakehouse.orders_base").filter(f"region = '{r}'")
    (
        df_r.write.format("delta")
        .mode("overwrite")
        .option("replaceWhere", f"region = '{r}'")
        .saveAsTable("retail_lakehouse.orders_concurrency")
    )
print("Disjoint region writes succeeded cleanly.")
