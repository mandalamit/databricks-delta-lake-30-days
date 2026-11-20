# Databricks notebook source
# MAGIC %md
# MAGIC # Day02 Solution: Convert to Delta & COPY INTO
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Migrating legacy Parquet archives in-place and loading daily CSV drops idempotently.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE TABLE IF NOT EXISTS orders_csv_bronze (
# MAGIC   order_id STRING, customer_id STRING, region STRING,
# MAGIC   status STRING, total_amount STRING, order_ts STRING, order_date STRING
# MAGIC ) USING DELTA;
# MAGIC 
# MAGIC COPY INTO orders_csv_bronze
# MAGIC FROM '/tmp/retail_lakehouse/raw_data/incoming_csv/orders_batch1'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('header' = 'true');
# MAGIC 
# MAGIC -- Re-run to verify idempotency (num_affected_rows should be 0)
# MAGIC COPY INTO orders_csv_bronze
# MAGIC FROM '/tmp/retail_lakehouse/raw_data/incoming_csv/orders_batch1'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS ('header' = 'true');
# MAGIC 
# MAGIC SELECT COUNT(*) AS row_count FROM orders_csv_bronze;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable

src_parquet = "/tmp/retail_lakehouse/raw_data/legacy_parquet/orders"
work_parquet = "/tmp/retail_lakehouse/day02_convert_orders"
dbutils.fs.rm(work_parquet, recurse=True)
dbutils.fs.cp(src_parquet, work_parquet, recurse=True)

# Convert Parquet to Delta in-place
DeltaTable.convertToDelta(spark, f"parquet.`{work_parquet}`")

# Verify it is now a Delta table
print("Is Delta:", DeltaTable.isDeltaTable(spark, work_parquet))
print("Row count:", spark.read.format("delta").load(work_parquet).count())
