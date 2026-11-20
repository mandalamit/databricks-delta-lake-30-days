# Databricks notebook source
# MAGIC %md
# MAGIC # Day15 Solution: Small File Compaction (OPTIMIZE)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Fixing query slowness caused by thousands of tiny streaming/micro-batch files.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_fragmented AS SELECT * FROM orders_base LIMIT 10;
# MAGIC DESCRIBE DETAIL orders_fragmented;
# MAGIC 
# MAGIC -- After running the PySpark cell below to create 20 small files, run:
# MAGIC OPTIMIZE orders_fragmented;
# MAGIC DESCRIBE DETAIL orders_fragmented;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable

sample = spark.table("retail_lakehouse.orders_base").limit(10)
for _ in range(15):
    sample.repartition(1).write.format("delta").mode("append").saveAsTable("retail_lakehouse.orders_fragmented")

print("Files BEFORE optimize:", spark.sql("DESCRIBE DETAIL retail_lakehouse.orders_fragmented").collect()[0]["numFiles"])

DeltaTable.forName(spark, "retail_lakehouse.orders_fragmented").optimize().executeCompaction()
print("Files AFTER optimize:", spark.sql("DESCRIBE DETAIL retail_lakehouse.orders_fragmented").collect()[0]["numFiles"])
