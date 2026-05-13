# Answers 026-050

## 026. Explain the concept of data partitioning in Hadoop.

**Ngan gon:** Partitioning chia data thanh cac folder/phan theo cot nhu date, country de query chi doc phan can thiet.

**Senior view:** Trong Hadoop/Hive/Spark, partition pruning giam scan IO rat lon. Chon partition key phai dua tren query pattern va cardinality. Partition qua min gay small files va metadata overhead.

**Production example:** Bang events 5TB/ngay partition `dt`, optional `hour` neu query hourly thuong xuyen. Khong partition theo `user_id` vi cardinality qua cao.

**Anti-pattern / trade-off:** Partition theo ngay tot cho time filter nhung query theo customer van phai scan nhieu. Bucketing/clustering co the bo sung.

**Follow-up:** Lam sao biet partition pruning co hoat dong? Xu ly late data vao partition cu the nao?

## 027. What is Kafka and its use cases in data engineering?

**Ngan gon:** Kafka la distributed event log dung de publish/subscribe data streams voi durability va scale cao.

**Senior view:** Kafka khong chi la message queue; no luu ordered log theo partition, consumer group doc doc lap, replay duoc theo offset. Thiet ke tot can keying, partition count, retention, schema registry va dead-letter handling.

**Production example:** Order service publish `order_created`; fraud, warehouse ingestion va notification consumers doc cung topic theo nhu cau rieng.

**Anti-pattern / trade-off:** Dung Kafka nhu database chinh la rui ro. Partition nhieu tang parallelism nhung tang overhead va kho preserve ordering.

**Follow-up:** Ordering duoc dam bao o cap nao? Exactly-once trong Kafka co nghia gi?

## 028. Describe the difference between batch processing and stream processing.

**Ngan gon:** Batch xu ly du lieu theo lo tai thoi diem dinh ky; stream xu ly lien tuc khi event den.

**Senior view:** Batch don gian hon, de backfill va reconcile. Streaming giam latency nhung phuc tap ve state, watermark, late events, exactly-once/idempotency. Nhieu he thong dung hybrid: stream cho alert, batch cho financial truth.

**Production example:** Daily revenue official tinh batch moi dem; fraud detection can stream trong vai giay.

**Anti-pattern / trade-off:** Streaming moi thu lam ops phuc tap va ton cost. Batch qua cham lam mat gia tri voi use case realtime.

**Follow-up:** Late event xu ly the nao? Khi nao micro-batch du tot?

## 029. What is Cassandra and its key features?

**Ngan gon:** Cassandra la distributed wide-column database, toi uu ghi nhieu, high availability va scale ngang.

**Senior view:** Cassandra yeu cau query-first data modeling. Partition key quyet dinh data distribution; clustering key quyet dinh sort trong partition. No khong phu hop ad-hoc joins/aggregations nhu warehouse.

**Production example:** Luu time-series device readings theo `(device_id, day)` de doc nhanh readings cua mot device trong ngay.

**Anti-pattern / trade-off:** Partition key sai tao hot partition. Denormalization la binh thuong trong Cassandra nhung tang write amplification.

**Follow-up:** Consistency level QUORUM nghia la gi? Tombstone problem la gi?

## 030. Explain the concept of data replication in Hadoop.

**Ngan gon:** HDFS replication sao chep moi block len nhieu DataNodes de chong mat data khi node fail.

**Senior view:** Replication factor mac dinh thuong la 3, dat rack-aware de replica nam o nhieu rack. Replication tang durability va read availability nhung ton storage va network.

**Production example:** File 900MB voi block 128MB tao nhieu blocks; moi block co 3 replicas. Neu mot node mat, NameNode schedule re-replication.

**Anti-pattern / trade-off:** Tang replication de "tang performance" khong phai luc nao cung dung; cache/format/partition co the hieu qua hon.

