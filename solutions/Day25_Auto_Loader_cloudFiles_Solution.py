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
# MAGIC USE SCHEMA retail_lakehouse;
# MAGIC -- Run the PySpark Auto Loader cell first, then verify:
# MAGIC SELECT COUNT(*) AS loaded_rows FROM orders_autoloader_bronze;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

catalog = spark.sql("SELECT current_catalog()").collect()[0][0]
base_path = f"/Volumes/{catalog}/retail_lakehouse/raw_data"

schema_loc = f"{base_path}/schemas/day25_autoloader"
ckpt_loc = f"{base_path}/checkpoints/day25_autoloader"
dbutils.fs.rm(schema_loc, recurse=True)
dbutils.fs.rm(ckpt_loc, recurse=True)

query = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("header", "true")
    .option("cloudFiles.schemaLocation", schema_loc)
    .option("cloudFiles.schemaEvolutionMode", "rescue")
    .load(f"{base_path}/incoming_csv/orders_batch1")
    .writeStream
    .format("delta")
    .option("checkpointLocation", ckpt_loc)
    .trigger(availableNow=True)
    .toTable(f"{catalog}.retail_lakehouse.orders_autoloader_bronze")
)
query.awaitTermination()
display(spark.table(f"{catalog}.retail_lakehouse.orders_autoloader_bronze").limit(5))
