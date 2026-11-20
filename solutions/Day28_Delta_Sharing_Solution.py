# Databricks notebook source
# MAGIC %md
# MAGIC # Day28 Solution: Delta Sharing (OpenSharing)
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Securely sharing curated Gold tables with external partners without duplicating data.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE gold_daily_revenue AS
# MAGIC SELECT order_date, region, COUNT(*) AS total_orders, ROUND(SUM(total_amount), 2) AS revenue
# MAGIC FROM orders_base
# MAGIC GROUP BY order_date, region;
# MAGIC 
# MAGIC -- Unity Catalog Admin commands (uncomment in UC workspace):
# MAGIC -- CREATE SHARE IF NOT EXISTS logistics_partner_share;
# MAGIC -- ALTER SHARE logistics_partner_share ADD TABLE retail_lakehouse.gold_daily_revenue;
# MAGIC -- CREATE RECIPIENT IF NOT EXISTS partner_acme;
# MAGIC -- GRANT SELECT ON SHARE logistics_partner_share TO RECIPIENT partner_acme;
# MAGIC 
# MAGIC SELECT * FROM gold_daily_revenue LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

# External consumers read shared tables using:
# import delta_sharing
# df = delta_sharing.load_as_spark("config.share#logistics_partner_share.retail_lakehouse.gold_daily_revenue")
display(spark.table("retail_lakehouse.gold_daily_revenue").limit(10))