**Follow-up:** Replication khac erasure coding the nao? Monitor under-replicated blocks ra sao?

## 031. What is data processing and its stages?

**Ngan gon:** Data processing la bien raw data thanh data co ich qua collection, ingestion, validation, transformation, storage va serving.

**Senior view:** Production processing can ro contract giua stages: raw immutable, staging validated, curated business-ready. Moi stage can metadata: batch id, source, load time, quality status.

**Production example:** Clickstream: collect SDK events, ingest Kafka, validate schema, enrich geo/device, aggregate sessions, serve dashboard.

**Anti-pattern / trade-off:** Tron validation, transform va serving trong mot job lam kho debug. Nhieu layer qua co the lam delivery cham.

**Follow-up:** Stage nao nen immutable? Ban reprocess tu raw hay tu curated?

## 032. Explain the difference between batch processing and real-time processing.

**Ngan gon:** Batch xu ly theo lich; real-time xu ly gan nhu ngay lap tuc de phan ung nhanh.

**Senior view:** Real-time yeu cau latency SLO, state management, event-time semantics va alerting chat. Batch uu tien throughput, completeness va reproducibility. Real-time "official metrics" can co reconciliation batch.

**Production example:** Personalization can real-time click events; monthly invoice can batch vi can day du va chinh xac.

**Anti-pattern / trade-off:** Goi dashboard refresh 5 phut la real-time neu business chi can near-real-time. Ultra-low latency ton chi phi va phuc tap.

**Follow-up:** Freshness requirement la bao nhieu? Neu event den muon 2 gio thi ket qua co update khong?

## 033. What are the common data transformation techniques?

**Ngan gon:** Techniques gom casting type, cleaning, standardization, dedup, filtering, joining, aggregation, enrichment, pivot/unpivot va masking.

**Senior view:** Transformation production phai deterministic, testable va versioned. Business transformation nen nam trong model co owner, khong rai rac trong notebook.

**Production example:** Chuyen timezone ve UTC, normalize currency sang USD, join product category, hash email PII, aggregate revenue daily.

**Anti-pattern / trade-off:** Transform len source system co the anh huong OLTP. Transform trong warehouse de audit hon nhung ton compute scan.

**Follow-up:** Ban dat transform logic o dbt, Spark hay app service? Lam sao test transformation?

## 034. Describe the role of data cleansing in data processing.

**Ngan gon:** Data cleansing sua hoac loai bo gia tri sai, duplicate, missing, invalid format de data dang tin hon.

**Senior view:** Clean khong nen tuy tien. Can rule ro: field nao bat buoc, missing co impute duoc khong, record nao quarantine, rule nao warning. Clean phai giu raw de audit.

**Production example:** Phone number duoc chuan hoa E.164; email invalid duoc gan flag thay vi xoa neu can audit lead quality.

**Anti-pattern / trade-off:** Tu dong fill missing bang 0 co the lam metric sai. Loai bo qua nhieu record lam bias analytics.

**Follow-up:** Khi nao quarantine thay vi drop? Ai approve cleansing rule?

## 035. What is data enrichment and why is it important?

**Ngan gon:** Data enrichment them context vao raw data, vi du geo, category, customer segment, exchange rate.

**Senior view:** Enrichment bien event thap cap thanh analytical signal. Can quan ly version cua reference data; neu exchange rate hay segment thay doi, phai biet dung version tai event time hay current.

**Production example:** Payment event co currency EUR duoc enrich voi FX rate ngay giao dich de tinh USD revenue.

**Anti-pattern / trade-off:** Enrich bang API synchronous trong batch lon de bi rate limit. Snapshot enrichment giu lich su tot nhung tang storage.

**Follow-up:** Enrichment late-arriving reference data xu ly sao? Join dimension theo event time hay current time?

## 036. Explain the concept of data aggregation and its use cases.

**Ngan gon:** Aggregation gom nhieu records thanh summary nhu count, sum, avg, min, max theo dimension/time.

