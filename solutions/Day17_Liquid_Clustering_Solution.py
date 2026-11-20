# Databricks notebook source
# MAGIC %md
# MAGIC # Day17 Solution: Liquid Clustering
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Replacing rigid Hive partitioning with adaptive Liquid Clustering for evolving query patterns.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_liquid
# MAGIC CLUSTER BY (region, order_date)
# MAGIC AS SELECT * FROM orders_base;
# MAGIC 
# MAGIC OPTIMIZE orders_liquid;
# MAGIC 
# MAGIC -- Evolve clustering keys dynamically
# MAGIC ALTER TABLE orders_liquid CLUSTER BY (customer_id);
# MAGIC DESCRIBE DETAIL orders_liquid;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

(
    spark.table("retail_lakehouse.orders_base")
    .write.format("delta")
    .mode("overwrite")
    .clusterBy("region", "order_date")
    .saveAsTable("retail_lakehouse.orders_liquid_pyspark")
)
display(spark.sql("DESCRIBE DETAIL retail_lakehouse.orders_liquid_pyspark").select("name", "clusteringColumns"))
