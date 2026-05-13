# Data Engineering Interview Preparation Handbook

Handbook nay la bo tai lieu on phong van Data Engineer doc lap, viet bang tieng Viet va giu cac thuat ngu English khi can thiet. Noi dung duoc xay dung tu danh sach 100 cau hoi public cua Devinterview.io/GitHub, nhung phan tra loi la dien giai rieng, tap trung vao he thong production, scalability, cost, monitoring va trade-off thuc te.

## Cau truc danh muc

1. **SQL & Modeling**: data modeling, normalization, OLTP/OLAP, star schema, SCD, keys.
2. **ETL / ELT**: extract, transform, load, staging, lineage, CDC, ingestion, integration pattern.
3. **Data Warehouse**: warehouse, mart, lake, lakehouse, storage, indexing, partitioning, archiving.
4. **Spark / Big Data**: Hadoop, HDFS, MapReduce, Hive, Spark, Flink, Cassandra, partitioning, replication.
5. **Kafka / Streaming**: Kafka, batch vs streaming, real-time processing, stream integration.
6. **Cloud**: AWS, Azure, GCP, S3, BigQuery, Redshift, Glue, Dataflow, Lambda, Databricks.
7. **Orchestration**: Airflow, NiFi, Azure Data Factory, scheduling, retries, dependency management.
8. **Data Quality**: profiling, cleansing, validation, deduplication, stewardship, governance.
9. **Monitoring & Optimization**: monitoring, query optimization, caching, compression, cost and performance.
10. **Architecture & Senior Mindset**: trade-offs, ownership, reliability, security, governance, system design.

## Cach hoc

- Bat dau bang `QUESTION_MAP_100.md` de nam pham vi va do kho.
- Moi ngay chon 5-8 cau, tu tra loi bang loi cua minh truoc khi doc dap an.
- Sau khi doc, viet lai mot version ngan 60-90 giay nhu dang tra loi phong van.
- Voi moi cau, luon them: example production, anti-pattern, trade-off, monitoring signal.
- Lap lai sau 3 ngay: neu khong giai thich duoc bang vi du thuc te, cau do chua nam.

## Interview prep flow de xuat

1. **Round 1 - Foundation**: SQL & Modeling, ETL/ELT, Data Warehouse.
2. **Round 2 - Scale**: Spark, Hadoop, partitioning, indexing, sharding, caching.
3. **Round 3 - Real-time**: Kafka, streaming, CDC, batch vs stream, latency trade-offs.
4. **Round 4 - Cloud**: AWS/Azure/GCP services, serverless, cost, IAM, storage design.
5. **Round 5 - Senior**: architecture, governance, monitoring, incident handling, stakeholder trade-offs.

## Thu tu hoc khuyen nghi

1. Cau 1-20: Nen tang modeling, warehouse, ETL.
2. Cau 31-50: Transformation, integration, pipeline thinking.
3. Cau 51-60: Storage/retrieval, partitioning, indexing, scaling.
4. Cau 65-80: Quality, monitoring, optimization.
5. Cau 21-30 va 81-90: Big data tools, Spark, Kafka, Airflow, dbt.
6. Cau 91-100: Cloud data engineering.
7. Cuoi cung quay lai cau 61-70: Governance, security, audit, vi day thuong phan biet Mid va Senior.

## Cach dung template

Dung `ANSWER_TEMPLATE.md` de tu tao them cau tra loi cua rieng ban. Trong phong van, dap an tot khong chi la dinh nghia; can chung minh ban biet van hanh pipeline that: retry, idempotency, schema evolution, backfill, data quality, lineage, cost va observability.

