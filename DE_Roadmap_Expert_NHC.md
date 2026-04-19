# Roadmap trở thành Data Engineer Expert
> Dựa trên `data-engineer-handbook` · Cập nhật: 2026-04-19  
> Xuất phát điểm: **đã biết ETL + SQL** · Mục tiêu: **Senior-ready DE trong 6–9 tháng**

---

## 1. Định nghĩa "Expert" trong roadmap này

Bạn đạt mức **Data Engineer Expert (thực chiến)** khi có thể:

1. Thiết kế data model chuẩn cho analytics (Star Schema, SCD Type 1/2, Fact/Dimension).
2. Xây batch pipeline có kiểm soát chất lượng, idempotent, incremental.
3. Dùng **dbt** để transform data có test, documentation, version control.
4. Orchestrate pipeline bằng **Airflow** trên môi trường cloud thực tế.
5. Xử lý dữ liệu lớn với **Spark** (join strategy, partitioning, unit test).
6. Triển khai **Flink/Kafka** pipeline real-time với sessionization.
7. Thiết kế KPI, experiment và chuyển hóa thành dashboard phục vụ business.
8. Vận hành production mindset: ownership, on-call, runbook, trade-off speed vs debt.
9. Có portfolio end-to-end + pass được SQL/modeling/architecture interview.

---

## 2. Nguyên tắc học

- Nhịp đề xuất: **12–15 giờ/tuần** trong **24–28 tuần** (~6–7 tháng thực tế khi đi làm full-time).
- Công thức: **30% lý thuyết + 70% build artifact**.
- Mỗi tuần phải có **1 commitable output** đẩy lên GitHub.
- Mỗi artifact có `README` ngắn: mục tiêu · input · output · cách chạy · kết quả.
- Học theo thứ tự — **không nhảy cóc**: dbt trước Spark, Airflow trước Flink.

---

## 3. Tech Stack theo từng giai đoạn

```
Giai đoạn 0-1  →  SQL · Python · PostgreSQL · Docker · Git
Giai đoạn 2    →  dbt · Airflow · Data Modeling · Data Cleaning
Giai đoạn 3    →  Spark · Cloud (AWS/GCP) · Snowflake/BigQuery · Airbyte
Giai đoạn 4    →  Flink · Kafka · Real-time · ClickHouse/DuckDB
Giai đoạn 5    →  KPI · A/B Testing · Dashboard · Tableau/Metabase
Giai đoạn 6    →  Capstone · Portfolio · Interview Prep
```

---

## 4. Lộ trình theo giai đoạn

---

### ▶ GIAI ĐOẠN 0 — Setup Môi Trường (Tuần 0)

**Mục tiêu:** Có môi trường học hoàn chỉnh trước khi bắt đầu bất kỳ module nào.

#### Tài liệu
- `beginner-bootcamp/software.md`
- `intermediate-bootcamp/materials/1-dimensional-data-modeling/README.md`
- `intermediate-bootcamp/materials/3-spark-fundamentals/README.md`

#### Việc phải xong
- [ ] Docker cài xong, `docker compose up` chạy được
- [ ] Python 3.11+ sẵn sàng, có virtual environment
- [ ] PostgreSQL local/container truy cập được
- [ ] Git + GitHub repo `de-roadmap-artifacts` đã tạo
- [ ] VS Code + extensions: Python, SQLTools, Docker, Jupyter
- [ ] Spark local chạy được 1 notebook đơn giản

#### Exit criteria
> Chụp lại `docker ps` + chạy thử 1 query SQL + 1 cell Spark notebook. Commit lên repo.

---

### ▶ GIAI ĐOẠN 1 — Foundation (Tuần 1–4)

**Mục tiêu:** Nắm chắc nền tảng SQL, Python, tư duy pipeline — chuẩn bị cho mọi thứ tiếp theo.

#### Tài liệu
- `beginner-bootcamp/introduction.md`
- `data_cleaning.md` ← **đọc song song từ tuần 2**

---

#### Module 101 · SQL Nâng Cao cho DE (Tuần 1)

**Nội dung:**
- Window functions: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `NTILE`
- Running totals, moving average, percentile
- `GROUPING SETS`, `ROLLUP`, `CUBE`
- CTE phức tạp, recursive CTE
- Query optimization: EXPLAIN ANALYZE, index, partition pruning

