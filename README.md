# Databricks Delta Lake: 30-Day Industry Practice Challenge

A hands-on, industry-standard 30-day practice repository to master **Delta Lake** in **Databricks** using both **SQL** and **PySpark**. Built around a realistic **E-Commerce & Logistics Lakehouse (`retail_lakehouse`)** domain.

## Repository Structure

```text
databricks-delta-lake-30-days/
├── README.md                          # Main guide & 30-day curriculum
├── Day00_Setup.py                     # Run this FIRST to generate all datasets
├── assignments/                       # 30 hands-on problem notebooks (starter templates)
│   ├── README.md
│   ├── Day01_Managed_vs_External_Tables.py
│   ├── ...
│   └── Day30_Capstone_Medallion_Pipeline.py
└── solutions/                         # 30 complete SQL + PySpark solution notebooks
    ├── README.md
    ├── Day01_Managed_vs_External_Tables_Solution.py
    ├── ...
    └── Day30_Capstone_Medallion_Pipeline_Solution.py
```

## Quick Start (Databricks Community Edition & Enterprise)

1. **Import into Databricks:**
   - **GitHub / Databricks Repos (Enterprise):** Clone this repository directly via **Workspace > Repos > Add Repo**.
   - **Databricks Community Edition:** Download this repo as a ZIP, unzip it, and import `Day00_Setup.py` and the `assignments/` notebooks via **Workspace > Import**.
2. **Run `Day00_Setup.py` First:**
   - Attach the notebook to a cluster and click **Run All**.
   - This creates the `retail_lakehouse` database and generates synthetic Parquet, CSV, JSON, and Delta datasets in `/tmp/retail_lakehouse/raw_data` (no external downloads required).
3. **Solve 1 Assignment Per Day:**
   - Open `assignments/DayXX_*.py`, read the industry scenario and instructions, and write your SQL and PySpark solutions directly in the `# TODO` cells.
   - Check your work against `solutions/DayXX_*_Solution.py`.

## 30-Day Curriculum

### Week 1: Core Foundations, ACID Transactions & DML
- **Day 01:** Managed vs. External Tables & `_delta_log`
- **Day 02:** Convert to Delta & `COPY INTO`
- **Day 03:** CRUD & Selective Overwrites (`replaceWhere`)
- **Day 04:** `MERGE INTO` (Upserts & Deduplication)
- **Day 05:** SCD Type 2 Pattern
- **Day 06:** Time Travel & Audit History
- **Day 07:** Disaster Recovery (`RESTORE`)

### Week 2: Schema Governance, Data Quality & Modern Types
- **Day 08:** Schema Enforcement & Evolution
- **Day 09:** Column Mapping (Rename & Drop Columns)
- **Day 10:** Type Widening
- **Day 11:** Data Quality Constraints (`NOT NULL`, `CHECK`)
- **Day 12:** Generated & `IDENTITY` Columns
- **Day 13:** `VARIANT` Data Type (Semi-Structured JSON)
- **Day 14:** Table Properties & `DROP FEATURE`

### Week 3: Performance Optimization & Storage Management
- **Day 15:** Small File Compaction (`OPTIMIZE`)
- **Day 16:** Data Skipping & Z-Ordering
- **Day 17:** Liquid Clustering
- **Day 18:** Deletion Vectors (Merge-on-Read)
- **Day 19:** `VACUUM` & Storage Cleanup
- **Day 20:** Predictive Optimization & File Sizing
- **Day 21:** Shallow & Deep Clones

### Week 4: Streaming, CDC, Interoperability & Capstone
- **Day 22:** Change Data Feed (CDF)
- **Day 23:** Row Tracking
- **Day 24:** Unified Batch & Streaming
- **Day 25:** Auto Loader (`cloudFiles`)
- **Day 26:** Concurrency & Isolation Levels
- **Day 27:** Delta UniForm (Iceberg Interoperability)
- **Day 28:** Delta Sharing
- **Day 29:** Auto TTL & GDPR Compliance
- **Day 30:** Capstone: Production Medallion Pipeline
