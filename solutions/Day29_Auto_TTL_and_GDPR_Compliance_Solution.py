# Databricks notebook source
# MAGIC %md
# MAGIC # Day29 Solution: Auto TTL & GDPR Compliance
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Fulfilling Right-to-be-Forgotten (GDPR) requests by deleting user PII and purging stale files.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE customers_gdpr AS SELECT * FROM dim_customers;
# MAGIC CREATE TABLE IF NOT EXISTS gdpr_audit_log (customer_id BIGINT, deleted_at TIMESTAMP, status STRING) USING DELTA;
# MAGIC 
# MAGIC DELETE FROM customers_gdpr WHERE customer_id = 42;
# MAGIC INSERT INTO gdpr_audit_log VALUES (42, current_timestamp(), 'PURGED_FROM_TABLE');
# MAGIC 
# MAGIC SELECT * FROM gdpr_audit_log;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "retail_lakehouse.customers_gdpr")
dt.delete("customer_id = 43")
print("Remaining count for customer 42 & 43:", spark.table("retail_lakehouse.customers_gdpr").filter("customer_id IN (42, 43)").count())
# In production, run VACUUM after retention window to physically purge Parquet files
dt.vacuum(168)
