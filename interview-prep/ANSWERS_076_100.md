# Answers 076-100

## 076. Explain the concept of data partitioning and its benefits in optimization.

**Ngan gon:** Partitioning chia data theo cot de engine bo qua phan khong can doc, giam scan va tang parallelism.

**Senior view:** Loi ich lon nhat la partition pruning va data lifecycle. Key nen match query filters, thuong la date trong analytics. Can ket hop clustering/bucketing neu query hay loc theo key khac.

**Production example:** BigQuery table partition by `event_date`, cluster by `user_id`. Query 7 ngay scan 7 partitions thay vi 3 nam.

**Anti-pattern / trade-off:** Partition theo cot cardinality cao nhu email tao metadata overload. Partition qua min tao small files.

**Follow-up:** Lam sao confirm query da prune partition? Late-arriving data vao partition cu xu ly the nao?

## 077. What is query optimization and its techniques?

**Ngan gon:** Query optimization lam truy van chay nhanh va re hon bang cach giam scan, join/shuffle, sort va intermediate data.

**Senior view:** Techniques: read explain plan, filter early, select needed columns, partition pruning, appropriate indexes/clustering, join order, broadcast small tables, pre-aggregate, materialized views, avoid functions on partition columns.

**SQL example:**

```sql
select customer_id, sum(amount)
from fact_orders
where order_date >= date '2026-01-01'
group by customer_id;
```

**Anti-pattern / trade-off:** `select *` tren columnar warehouse tang scan cost. Materialized view nhanh nhung can refresh va co stale risk.

**Follow-up:** Ban doc explain plan nhu the nao? Skew join toi uu ra sao?

## 078. Describe the difference between data compression and data deduplication.

**Ngan gon:** Compression ma hoa data de dung it bytes hon; deduplication loai bo ban sao trung lap.

**Senior view:** Compression khong thay doi logical rows; dedup thay doi dataset result. Columnar formats nhu Parquet/ORC nen dung compression. Dedup can business key va rules.

**Production example:** Parquet + ZSTD giam storage events 70%. Dedup payments theo `transaction_id` de khong tinh doanh thu hai lan.

**Anti-pattern / trade-off:** Compression manh giam storage nhung co the tang CPU decode. Dedup sai key lam mat events hop le.

**Follow-up:** Compression codec nao cho analytics? Dedup streaming can state retention bao lau?

## 079. What is data caching and its use cases in optimization?

**Ngan gon:** Caching giu data/ket qua hay dung o noi nhanh hon de giam latency, compute va source load.

**Senior view:** Use cases: BI query result cache, Redis lookup dimensions, Spark cache DataFrame dung lap lai, metadata cache, API response cache. Can invalidation, TTL, capacity va cache stampede prevention.

**Production example:** Dashboard top KPIs cache 5 phut, vi data warehouse refresh moi 15 phut va 500 users mo cung luc.

**Anti-pattern / trade-off:** Cache data nhay cam khong ma hoa/khong TTL. Cache qua lau lam stale decisions.

**Follow-up:** Cache invalidation strategy la gi? Khi nao khong nen cache?

## 080. Explain the purpose of data archiving in data optimization.

**Ngan gon:** Archiving dua data cu sang storage re/it truy cap de giam cost va lam bang active nhe hon.

**Senior view:** Archive cung la performance optimization: smaller active partitions, faster maintenance, lower backup time. Can restore workflow va catalog de biet data nam dau.

**Production example:** Giua 90 ngay order detail trong hot warehouse, chuyen older raw JSON sang cold object storage, giu aggregates 7 nam.

**Anti-pattern / trade-off:** Archive khong test restore la rui ro. Legal/compliance co the yeu cau delete vinh vien thay vi archive.

**Follow-up:** Retention policy ai quyet? Query historical 5 nam se hoat dong ra sao?

## 081. What is Apache Spark and its key features?

**Ngan gon:** Apache Spark la distributed processing engine cho batch, SQL, streaming, ML va graph workload.

