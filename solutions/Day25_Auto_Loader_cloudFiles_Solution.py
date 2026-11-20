# Databricks notebook source
# MAGIC %md
# MAGIC # Day25 Solution: Auto Loader (cloudFiles)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Incrementally ingesting arriving CSV/JSON files from cloud storage with schema inference and rescue.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC -- Run the PySpark Auto Loader cell first, then verify:
# MAGIC SELECT COUNT(*) AS loaded_rows FROM orders_autoloader_bronze;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

schema_loc = "/tmp/retail_lakehouse/schemas/day25_autoloader"
ckpt_loc = "/tmp/retail_lakehouse/checkpoints/day25_autoloader"
dbutils.fs.rm(schema_loc, recurse=True)
dbutils.fs.rm(ckpt_loc, recurse=True)

query = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("header", "true")
    .option("cloudFiles.schemaLocation", schema_loc)
    .option("cloudFiles.schemaEvolutionMode", "rescue")
    .load("/tmp/retail_lakehouse/raw_data/incoming_csv/orders_batch1")
    .writeStream
    .format("delta")
    .option("checkpointLocation", ckpt_loc)
    .trigger(availableNow=True)
    .toTable("retail_lakehouse.orders_autoloader_bronze")
)
query.awaitTermination()
display(spark.table("retail_lakehouse.orders_autoloader_bronze").limit(5))