**Senior view:** Can hieu additive/semi-additive/non-additive metrics. Aggregation phai can nhac grain, timezone, distinct count approximation va incremental update.

**Production example:** Tinh daily active users theo ngay va platform tu event login. Official DAU can dedup user_id trong ngay.

**SQL example:**

```sql
select dt, platform, count(distinct user_id) dau
from events
where event_name = 'login'
group by dt, platform;
```

**Anti-pattern / trade-off:** Average of averages sai neu group size khac nhau. Pre-aggregate tang speed nhung giam flexibility.

**Follow-up:** DAU co tinh guest user khong? Distinct count lon toi uu the nao?

## 037. What is data deduplication and how is it achieved?

**Ngan gon:** Deduplication loai bo ban ghi trung lap dua tren key, timestamp, checksum hoac business rule.

**Senior view:** Duplicate co nhieu loai: exact duplicate, retry duplicate, business duplicate. Rule dedup phai deterministic va giu du metadata de trace ban ghi bi loai.

**Production example:** API retry gui cung `transaction_id` nhieu lan. Pipeline dung `row_number()` order by `updated_at desc` de giu latest.

**SQL example:**

```sql
select *
from (
  select *, row_number() over (partition by transaction_id order by updated_at desc) rn
  from staging_payments
) x
where rn = 1;
```

**Anti-pattern / trade-off:** Dedup theo tat ca columns se that bai neu metadata load_time khac. Dedup qua manh co the gop nham events that.

**Follow-up:** Neu khong co unique id thi dedup the nao? Dedup trong stream can state TTL bao lau?

## 038. Describe the difference between data filtering and data sorting.

**Ngan gon:** Filtering chon subset rows theo dieu kien; sorting sap xep rows theo cot.

**Senior view:** Filtering co the giam data early va tiet kiem compute. Sorting thuong ton chi phi lon vi can shuffle/distributed order. Trong warehouse, ORDER BY khong can neu downstream khong yeu cau.

**Production example:** Loc events theo `dt` truoc khi join. Sort chi dung khi tao top-N, window function hoac output deterministic.

**Anti-pattern / trade-off:** Sort dataset TB chi de "nhin dep" la lang phi. Filter sau join thay vi truoc join lam tang scan/shuffle.

**Follow-up:** ORDER BY trong subquery co dam bao output order khong? Predicate pushdown la gi?

## 039. What is data normalization and its techniques?

**Ngan gon:** Trong processing, data normalization co the la chuan hoa format/scale; trong database, normalization la tach bang giam redundancy. Can lam ro context.

**Senior view:** Interviewer co the muon nghe ca hai. Data prep normalization gom standardize case, units, date, categorical values, numeric scaling. Database normalization gom 1NF/2NF/3NF.

**Production example:** Chuan hoa `country` ve ISO code, currency ve USD, timestamp ve UTC; khac voi normalize schema customer/order.

**Anti-pattern / trade-off:** Chuan hoa qua muc lam mat raw signal. Scaling numeric can fit tren train set trong ML, khong leak future data.

**Follow-up:** Ban dang noi normalization trong DB hay data prep? Luu raw value hay normalized value?

## 040. Explain the purpose of data validation in data processing.

**Ngan gon:** Validation kiem tra data co dung schema, range, uniqueness, referential integrity va business rules truoc khi dung.

**Senior view:** Validation la contract giua producer va consumer. Can chia blocking vs non-blocking tests, log rejected rows, alert dung owner va theo doi trend quality.

**Production example:** `order_total` phai bang sum line items tru thue/giam gia trong tolerance. Neu lech tren nguong, dung load mart finance.

**Anti-pattern / trade-off:** Chi validate schema ma khong validate business invariants. Validate qua muon sau khi dashboard refresh se tao incident.

**Follow-up:** Ban luu invalid records o dau? Threshold anomaly duoc dat ra sao?