**Senior view:** Features quan trong: lazy evaluation, Catalyst optimizer, Tungsten execution, DataFrame/Dataset APIs, fault tolerance qua lineage, in-memory processing, connectors. Production can tune partitions, shuffle, memory va file layout.

**Production example:** Spark doc raw Parquet 10TB, clean/enrich, write Delta table partitioned by date cho analytics.

**Anti-pattern / trade-off:** `repartition(1)` de tao mot file lam job bi bottleneck. Cache DataFrame lon khong du memory gay spill.

**Follow-up:** Narrow vs wide transformation? Shuffle la gi va vi sao dat?

## 082. Explain the difference between Spark RDDs and DataFrames.

**Ngan gon:** RDD la low-level distributed collection; DataFrame la structured API co schema va optimizer.

**Senior view:** DataFrame thuong duoc uu tien vi Catalyst optimize query plan, Tungsten optimize memory/codegen, va de doc hon. RDD dung khi can control low-level hoac data unstructured dac biet.

**Production example:** ETL Parquet/SQL nen dung DataFrame. Custom parser phuc tap co the dung RDD ban dau roi convert sang DataFrame.

**Anti-pattern / trade-off:** Dung RDD map/filter cho workload relational lam mat optimization. DataFrame UDF Python co the cham vi serialization; prefer built-in functions.

**Follow-up:** Khi nao UDF lam Spark cham? Dataset trong Scala khac DataFrame the nao?

## 083. What is Apache Airflow and its use cases?

**Ngan gon:** Airflow la workflow orchestrator tao DAG de schedule, run, retry va monitor tasks.

**Senior view:** Airflow tot cho batch orchestration, dependencies, backfill, sensors va alerting. Business logic nen nam trong SQL/Spark/dbt scripts, Airflow chi dieu phoi. Can idempotent tasks va manage concurrency.

**Production example:** DAG nightly chay ingestion, dbt models, quality checks, publish marts va Slack alert neu fail.

**Anti-pattern / trade-off:** Dung Airflow cho low-latency streaming per event la sai. Qua nhieu dynamic DAG phuc tap co the lam scheduler cham.

**Follow-up:** Catchup va backfill khac nhau the nao? Task retry co tao duplicate khong?

## 084. Describe the role of Apache Kafka in data streaming.

**Ngan gon:** Kafka la backbone cho streaming: producers ghi events vao topics, consumers doc de xu ly realtime hoac near-real-time.

**Senior view:** Kafka cung cap durability, replay, consumer groups va horizontal scale qua partitions. Design can schema registry, key strategy, retention, compaction, monitoring lag va DLQ.

**Production example:** CDC changes tu Postgres vao Kafka, stream processor update real-time inventory view va warehouse sink.

**Anti-pattern / trade-off:** Gui event khong co schema/version lam consumer vo khi producer doi field. Retention qua ngan lam khong replay duoc incident.

**Follow-up:** Consumer lag nghia la gi? Log compaction dung khi nao?

## 085. What is Talend and its key components?

**Ngan gon:** Talend la data integration/ETL platform co giao dien thiet ke job, connectors, transformation components va orchestration/deployment.

**Senior view:** Talend huu ich trong enterprise can nhieu connectors, visual ETL, metadata va governance. Diem can can nhac la version control, testing, CI/CD va vendor lock-in so voi code-first pipelines.

**Production example:** Dung Talend de dong bo Salesforce, Oracle va flat files vao warehouse voi standard components va scheduling.

**Anti-pattern / trade-off:** Keo-tha job phuc tap khong co code review se kho maintain. Tool ETL nhanh cho integration nhung co the kho tuy bien logic nang.

**Follow-up:** Ban deploy Talend job qua environments the nao? Khi nao chon Talend thay vi Airflow + Spark/dbt?

## 086. Explain the concept of data pipelines in Apache NiFi.

**Ngan gon:** NiFi xay dataflow bang processors, connections va flow files de ingest, route, transform nhe va monitor data movement.

**Senior view:** NiFi manh ve flow-based ingestion, backpressure, provenance va drag-drop operations. Phu hop routing/API/file movement, khong phai engine analytics nang nhu Spark.

