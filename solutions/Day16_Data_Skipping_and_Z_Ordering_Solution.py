# Databricks notebook source
# MAGIC %md
# MAGIC # Day16 Solution: Data Skipping & Z-Ordering
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Speeding up point lookups on high-cardinality columns (`customer_id`) in partitioned tables.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE orders_zorder
# MAGIC PARTITIONED BY (region)
# MAGIC AS SELECT * FROM orders_base;
# MAGIC 
# MAGIC OPTIMIZE orders_zorder ZORDER BY (customer_id);
# MAGIC DESCRIBE HISTORY orders_zorder;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "retail_lakehouse.orders_zorder")
metrics = dt.optimize().executeZOrderBy("customer_id")
display(metrics)
