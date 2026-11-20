# Databricks notebook source
# MAGIC %md
# MAGIC # Day30 Solution: Capstone: Production Medallion Pipeline
# MAGIC
# MAGIC ### Industry Scenario
# MAGIC Delivering an end-to-end Bronze -> Silver -> Gold e-commerce lakehouse combining Delta Lake best practices.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 1: SQL Solution

# COMMAND ----------

# MAGIC %sql
# MAGIC USE retail_lakehouse;
# MAGIC 
# MAGIC -- BRONZE
# MAGIC CREATE OR REPLACE TABLE capstone_orders_bronze
# MAGIC TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true')
# MAGIC AS SELECT * FROM orders_base;
# MAGIC 
# MAGIC -- SILVER
# MAGIC CREATE OR REPLACE TABLE capstone_orders_silver (
# MAGIC   order_id BIGINT NOT NULL,
# MAGIC   customer_id BIGINT,
# MAGIC   region STRING,
# MAGIC   status STRING,
# MAGIC   total_amount DOUBLE,
# MAGIC   order_ts TIMESTAMP,
# MAGIC   order_date DATE
# MAGIC ) USING DELTA
# MAGIC CLUSTER BY (region, order_date)
# MAGIC TBLPROPERTIES ('delta.enableDeletionVectors' = 'true');
# MAGIC 
# MAGIC ALTER TABLE capstone_orders_silver ADD CONSTRAINT positive_amount CHECK (total_amount >= 0);
# MAGIC 
# MAGIC MERGE INTO capstone_orders_silver t
# MAGIC USING (SELECT DISTINCT * FROM capstone_orders_bronze WHERE total_amount >= 0) s
# MAGIC ON t.order_id = s.order_id
# MAGIC WHEN MATCHED THEN UPDATE SET *
# MAGIC WHEN NOT MATCHED THEN INSERT *;
# MAGIC 
# MAGIC -- GOLD
# MAGIC CREATE OR REPLACE TABLE capstone_gold_regional_kpi AS
# MAGIC SELECT region, order_date,
# MAGIC        COUNT(order_id) AS total_orders,
# MAGIC        ROUND(SUM(total_amount), 2) AS total_revenue
# MAGIC FROM capstone_orders_silver
# MAGIC WHERE status <> 'CANCELLED'
# MAGIC GROUP BY region, order_date;
# MAGIC 
# MAGIC SELECT * FROM capstone_gold_regional_kpi ORDER BY order_date DESC, region LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Part 2: PySpark Solution

# COMMAND ----------

# End-to-end PySpark validation of the Medallion Pipeline
bronze_cnt = spark.table("retail_lakehouse.capstone_orders_bronze").count()
silver_cnt = spark.table("retail_lakehouse.capstone_orders_silver").count()
gold_cnt = spark.table("retail_lakehouse.capstone_gold_regional_kpi").count()

print(f"Capstone Pipeline Summary -> Bronze: {bronze_cnt}, Silver: {silver_cnt}, Gold KPI rows: {gold_cnt}")
assert silver_cnt > 0 and gold_cnt > 0, "Pipeline tables should not be empty!"
display(spark.table("retail_lakehouse.capstone_gold_regional_kpi").limit(10))
