# Databricks notebook source
# MAGIC %md
# MAGIC # Day13 Solution: VARIANT Data Type (Semi-Structured JSON)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Ingesting rapidly changing clickstream JSON payloads without slow string parsing or rigid schemas.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE clickstream_variant (
# MAGIC   id INT,
# MAGIC   payload VARIANT
# MAGIC ) USING DELTA;
# MAGIC 
# MAGIC INSERT INTO clickstream_variant
# MAGIC SELECT 1, parse_json('{"event_id": 1, "device": "mobile", "os": "iOS"}');
# MAGIC 
# MAGIC SELECT id, payload:device::STRING AS device, payload:os::STRING AS os
# MAGIC FROM clickstream_variant;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from pyspark.sql import functions as F

raw_df = spark.read.text("/tmp/retail_lakehouse/raw_data/clickstream_json").limit(20)
variant_df = raw_df.select(F.parse_json(F.col("value")).alias("payload"))
variant_df.write.format("delta").mode("overwrite").saveAsTable("retail_lakehouse.clickstream_variant_pyspark")

display(spark.sql("SELECT payload:event_id::INT AS event_id, payload:metadata.device::STRING AS device FROM retail_lakehouse.clickstream_variant_pyspark LIMIT 5"))