**Artifact bắt buộc:** `week1_sql_advanced.sql`
```
- 5 bài window function thực tế (doanh thu, retention, ranking)
- 2 bài recursive CTE (hierarchy, series)
- 1 bài GROUPING SETS phân tích đa chiều
- EXPLAIN ANALYZE trước/sau optimize cho 1 query chậm
```

**Tài nguyên:**
- [Mode SQL Tutorial](https://mode.com/sql-tutorial/)
- [SQLZoo Window Functions](https://sqlzoo.net/)
- Blog kỹ thuật: Netflix, Airbnb, Uber (link trong README repo)

---

#### Module 102 · Python cho DE (Tuần 2)

**Nội dung:**
- `pandas`: đọc/ghi CSV, JSON, Parquet, xử lý null, merge, groupby
- `sqlalchemy`: kết nối DB, execute query, bulk insert
- `requests`: gọi REST API, xử lý pagination, rate limit
- `logging`: structured logging, log levels, log to file
- Error handling: try/except, retry pattern
- Module hóa code: tách extract/transform/load thành functions

**Artifact bắt buộc:** `week2_python_etl/`
```
extract.py     — đọc từ CSV + API
transform.py   — làm sạch, chuẩn hóa, validate
load.py        — ghi vào PostgreSQL (incremental)
pipeline.py    — orchestrate 3 bước trên
README.md      — mô tả pipeline, cách chạy
```

**Tài nguyên:**
- [Start Data Engineering](https://www.startdataengineering.com)
- Sách: *Fundamentals of Data Engineering* — chương 2, 5

---

#### Module 103 · Data Cleaning (Tuần 3)

> Dựa trực tiếp trên `data_cleaning.md` trong repo

**Nội dung:**
- Identify: missing values, duplicates, outliers, wrong data types
- Strategies: imputation, deduplication, normalization, validation rules
- Data profiling: đánh giá chất lượng dữ liệu trước khi load
- Tidy Data principles (whitepaper Hadley Wickham)
- Defensive programming: assert, schema validation với `pandera`

**Artifact bắt buộc:** `week3_data_cleaning/`
```
profiling_report.ipynb  — phân tích chất lượng 1 dataset thực tế
cleaning_pipeline.py    — áp dụng các kỹ thuật cleaning
validation_rules.py     — schema + business rules validation
before_after_comparison.md
```

---

#### Module 104 · Tư Duy Pipeline (Tuần 4)

**Nội dung:**
- DAG (Directed Acyclic Graph): node, edge, dependency
- Idempotency: pipeline chạy nhiều lần cho cùng kết quả
- Backfill vs incremental vs full load — khi nào dùng gì
- Failure handling: retry, dead letter queue, alerting
- Monitoring cơ bản: row count check, null check, freshness check
- SLA và data contract

**Artifact bắt buộc:** `week4_pipeline_design.md`
```
- Vẽ DAG cho 1 pipeline ETL thực tế (dạng text/diagram)
- Giải thích idempotency strategy
- Failure scenario + xử lý cho từng bước
- Monitoring checklist
- Trade-off: full load vs incremental cho use case cụ thể
```

#### Exit criteria Giai đoạn 1
> Hoàn thành 4 artifact. Trình bày được quyết định thiết kế cho từng artifact (tại sao làm thế này, không làm thế kia).

---

### ▶ GIAI ĐOẠN 2 — Core Skills: Modeling + dbt + Airflow (Tuần 5–12)

**Mục tiêu:** Đây là giai đoạn quan trọng nhất. Sau giai đoạn này bạn đã đủ để apply vị trí DE mid-level.

---

#### Module 201 · Dimensional Data Modeling (Tuần 5–6)

> Dựa trực tiếp: `intermediate-bootcamp/materials/1-dimensional-data-modeling/`

**Nội dung:**
- Grain: định nghĩa 1 row trong fact table là gì
- Dimension table: attribute, surrogate key, natural key
- Fact table: additive/semi-additive/non-additive facts
- Star Schema vs Snowflake Schema — khi nào dùng gì
- **SCD Type 1, 2, 3** — implement từng loại bằng SQL thực tế
- Cumulative Table Design (design pattern từ repo)
- Backfill strategy cho historical data

**Artifact bắt buộc** (theo homework repo):
```sql
-- DDL bảng actors
-- Query cumulative theo từng năm
-- DDL + backfill + incremental cho actors_history_scd (SCD Type 2)
-- Star schema cho 1 domain tự chọn (e-commerce/streaming/fintech)
```

**Tài nguyên:**
- `intermediate-bootcamp/materials/1-dimensional-data-modeling/homework/homework.md`
- [Cumulative Table Design](https://github.com/DataExpert-io/cumulative-table-design)
- Sách: *Fundamentals of Data Engineering* — chương 8

---

#### Module 202 · Fact Data Modeling (Tuần 7)

> Dựa trực tiếp: `intermediate-bootcamp/materials/2-fact-data-modeling/`

**Nội dung:**
- Transaction fact vs Periodic snapshot vs Accumulating snapshot
- Deduplication: `ROW_NUMBER` pattern, Microbatch deduplication
- Reduced fact tables: tiết kiệm storage với bit arrays / compressed format
- Incremental load cho fact table: MERGE, UPSERT, INSERT-only

**Artifact bắt buộc** (theo homework repo):
```sql
-- Dedup query chuẩn production
-- user_devices_cumulated
-- hosts_cumulated
-- host_activity_reduced (dạng bit-packed hoặc array)
-- Incremental load script cho bảng reduced fact
```

**Tài nguyên:**
- `intermediate-bootcamp/materials/2-fact-data-modeling/homework/homework.md`
- [Microbatch Deduplication](https://github.com/EcZachly/microbatch-hourly-deduped-tutorial)

---

#### Module 203 · dbt — Transform Data bằng SQL (Tuần 8–9) ⭐ QUAN TRỌNG

> **Đây là kỹ năng bị thiếu trong roadmap cũ — bắt buộc phải có**

**Nội dung:**
- dbt là gì: T trong ELT, không phải ETL
- Project structure: `models/`, `tests/`, `macros/`, `seeds/`, `snapshots/`
- Model types: `view`, `table`, `incremental`, `ephemeral`
- `ref()` và `source()`: quản lý dependency giữa models
- Built-in tests: `unique`, `not_null`, `accepted_values`, `relationships`
- Custom tests và `dbt-expectations`
- Documentation: `schema.yml`, `dbt docs generate`, `dbt docs serve`
- Snapshots: implement SCD Type 2 bằng dbt
- Macros: DRY principle trong SQL
- `dbt run`, `dbt test`, `dbt build`, `dbt source freshness`

**Artifact bắt buộc:** `dbt_project/`
```
models/
  staging/         — raw → cleaned (1:1 với source)
    stg_orders.sql
    stg_customers.sql
  intermediate/    — business logic
    int_order_items_enriched.sql
  marts/           — final output cho BI
    fct_orders.sql
    dim_customers.sql (snapshot SCD2)

tests/
  generic/         — custom test
  singular/        — one-off test

README.md — lineage diagram, cách chạy, test coverage
```

**Tài nguyên:**
- [dbt Learn](https://learn.getdbt.com) — miễn phí, làm hết các course
- [dbt Best Practices](https://docs.getdbt.com/guides/best-practices)
- Repo: dbt trong mục Data Quality của README

---

#### Module 204 · Airflow — Orchestration (Tuần 10–11)

**Nội dung:**
- Kiến trúc Airflow: Scheduler, Executor, Worker, Metadata DB, Webserver
- DAG: định nghĩa, schedule (`cron`, `@daily`, `timedelta`)
- Operators: `PythonOperator`, `BashOperator`, `SQLExecuteQueryOperator`
- Task dependencies: `>>`, `<<`, `set_upstream`, `set_downstream`
- `XCom`: truyền data giữa tasks
- Variables và Connections: quản lý config/secret
- Sensors: `FileSensor`, `ExternalTaskSensor`, `HttpSensor`
- Retry, timeout, SLA miss
- Dynamic DAGs: generate DAG từ config
- Tích hợp dbt + Airflow: `DbtRunOperator`, `DbtTestOperator`

**Artifact bắt buộc:** `airflow_dags/`
```
dags/
  etl_orders_daily.py       — batch pipeline chạy 6AM/ngày
  dbt_pipeline.py           — trigger dbt run + test sau ETL
  data_quality_check.py     — row count + null check + freshness
  backfill_historical.py    — DAG cho backfill

README.md — hướng dẫn setup local với Docker Compose
```

**Tài nguyên:**
- [Astronomer Learn](https://learn.astronomer.io) — miễn phí
- [Marc Lamberti YouTube](https://www.youtube.com/@marclamberti) — top Airflow creator

---

#### Module 205 · Data Quality & Testing (Tuần 12)

**Nội dung:**
- Tầng testing: unit test (transform logic) → integration test (pipeline) → data quality test (output)
- Great Expectations: `ExpectationSuite`, `Checkpoint`, data docs
- Soda: SQL-based checks, `scan.yml`
- dbt tests nâng cao: `dbt-expectations`, custom macros
- Anomaly detection cơ bản: row count deviation, value range check
- Data contracts: định nghĩa schema + SLA giữa producer và consumer

**Artifact bắt buộc:** `data_quality/`
```
great_expectations/
  expectations/orders_suite.json
  checkpoints/daily_check.yml
soda/
  checks/orders_checks.yml
dbt_tests/
  custom_test_accepted_range.sql
README.md — test strategy, khi nào fail thì alert gì
```

#### Exit criteria Giai đoạn 2
> Bạn có **mini data platform batch hoàn chỉnh**: modeling đúng · dbt transform có test · Airflow schedule · data quality check pass. Đủ để apply DE mid-level.

---

### ▶ GIAI ĐOẠN 3 — Cloud + Big Data (Tuần 13–17)

**Mục tiêu:** Đưa pipeline từ local lên production-like environment. Học Spark xử lý dữ liệu lớn.

---

#### Module 301 · Cloud Platform — Chọn 1 trong 3 (Tuần 13)

> Repo gợi ý cả 3. Tại Việt Nam: **AWS phổ biến nhất**, GCP có BigQuery mạnh.

**Nội dung (lấy AWS làm ví dụ):**
- S3: object storage, partitioning, lifecycle policy
- IAM: roles, policies, least privilege
- RDS/Aurora: managed PostgreSQL cho metadata
- Redshift hoặc Athena: query engine trên S3
- Lambda: serverless trigger cho pipeline nhỏ
- CloudWatch: logging và monitoring pipeline
- AWS Glue Catalog: metadata layer cho Data Lake

**Artifact bắt buộc:** `cloud_setup/`
```
terraform/ hoặc CloudFormation/
  s3_buckets.tf        — raw / staging / curated / archive
  iam_roles.tf         — DE role với least privilege
  rds_metadata.tf      — Airflow metadata DB
README.md — kiến trúc, cost estimate, security notes
```

**Tài nguyên:**
- [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/)
- [Qwiklabs](https://www.qwiklabs.com/) — hands-on lab miễn phí

---

#### Module 302 · Data Warehouse Hiện Đại (Tuần 14)

**Nội dung:**
- Snowflake hoặc BigQuery: virtual warehouse, query history, cost control
- Columnar storage: tại sao nhanh hơn row-based cho analytics
- Clustering, partitioning, materialized views
- Apache Iceberg: table format, time travel, schema evolution, ACID
- Data Lakehouse: kết hợp DWH + Data Lake
- So sánh: Snowflake vs BigQuery vs Databricks vs Redshift

**Artifact bắt buộc:**
```
- Migrate dbt project từ PostgreSQL → Snowflake/BigQuery
- Demo time travel với Apache Iceberg
- Cost comparison report: 3 warehouse cho cùng workload
```

**Tài nguyên:**
- [Apache Iceberg docs](https://iceberg.apache.org/)
- [Lakehouse whitepaper](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)
- [Onehouse blog](https://www.onehouse.ai/blog)

---

#### Module 303 · Data Integration — Ingestion Tools (Tuần 15)

> Phần này bị thiếu hoàn toàn trong roadmap cũ

**Nội dung:**
- ELT vs ETL: tại sao ELT thắng thế với cloud DWH
- **Airbyte**: connector-based ingestion, custom connector
- **Fivetran**: managed ingestion, transformation layer
- **dlt** (data load tool): Python-native, lightweight
- **Sling**: SQL-to-SQL ingestion đơn giản
- Change Data Capture (CDC): Debezium, log-based vs trigger-based
- Schema evolution: thêm cột mới không break pipeline

**Artifact bắt buộc:** `data_ingestion/`
```
airbyte/
  connection_config.json    — source → destination setup
dlt_pipeline/
  load_api_to_dw.py         — API → Snowflake/BigQuery bằng dlt
cdc_demo/
  debezium_config.json      — CDC từ PostgreSQL
README.md — khi nào dùng Airbyte vs dlt vs Fivetran
```

**Tài nguyên:**
- [Airbyte docs](https://airbyte.io)
- [dlt hub](https://dlthub.com/)
- Repo README mục Data Integration

---

#### Module 304 · Apache Spark (Tuần 16–17)

> Dựa trực tiếp: `intermediate-bootcamp/materials/3-spark-fundamentals/`

**Nội dung:**
- Spark architecture: Driver, Executor, Stage, Task, Shuffle
- RDD vs DataFrame vs Dataset
- Transformations vs Actions: lazy evaluation
- Join strategies: Broadcast Join, Sort-Merge Join, Shuffle Hash Join
- Partitioning: `repartition` vs `coalesce`, `partitionBy` khi ghi file
- Bucketing: tối ưu join lặp lại
- `sortWithinPartitions`: giảm shuffle khi sort
- Caching và Persistence: khi nào nên cache
- Spark UI: đọc DAG, xác định bottleneck
- Unit testing Spark: fake input → expected output

**Artifact bắt buộc** (theo homework repo):
```python
# spark_jobs/
#   broadcast_join_job.py        — demo broadcast join nhỏ vs lớn
#   bucket_join_job.py           — so sánh before/after bucket
#   aggregation_optimized.py     — tối ưu groupBy + agg
#   sort_within_partitions.py    — so sánh strategy
#   tests/
#     test_transform_functions.py — unit tests có fake DataFrame
```

**Tài nguyên:**
- `intermediate-bootcamp/materials/3-spark-fundamentals/homework/`
- [Rock the JVM](https://rockthejvm.com/) — Spark in Scala/Python
- Sách: *Designing Data-Intensive Applications* — chương 10, 11

#### Exit criteria Giai đoạn 3
> Pipeline chạy trên cloud thực tế (không chỉ local). Spark job có optimization rõ ràng và unit test pass. Airbyte/dlt ingest được từ ít nhất 1 nguồn bên ngoài.

---

### ▶ GIAI ĐOẠN 4 — Real-time & Analytics Patterns (Tuần 18–22)

**Mục tiêu:** Mở rộng sang streaming và analytics nâng cao.

---

#### Module 401 · Real-time Pipelines với Flink + Kafka (Tuần 18–19)

> Dựa trực tiếp: `intermediate-bootcamp/materials/4-apache-flink-training/`

**Nội dung:**
- Kafka: topic, partition, consumer group, offset, retention
- Flink architecture: JobManager, TaskManager, checkpoint
- DataStream API vs Table API / SQL
- Event time vs Processing time vs Ingestion time
- Watermarks: xử lý late data
- Sessionization: group events theo session gap
- Stateful processing: RocksDB state backend
- Windowing: Tumbling, Sliding, Session windows
- Kết nối Flink → Kafka → PostgreSQL/S3

**Artifact bắt buộc** (theo homework repo):
```python
# flink_jobs/
#   session_by_ip.py           — sessionize theo IP, gap 5 phút
#   session_by_host.py         — sessionize theo host
#   analysis_output.md         — 2 câu hỏi phân tích từ output session
#   kafka_producer_mock.py     — sinh data test
```

**Tài nguyên:**
- `intermediate-bootcamp/materials/4-apache-flink-training/homework/`
- [Confluent Streaming Audio Podcast](https://developer.confluent.io/podcast/)
- [RisingWave](https://risingwave.com/) — alternative nhẹ hơn Flink để học nhanh

---

#### Module 402 · Modern OLAP — Analytics tốc độ cao (Tuần 20)

> Từ mục Modern OLAP trong repo README

**Nội dung:**
- OLAP vs OLTP: tại sao cần engine riêng cho analytics
- **DuckDB**: chạy SQL analytics ngay trên laptop, file Parquet
- **ClickHouse**: columnar, cực nhanh cho time-series + event data
- **Apache Druid**: low-latency OLAP cho real-time dashboard
- So sánh: DuckDB vs ClickHouse vs BigQuery cho analytics workload
- Materialized views và pre-aggregation

**Artifact bắt buộc:**
```
- Benchmark cùng 1 query trên: PostgreSQL vs DuckDB vs ClickHouse
- Pipeline: Kafka → ClickHouse (real-time ingestion)
- DuckDB demo: query 10M rows Parquet file trong <1 giây
```

**Tài nguyên:**
- [DuckDB docs](https://duckdb.org/)
- [ClickHouse docs](https://clickhouse.com/)
- [Apache Druid](https://druid.apache.org/)

---

#### Module 403 · Analytical Patterns nâng cao (Tuần 21)

> Dựa trực tiếp: `intermediate-bootcamp/materials/4-applying-analytical-patterns/`

**Nội dung:**
- State change tracking: theo dõi thay đổi trạng thái entity theo thời gian
- `GROUPING SETS`, `ROLLUP`, `CUBE` nâng cao
- Window analysis: streak, rolling average, consecutive days active
- Funnel analysis: conversion rate qua các bước
- Cohort analysis: retention theo cohort ngày đầu tiên dùng
- Attribution modeling: first-touch, last-touch, multi-touch

**Artifact bắt buộc** (theo homework repo):
```sql
-- state_change_tracking.sql
-- grouping_sets_multidim.sql
-- streak_analysis.sql          — consecutive active days
-- funnel_analysis.sql          — step-by-step conversion
-- cohort_retention.sql         — 30/60/90 day retention
```

---

#### Module 404 · KPI, Experimentation & Dashboard (Tuần 22)

> Dựa trực tiếp: `intermediate-bootcamp/materials/5-kpis-and-experimentation/` + `6-data-impact-training/`

**Nội dung:**
- North Star Metric vs supporting metrics
- Leading vs Lagging indicators
- A/B testing: allocation, hypothesis, sample size, p-value, confidence interval
- Guardrail metrics: phát hiện regression
- Product journey analysis: path analysis, drop-off
- Dashboard design: executive summary vs operational drill-down
- Tableau Public / Metabase: tạo dashboard public để portfolio

**Artifact bắt buộc:**
```
- product_journey_analysis.sql
- ab_experiment_design.md      — 3 experiments với hypothesis đầy đủ
- kpi_framework.md             — North Star + supporting metrics
- dashboard_executive/ (Tableau Public link hoặc Metabase)
- dashboard_exploratory/ (drill-down cho analyst)
```

**Tài nguyên:**
- `intermediate-bootcamp/materials/5-kpis-and-experimentation/homework/`
- `intermediate-bootcamp/materials/6-data-impact-training/homework/`

#### Exit criteria Giai đoạn 4
> Có streaming pipeline Flink chạy được. Biết dùng DuckDB/ClickHouse cho fast analytics. Dashboard public trên Tableau/Metabase.

---

### ▶ GIAI ĐOẠN 5 — Pipeline Maintenance & Production Mindset (Tuần 23)

> Dựa trực tiếp: `intermediate-bootcamp/materials/6-data-pipeline-maintenance/`

**Mục tiêu:** Thinking như một DE đang vận hành hệ thống thực tế.

**Nội dung:**
- Ownership model: primary owner, secondary owner, stakeholder
- On-call schedule: công bằng, không burn-out
- Runbook: tài liệu xử lý incident step-by-step
- Risk register: liệt kê rủi ro + mitigation
- Data lineage: theo dõi dữ liệu từ nguồn đến output
- **OpenLineage**: open standard cho data lineage
- SLA vs SLO vs SLI cho data pipeline
- Incident post-mortem: blameless, action items cụ thể

**Artifact bắt buộc** (theo homework repo):
```
ownership_matrix.md       — primary/secondary cho từng pipeline
on_call_schedule.md       — rotation công bằng 4 người, 1 tháng
runbook_investor_metrics.md — step-by-step xử lý khi pipeline fail
risk_register.md          — top 5 rủi ro + mitigation plan
lineage_diagram.md        — lineage từ source → mart cho 1 domain
```

**Tài nguyên:**
- `intermediate-bootcamp/materials/6-data-pipeline-maintenance/homework/`
- [OpenLineage docs](https://openlineage.io/)

---

### ▶ GIAI ĐOẠN 6 — Expert Capstone (Tuần 24–27)

**Mục tiêu:** Tổng hợp tất cả kỹ năng thành 1 hệ thống end-to-end có thể demo.

#### Đề bài Capstone

Xây 1 hệ thống dữ liệu end-to-end cho domain tự chọn (e-commerce / fintech / streaming platform):

```
Layer 1 — Ingestion
  Airbyte/dlt ingest từ: API + database + file

Layer 2 — Storage
  S3/GCS (raw) → Snowflake/BigQuery (curated)
  Apache Iceberg table format

Layer 3 — Batch Transform
  dbt models: staging → intermediate → marts
  dbt tests: unit + data quality
  Airflow DAG: schedule + monitoring + alerting

Layer 4 — Stream (optional nếu domain phù hợp)
  Kafka producer → Flink sessionization → ClickHouse

Layer 5 — Big Data Compute
  Spark job: xử lý historical data lớn
  Unit tests có fake DataFrame

Layer 6 — Analytics & BI
  Analytical patterns: funnel, cohort, retention
  KPI framework + A/B experiment design
  Dashboard: executive + exploratory

Layer 7 — Operations
  Ownership matrix + On-call + Runbook
  Data lineage diagram
  Risk register
```

#### Mapping sang materials trong repo
- Modeling: `materials/1` + `materials/2`
- Spark: `materials/3`
- Streaming: `materials/4-apache-flink-training`
- Analytics: `materials/4-applying-analytical-patterns` + `materials/5`
- Dashboard: `materials/6-data-impact`
- Maintenance: `materials/6-data-pipeline-maintenance`

#### Exit criteria Capstone
> Demo được trong 20–30 phút:
> - Giải thích kiến trúc tổng thể
> - Trade-off tại sao chọn tool A thay vì tool B
> - Chỉ ra 1 incident đã xảy ra trong lúc build và cách fix
> - Nêu được business impact của hệ thống

---

### ▶ GIAI ĐOẠN SONG SONG (từ Tuần 10 trở đi) — Interview + Reading + Community

#### Interview Prep
> Dựa trực tiếp: `interviews.md`

4 vòng cần chuẩn bị:

**SQL Round**
- Window functions, CTE, optimization
- Câu hỏi thực tế: "Viết query tìm user active 3 ngày liên tiếp"
- Luyện: [StrataScratch](https://www.stratascratch.com/), [DataLemur](https://datalemur.com/)

**Data Modeling Round**
- Thiết kế schema cho use case mới (30 phút whiteboard)
- Giải thích grain, SCD choice, fact type
- Câu hỏi: "Model hệ thống đặt vé máy bay từ đầu"

**Data Architecture Round**
- System design: "Thiết kế pipeline xử lý 1TB/ngày"
- Trade-off: batch vs streaming, DWH vs Lakehouse
- Câu hỏi về: latency, scalability, cost, reliability

**Behavioral / Production Mindset**
- "Kể về lần pipeline của bạn bị fail trong production"
- "Bạn xử lý conflict với stakeholder khi họ yêu cầu data gấp như thế nào?"
- Ownership, on-call experience, post-mortem mindset

---

#### Reading Plan
> Dựa trực tiếp: `books.md` (25+ cuốn trong repo)

**Core — đọc theo thứ tự này:**

1. *Fundamentals of Data Engineering* — Joe Reis & Matt Housley
   - Đọc song song từ Giai đoạn 1, 1 chương/tuần
   - Nền tảng tư duy, không phải technical

2. *Designing Data-Intensive Applications* — Martin Kleppmann
   - Bắt đầu từ Giai đoạn 3
   - Sâu nhất về distributed systems, storage engine, streaming

3. Chọn 1 theo hướng bạn thích:
   - Spark: *Spark: The Definitive Guide* (Chambers & Zaharia)
   - Streaming: *Kafka: The Definitive Guide*
   - ML Engineering: *Designing Machine Learning Systems* (Chip Huyen)

**Whitepapers kinh điển** (đọc khi học module liên quan):
- [The Google File System](https://research.google/pubs/the-google-file-system/) — khi học Cloud
- [MapReduce](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/) — khi học Spark
- [Lakehouse Architecture](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) — khi học Iceberg
- [Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf) — khi học Data Cleaning

---

#### Community & Cập Nhật
> Dựa trực tiếp: `communities.md` + `newsletters.md`

**Tham gia ngay từ tuần 1:**
- [DataExpert.io Discord](https://discord.gg/JGumAXncAK) — hỏi bài, share output hàng tuần
- [DataTalks Club Slack](https://datatalks.club/slack) — có free bootcamp, học nhóm

**Newsletter đăng ký:**
- [DataEngineer.io Newsletter](https://blog.dataengineer.io) — Zach Wilson, weekly, thực tế
- [Start Data Engineering](https://www.startdataengineering.com) — technical, project-based
- [Data Engineering Weekly](https://www.dataengineeringweekly.com) — tổng hợp link hay

**Follow trên YouTube:**
- [Data with Zach](https://www.youtube.com/@eczachly_) — 150k+, creator của repo này
- [Seattle Data Guy](https://www.youtube.com/c/SeattleDataGuy) — 100k+, thực tế
- [ByteByteGo](https://www.youtube.com/c/ByteByteGo) — 1M+, system design

**Thói quen hàng tuần:**
- Đọc 2 newsletter
- Xem 1 video kỹ thuật
- Viết 1 note 300–500 từ về thứ vừa học (commit vào repo)

---

## 5. Chứng Chỉ — Học Khi Nào?

| Chứng chỉ | Thời điểm học | Độ ưu tiên |
|---|---|---|
| dbt Analytics Engineering | Sau Module 203 | ⭐⭐⭐ Cao nhất |
| AWS Certified Data Engineer Associate | Sau Giai đoạn 3 | ⭐⭐⭐ Cao |
| Databricks Data Engineer Associate | Sau Module 304 | ⭐⭐ Trung bình |
| Google Professional Data Engineer | Sau Giai đoạn 3 (nếu chọn GCP) | ⭐⭐ Trung bình |
| Databricks Data Engineer Professional | Sau Capstone | ⭐ Tùy nhu cầu |

**Tài nguyên:**
- Toàn bộ link chứng chỉ trong mục *Certifications Courses* của README repo

---

## 6. Portfolio Tối Thiểu Khi Apply

```
repo 1: de-data-modeling/
  - actors SCD2 + fact tables
  - dbt models staging → marts
  - dbt tests + documentation
  README: kiến trúc, design decisions

repo 2: de-spark-pipeline/
  - Spark job có broadcast + bucket join
  - sortWithinPartitions optimization
  - Unit tests với fake DataFrame
  README: benchmark before/after

repo 3: de-airflow-platform/
  - Airflow DAGs: ETL + dbt + quality check
  - Docker Compose setup
  - Alerting khi fail
  README: kiến trúc, cách deploy

repo 4: de-streaming-flink/
  - Flink sessionization job
  - Kafka producer mock
  - Output analysis
  README: sessionization logic, kết quả

repo 5: de-capstone/
  - End-to-end system đầy đủ 7 layers
  - README đầy đủ: kiến trúc, trade-off, demo video
  - Runbook + ownership matrix

bonus: de-notes/
  - 24 weekly notes (300-500 từ/note)
  - Chứng minh learning consistency
```

---

## 7. Scorecard Tự Đánh Giá (mỗi 2 tuần)

Chấm thang **0–3** cho từng năng lực:

| Năng lực | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| SQL & Data Modeling | Chưa biết | Viết được cơ bản | SCD + incremental | Tối ưu + thiết kế từ đầu |
| dbt | Chưa biết | Tạo được model | Tests + incremental | Macro + CI/CD |
| Batch Pipeline (Airflow) | Chưa biết | DAG chạy được | Retry + monitoring | Production-grade |
| Spark | Chưa biết | Chạy được job | Optimize join/partition | Unit test + UI debug |
| Streaming (Flink/Kafka) | Chưa biết | Hiểu concept | Chạy được job | Sessionization + stateful |
| Cloud (AWS/GCP) | Chưa biết | Setup được | Pipeline chạy trên cloud | Cost optimize + IAM đúng |
| Data Quality | Chưa biết | dbt test | Great Expectations | Contract + alerting |
| Business Communication | Chưa biết | Viết được README | Trình bày trade-off | Stakeholder-ready |

**Mục tiêu tốt nghiệp roadmap:** tổng điểm **≥ 18/24** và **không có mục nào dưới 2**.

---

## 8. Kế Hoạch Tuần Này (Bắt Đầu Ngay)

**Ngày 1–2:** Hoàn tất Setup Môi Trường (Giai đoạn 0)
- Cài Docker, PostgreSQL, Python, Git
- Tạo repo `de-roadmap-artifacts` trên GitHub
- Chạy thử 1 query SQL + 1 notebook Spark → commit

**Ngày 3–5:** Bắt đầu Module 101 (SQL Nâng Cao)
- Làm 3 bài window functions trên [DataLemur](https://datalemur.com/)
- Bắt đầu viết `week1_sql_advanced.sql`

**Ngày 6–7:** Đọc + Community
- Đọc chương 1–2 *Fundamentals of Data Engineering*
- Join Discord DataExpert.io, tự giới thiệu

---

> **Giữ được nhịp đều 12–15h/tuần và hoàn thành đủ artifact** → năng lực **Senior-ready Data Engineer** trong 6–9 tháng thực tế.
>
> Chìa khóa không phải học nhiều — mà là **build nhiều, commit đều, không bỏ tuần nào**.