## 041. What is data integration and its challenges?

**Ngan gon:** Data integration ket hop data tu nhieu source thanh view nhat quan de analytics/operation.

**Senior view:** Kho khan nam o identity resolution, schema mismatch, latency khac nhau, ownership, PII, duplicate semantics va source reliability. Integration tot can canonical model va data contracts.

**Production example:** Gop customer tu app DB, CRM va billing can resolve email/user_id/account_id, xu ly account merge va deleted customers.

**Anti-pattern / trade-off:** "Join bang email" nhanh nhung sai khi email thay doi/shared. Master data management tot hon nhung can governance.

**Follow-up:** Source of truth cho customer la dau? Conflict giua systems xu ly the nao?

## 042. Explain the difference between ETL and ELT approaches.

**Ngan gon:** ETL transform truoc khi load vao target; ELT load raw vao warehouse/lake truoc, transform sau bang compute cua target.

**Senior view:** ELT pho bien voi cloud warehouse vi storage re, compute scale va audit raw tot. ETL phu hop khi can clean/mask truoc target, source format nang, hoac compliance khong cho raw PII vao warehouse.

**Production example:** Load raw Salesforce vao BigQuery roi dbt transform thanh marts la ELT. Mask PII truoc khi vao analytics platform la ETL.

**Anti-pattern / trade-off:** ELT khong co governance se tao raw sprawl. ETL ngoai warehouse kho debug neu khong luu intermediate data.

**Follow-up:** Khi nao ban chon ETL thay vi ELT? Raw zone co ai duoc truy cap?

## 043. What are the common data integration patterns?

**Ngan gon:** Patterns gom batch file, API polling, database replication, CDC, event streaming, federation va reverse ETL.

**Senior view:** Chon pattern dua tren latency, volume, source impact, consistency va cost. CDC tot cho thay doi gan realtime nhung can handle schema evolution/deletes. API polling de bat dau nhung de miss updates neu cursor kem.

**Production example:** Billing exports daily file, app DB dung CDC, product events dung Kafka, BI dung warehouse marts.

**Anti-pattern / trade-off:** Mot pattern cho moi source la sai. Federation nhanh cho exploration nhung khong thay the curated pipeline cho core metrics.

**Follow-up:** Pattern nao support replay? Ban giam impact len source OLTP bang cach nao?

## 044. Describe the role of data pipelines in data engineering.

**Ngan gon:** Data pipeline tu dong di chuyen va bien doi data tu source den noi su dung, co dependency, schedule va monitoring.

**Senior view:** Pipeline production la san pham van hanh: idempotent, observable, versioned, recoverable, co SLA va owner. Pipeline tot phai biet backfill va partial failure.

**Production example:** `orders_raw -> orders_stg -> fact_orders -> revenue_mart`, moi step co tests va alert freshness.

**Anti-pattern / trade-off:** Pipeline chi la cron scripts khong lineage/retry se kho scale team. Orchestrator nang cho job don gian co the overkill.

**Follow-up:** Backfill 2 nam du lieu lam sao khong pha SLA hien tai? Dependency failure propagate the nao?

## 045. What is a data lake and how does it differ from a data warehouse?

**Ngan gon:** Data lake luu raw/semi-structured/unstructured data tren storage re, schema-on-read. Warehouse luu data curated/toi uu cho analytics, schema-on-write hoac governed schema.

**Senior view:** Lake linh hoat va re cho raw history; warehouse dang tin va de query cho business. Lakehouse ket hop table format (Delta/Iceberg/Hudi), ACID, metadata va governance tren object storage.

**Production example:** Raw click JSON, images, logs vao lake; curated revenue mart vao warehouse/lakehouse table.

**Anti-pattern / trade-off:** Lake khong catalog/tests thanh data swamp. Warehouse dat hon nhung giam chaos cho BI.