**Production example:** NiFi watch SFTP folder, validate filename/checksum, route CSV vao S3 raw, bad files vao quarantine.

**Anti-pattern / trade-off:** Dung NiFi de join/aggregate dataset TB la sai cong cu. Visual flow de bat dau nhung can naming/versioning/process groups nghiem tuc.

**Follow-up:** Backpressure trong NiFi la gi? Data provenance giup debug ra sao?

## 087. What is Informatica PowerCenter and its features?

**Ngan gon:** Informatica PowerCenter la enterprise ETL tool cho mapping, transformation, workflow, metadata va connectors.

**Senior view:** No pho bien trong legacy/regulated enterprises vi governance, reliability, connectors va operational tooling. Can danh gia chi phi license, skill set va kha nang modernize sang cloud/code-first.

**Production example:** Banking ETL tu mainframe/Oracle vao enterprise warehouse voi audit logs, restartability va standard mappings.

**Anti-pattern / trade-off:** Mappings khong document/version control tot se thanh black box. Modern stack co the linh hoat hon nhung can tu build governance.

**Follow-up:** Migration PowerCenter sang cloud thach thuc gi? Mapping reusable co mat trai nao?

## 088. Describe the difference between Hadoop and Apache Flink.

**Ngan gon:** Hadoop classic tap trung distributed storage va batch MapReduce; Flink la stream processing engine voi event-time, stateful processing va low latency.

**Senior view:** Flink co native streaming va batch nhu truong hop dac biet, manh ve state, checkpoints, watermarks. Hadoop MapReduce phu hop batch lich su nhung khong tot cho realtime.

**Production example:** Hadoop/Hive build daily aggregates; Flink tinh rolling fraud score moi vai giay tu Kafka.

**Anti-pattern / trade-off:** Flink stateful jobs phai quan ly checkpoint size, state backend va upgrade. Batch Hadoop don gian hon cho workloads khong can latency.

**Follow-up:** Watermark la gi? Checkpoint khac savepoint the nao?

## 089. What is dbt (Data Build Tool) and its benefits?

**Ngan gon:** dbt la tool transform data bang SQL trong warehouse/lakehouse, ho tro models, tests, docs, lineage va CI/CD.

**Senior view:** dbt tot cho analytics engineering: versioned SQL, modular models, materializations, macros, data tests va docs. No khong ingest data; no transform sau khi data da vao platform.

**Production example:** Raw Stripe tables duoc dbt build thanh `stg_payments`, `int_revenue_events`, `mart_mrr` voi tests unique/not_null.

**Anti-pattern / trade-off:** Dung dbt models qua nhieu layer khong ro purpose lam DAG phinh to. SQL-only tot cho warehouse transforms nhung khong thay Spark cho processing phi cau truc nang.

**Follow-up:** View/table/incremental materialization chon the nao? dbt test nao nen blocking?

## 090. Explain the purpose of Presto in data querying.

**Ngan gon:** Presto/Trino la distributed SQL query engine de query data tu nhieu sources, dac biet data lake, voi latency interactive.

**Senior view:** Presto tach compute khoi storage, query Parquet/ORC tren S3/HDFS va federate sources. Tot cho ad-hoc analytics, khong phai ETL engine cho job write-heavy phuc tap.

**Production example:** Analysts query Iceberg tables tren S3 qua Trino, join voi small dimension trong Postgres connector cho exploration.

**Anti-pattern / trade-off:** Federated query qua OLTP source lon co the anh huong production. Presto can tuning memory, splits, catalog va access controls.

**Follow-up:** Presto khac Hive/Spark SQL the nao? Predicate pushdown quan trong ra sao?

## 091. What is cloud data engineering and its advantages?

**Ngan gon:** Cloud data engineering xay pipelines, storage, processing va analytics tren managed cloud services.

**Senior view:** Advantages: elastic compute, managed operations, object storage re, serverless analytics, global services, integrated IAM/monitoring. Trade-off la cost governance, vendor lock-in va data residency.

