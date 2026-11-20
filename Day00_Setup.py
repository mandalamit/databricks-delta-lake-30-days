# Databricks notebook source
# MAGIC %md
# MAGIC # Day 00: Environment & Synthetic Dataset Setup
# MAGIC
# MAGIC Run this notebook **once** before starting Day 1.
# MAGIC
# MAGIC ### What this notebook creates:
# MAGIC 1. Database: `retail_lakehouse`
# MAGIC 2. Base storage path: `/tmp/retail_lakehouse/raw_data` (works on both Community Edition and Enterprise workspaces)
# MAGIC 3. Datasets:
# MAGIC    - `legacy_parquet/orders` (10,000 rows in Parquet format)
# MAGIC    - `incoming_csv/orders_batch1` (1,000 rows in CSV format)
# MAGIC    - `clickstream_json` (2,000 raw JSON event lines)
# MAGIC    - `retail_lakehouse.dim_customers` (500 customer records in Delta format)
# MAGIC    - `retail_lakehouse.orders_base` (10,000 order records in Delta format)

# COMMAND ----------

from pyspark.sql import functions as F

# Create database (works in both Hive Metastore / Community Edition and Unity Catalog)
spark.sql("CREATE DATABASE IF NOT EXISTS retail_lakehouse")
spark.sql("USE retail_lakehouse")

base_path = "/tmp/retail_lakehouse/raw_data"
dbutils.fs.mkdirs(base_path)

print("Using database: retail_lakehouse")
print("Using raw data path:", base_path)

# COMMAND ----------

# 1. Generate Orders Dataset (10,000 rows)
orders_df = (
    spark.range(1, 10001)
    .withColumnRenamed("id", "order_id")
    .withColumn("customer_id", (F.col("order_id") % 500) + 1)
    .withColumn(
        "region",
        F.element_at(
            F.array(F.lit("APAC"), F.lit("EMEA"), F.lit("NA"), F.lit("LATAM")),
            (F.col("order_id") % 4) + 1,
        ),
    )
    .withColumn(
        "status",
        F.element_at(
            F.array(F.lit("COMPLETED"), F.lit("PENDING"), F.lit("SHIPPED"), F.lit("CANCELLED")),
            (F.col("order_id") % 4) + 1,
        ),
    )
    .withColumn("total_amount", F.round(F.rand(seed=42) * 500 + 10, 2))
    .withColumn(
        "order_ts",
        F.expr("timestamp'2026-01-01 00:00:00' + make_interval(0, 0, 0, cast(order_id % 300 as int), 0, 0, 0)"),
    )
    .withColumn("order_date", F.to_date("order_ts"))
)

# Write legacy Parquet (Day 2)
orders_df.write.mode("overwrite").parquet(f"{base_path}/legacy_parquet/orders")

# Write incoming CSV batch (Day 2 & Day 25)
orders_df.limit(1000).write.mode("overwrite").option("header", "true").csv(f"{base_path}/incoming_csv/orders_batch1")

# Write base Delta table for reuse across exercises
orders_df.write.mode("overwrite").format("delta").saveAsTable("retail_lakehouse.orders_base")

print("Orders dataset generated successfully.")

# COMMAND ----------

# 2. Generate Customers Dataset (500 rows)
customers_df = (
    spark.range(1, 501)
    .withColumnRenamed("id", "customer_id")
    .withColumn("customer_name", F.concat(F.lit("Customer_"), F.col("customer_id")))
    .withColumn(
        "tier",
        F.element_at(F.array(F.lit("Bronze"), F.lit("Silver"), F.lit("Gold")), (F.col("customer_id") % 3) + 1),
    )
    .withColumn(
        "city",
        F.element_at(
            F.array(F.lit("Bengaluru"), F.lit("Mumbai"), F.lit("London"), F.lit("New York")),
            (F.col("customer_id") % 4) + 1,
        ),
    )
    .withColumn("email", F.concat(F.lit("user"), F.col("customer_id"), F.lit("@example.com")))
)

customers_df.write.mode("overwrite").format("delta").saveAsTable("retail_lakehouse.dim_customers")
print("Customers dataset generated successfully.")

# COMMAND ----------

# 3. Generate Raw JSON Clickstream (2,000 rows)
clickstream_df = (
    spark.range(1, 2001)
    .withColumn(
        "raw_json",
        F.to_json(
            F.struct(
                F.col("id").alias("event_id"),
                ((F.col("id") % 500) + 1).alias("customer_id"),
                F.lit("page_view").alias("event_type"),
                F.struct(F.lit("mobile").alias("device"), F.lit("iOS").alias("os")).alias("metadata"),
            )
        ),
    )
    .select("raw_json")
)

clickstream_df.write.mode("overwrite").text(f"{base_path}/clickstream_json")
print("Clickstream JSON dataset generated successfully.")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Verify setup
# MAGIC SHOW TABLES IN retail_lakehouse;