**Follow-up:** Bronze/silver/gold layer la gi? Table format giup lakehouse nhu the nao?

## 046. Explain the concept of data ingestion and its methods.

**Ngan gon:** Ingestion la dua data tu source vao data platform. Methods gom batch file, API, database dump, CDC, stream va manual upload co kiem soat.

**Senior view:** Ingestion nen preserve raw data, metadata, schema version va source offsets. Can handle retries, duplicates, rate limits, partial files va secrets.

**Production example:** S3 landing zone nhan file CSV tu vendor; Airflow validate checksum, load raw, ghi manifest va batch id.

**Anti-pattern / trade-off:** Ghi de raw file lam mat kha nang audit. Ingest realtime khi source chi update daily khong co gia tri.

**Follow-up:** Ban dam bao exactly-once/at-least-once ingestion ra sao? Manifest file dung de lam gi?

## 047. What is change data capture (CDC) and its use cases?

**Ngan gon:** CDC bat cac thay doi insert/update/delete tu database source, thuong qua transaction log, de dong bo downstream.

**Senior view:** CDC tot vi it scan full table va latency thap. Production can schema evolution, ordering, snapshot initial, tombstones/deletes, lag monitoring va idempotent consumers.

**Production example:** Debezium doc Postgres WAL, publish changes vao Kafka, Spark/Flank merge vao lakehouse table.

**Anti-pattern / trade-off:** CDC log khong thay the business events; update row co the khong noi du ly do business. CDC phuc tap hon daily batch.

**Follow-up:** Initial snapshot ket hop streaming changes the nao? Delete event merge vao warehouse ra sao?

## 048. Describe the difference between batch and streaming data integration.

**Ngan gon:** Batch integration gom data theo lo dinh ky; streaming integration di chuyen event lien tuc.

**Senior view:** Batch de reconcile va co completeness cao; streaming cho freshness thap nhung can offset, state, backpressure, late data va schema compatibility. Dung streaming phai co plan replay.

**Production example:** Inventory snapshot moi dem batch; payment authorization stream cho fraud/risk.

**Anti-pattern / trade-off:** Streaming vao warehouse nhung dashboard refresh moi 24h la lang phi. Batch hourly co the du cho nhieu SLA.

**Follow-up:** SLA freshness that su la gi? Lam sao test streaming pipeline?

## 049. What is data replication and its techniques?

**Ngan gon:** Data replication copy data tu source sang mot hoac nhieu target de tang availability, performance hoac analytics access.

**Senior view:** Techniques gom snapshot/full copy, incremental timestamp, log-based CDC, physical replication, logical replication. Can ro consistency model: sync, async, eventual.

**Production example:** OLTP Postgres async replica cho read-heavy app; log-based replication sang warehouse cho analytics.

**Anti-pattern / trade-off:** Async replica co lag, khong dung cho decision can latest transaction tuyet doi. Sync replication tang consistency nhung tang write latency.

**Follow-up:** Replica lag monitor bang gi? Replication co copy deletes va schema changes khong?

## 050. Explain the purpose of data orchestration in data pipelines.

**Ngan gon:** Orchestration dieu phoi thu tu job, schedule, dependency, retry, alert va backfill cua pipelines.

**Senior view:** Orchestrator nhu Airflow/Dagster/Prefect khong nen chua business logic nang; no nen goi jobs idempotent va quan ly state. Production can SLAs, retries co backoff, sensors, pools, concurrency limits va lineage.

**Production example:** DAG chay extract orders, validate staging, build dim/fact, run dbt tests, publish mart. Neu validation fail thi dung publish va alert data owner.

**Anti-pattern / trade-off:** Cron scripts don gian nhanh nhung kho observe dependency. Orchestrator qua phuc tap cho pipeline nho tang ops overhead.

**Follow-up:** Retry job co gay duplicate khong? Backfill thang cu co anh huong run hang ngay khong?