**Production example:** S3/Glue/Lambda/EMR/Redshift hoac GCS/Dataflow/BigQuery tao platform khong can tu van hanh Hadoop cluster.

**Anti-pattern / trade-off:** Cloud khong tu dong re; query scan khong kiem soat co the dat. Managed service giam ops nhung can hieu limits.

**Follow-up:** Ban thiet ke cost controls nao? Multi-cloud co dang khong?

## 092. Explain the difference between AWS, Azure, and Google Cloud Platform for data engineering.

**Ngan gon:** Ca ba deu co storage, compute, warehouse, streaming va orchestration, nhung ecosystem va naming khac nhau.

**Senior view:** AWS manh ve breadth: S3, Glue, EMR, Redshift, Kinesis. Azure phu hop Microsoft enterprise: ADLS, ADF, Synapse, Databricks. GCP rat manh serverless analytics: BigQuery, Dataflow, Pub/Sub, Dataproc.

**Production example:** Team dung Power BI/AD thuong chon Azure; team muon serverless warehouse nhanh co the chon BigQuery; org da tren AWS chon S3/Glue/Redshift.

**Anti-pattern / trade-off:** Chon cloud theo feature list ma bo qua team skill, compliance, networking va existing contracts. Multi-cloud tang complexity.

**Follow-up:** Service tuong duong cua S3/BigQuery/Dataflow tren cloud khac la gi? IAM model khac nhau the nao?

## 093. What is Amazon S3 and its use cases in data storage?

**Ngan gon:** Amazon S3 la object storage ben, scale lon, dung de luu raw data, data lake, backups, logs va static assets.

**Senior view:** S3 co durability cao, lifecycle policies, versioning, encryption, IAM/bucket policies. No khong phai file system POSIX; consistency va listing/performance pattern can hieu khi build data lake.

**Production example:** Landing zone `s3://company-raw/orders/dt=...`, curated Parquet tables, archived logs va ML datasets.

**Anti-pattern / trade-off:** Luu qua nhieu small files lam query engine cham. Public bucket/misconfigured policy la rui ro bao mat lon.

**Follow-up:** S3 partition layout thiet ke ra sao? Lifecycle policy cho raw data the nao?

## 094. Describe the role of Azure Data Factory in data integration.

**Ngan gon:** Azure Data Factory (ADF) la managed data integration/orchestration service de copy, transform va schedule pipelines tren Azure va hybrid sources.

**Senior view:** ADF manh ve connectors, Copy Activity, Mapping Data Flows, triggers, integration runtime va monitoring. Tot cho enterprise integration; logic phuc tap co the delegate sang Databricks/Synapse/dbt.

**Production example:** ADF copy data tu on-prem SQL Server qua self-hosted integration runtime vao ADLS, trigger Databricks transform.

**Anti-pattern / trade-off:** De business logic qua lon trong visual data flow kho version/review. ADF pipeline can parameterization va environment promotion nghiem tuc.

**Follow-up:** Integration Runtime la gi? ADF retry co gay duplicate load khong?

## 095. What is Google BigQuery and its key features?

**Ngan gon:** BigQuery la serverless cloud data warehouse cua GCP, toi uu analytical SQL tren data lon.

**Senior view:** Features: separation storage/compute, columnar storage, partitioning, clustering, nested/repeated fields, BigQuery ML, scheduled queries, IAM, authorized views. Billing thuong dua tren bytes processed hoac slots.

**Production example:** Luu fact events partitioned by date, cluster by user_id; analysts query SQL khong quan ly cluster.

**Anti-pattern / trade-off:** `select *` tren bang lon gay cost cao. Partition khong dung filter se scan nhieu. Serverless giam ops nhung can cost guardrails.

**Follow-up:** On-demand vs flat-rate/slots khac nhau the nao? Partition va clustering khac nhau ra sao?

## 096. Explain the concept of serverless data processing in AWS Lambda.

**Ngan gon:** AWS Lambda chay code theo event ma khong quan ly server, phu hop task nho/ngan nhu trigger ingestion, validate file, route events.

