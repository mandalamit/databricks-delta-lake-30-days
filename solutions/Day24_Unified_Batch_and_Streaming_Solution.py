# Databricks notebook source
# MAGIC %md
# MAGIC # Day24 Solution: Unified Batch & Streaming
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Processing live order events incrementally from a Delta table with exactly-once guarantees.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA retail_lakehouse;
# MAGIC -- Run the PySpark streaming cell first, then verify:
# MAGIC SELECT COUNT(*) AS streamed_rows FROM orders_stream_sink;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

catalog = spark.sql("SELECT current_catalog()").collect()[0][0]
checkpoint_path = f"/Volumes/{catalog}/retail_lakehouse/raw_data/checkpoints/day24_orders_stream"
dbutils.fs.rm(checkpoint_path, recurse=True)

query = (
    spark.readStream.table(f"{catalog}.retail_lakehouse.orders_base")
    .writeStream
    .format("delta")
    .option("checkpointLocation", checkpoint_path)
    .trigger(availableNow=True)
    .toTable(f"{catalog}.retail_lakehouse.orders_stream_sink")
)
query.awaitTermination()
print("Stream completed. Row count:", spark.table(f"{catalog}.retail_lakehouse.orders_stream_sink").count())