**Senior view:** Lambda co limits ve timeout, memory, package size, concurrency va cold start. Khong phu hop Spark-scale transformation lon. Nen dung voi S3 events, API, lightweight ETL, orchestration glue.

**Production example:** S3 upload file moi trigger Lambda validate schema/checksum, ghi manifest, start Glue job.

**Anti-pattern / trade-off:** Xu ly file 50GB trong Lambda la sai. Concurrency khong kiem soat co the lam qua tai downstream DB.

**Follow-up:** Idempotency trong Lambda event handler lam sao? DLQ va retry behavior the nao?

## 097. What is Azure Databricks and its benefits?

**Ngan gon:** Azure Databricks la managed Databricks/Spark platform tren Azure cho data engineering, lakehouse, ML va collaboration.

**Senior view:** Benefits: managed Spark clusters, Delta Lake, notebooks/jobs, Unity Catalog, autoscaling, integration ADLS/AAD/ADF. Tot cho large-scale transformations va lakehouse tables.

**Production example:** Bronze raw files tren ADLS duoc Databricks Auto Loader ingest vao Delta, silver clean, gold marts cho Power BI.

**Anti-pattern / trade-off:** Notebook-only production khong CI/CD/test se kho maintain. Cluster always-on gay cost cao neu khong co policies.

**Follow-up:** Delta Lake cung cap gi? Job clusters vs all-purpose clusters khac nhau the nao?

## 098. Describe the difference between Amazon Redshift and Google BigQuery.

**Ngan gon:** Redshift la AWS data warehouse cluster/serverless; BigQuery la GCP serverless warehouse. Ca hai dung cho analytics SQL nhung operating model va billing khac.

**Senior view:** Redshift truyen thong can quan ly node, sort/dist keys, workload management; Redshift Serverless giam ops. BigQuery serverless hon, billing bytes/slots, partition/cluster. Chon dua tren cloud ecosystem, workload, cost model va skills.

**Production example:** AWS-native org voi data tren S3 co the dung Redshift Spectrum/Redshift. GCP org voi event data lon dung BigQuery.

**Anti-pattern / trade-off:** Migrate chi vi benchmark don le ma bo qua governance/IAM/data egress. Redshift tuning cho performance; BigQuery tuning cho scan cost/slot usage.

**Follow-up:** Distribution key trong Redshift la gi? BigQuery clustering thay the index ra sao?

## 099. What is AWS Glue and its use cases in data integration?

**Ngan gon:** AWS Glue la managed ETL/catalog service gom Glue Data Catalog, crawlers, Spark jobs va connectors.

**Senior view:** Glue tot cho serverless Spark ETL, catalog tables tren S3, schema discovery va integration voi Athena/Redshift/EMR. Can quan ly job bookmarks, worker sizing, small files va crawler governance.

**Production example:** Glue crawler catalog raw Parquet tren S3; Glue job transform sang curated partitioned table; Athena query qua catalog.

**Anti-pattern / trade-off:** Crawler tu dong tren production co the doi schema khong kiem soat. Glue serverless tien loi nhung cold start va tuning it linh hoat hon self-managed Spark.

**Follow-up:** Glue bookmark dung de lam gi? Crawler nen chay o raw hay curated layer?

## 100. Explain the purpose of Google Cloud Dataflow in data processing.

**Ngan gon:** Google Cloud Dataflow la managed service chay Apache Beam pipelines cho batch va streaming processing.

**Senior view:** Dataflow manh ve unified batch/stream, autoscaling, windowing, watermarks, exactly-once-style processing voi supported sinks. Phu hop Pub/Sub -> transform -> BigQuery/GCS pipelines.

**Production example:** Pub/Sub nhan click events, Dataflow window 5 phut tinh metrics, ghi BigQuery va dead-letter invalid records vao GCS.

**Anti-pattern / trade-off:** Beam model co learning curve. Streaming Dataflow job chay lien tuc can monitor backlog, watermark lag, worker cost va schema errors.

**Follow-up:** Windowing va watermark la gi? Dataflow khac Dataproc/Spark nhu the nao?

