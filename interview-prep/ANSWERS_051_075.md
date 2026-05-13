# Answers 051-075

## 051. What is a database management system (DBMS) and its types?

**Ngan gon:** DBMS la phan mem quan ly luu tru, truy van, giao dich, bao mat va recovery cho data.

**Senior view:** Types gom relational, document, key-value, wide-column, graph, time-series, columnar analytics. Chon DBMS dua tren workload: transaction, analytical scan, low-latency lookup, flexible schema hay graph traversal.

**Production example:** Postgres cho transactional orders, Redis cache session, BigQuery cho analytics, Cassandra cho time-series ghi lon.

**Anti-pattern / trade-off:** Chon NoSQL chi vi "scale" nhung workload can joins/transactions se tang complexity. Mot DB cho moi thu hiem khi toi uu.

**Follow-up:** Workload read/write ratio ra sao? Consistency requirement la gi?

## 052. Explain the difference between SQL and NoSQL databases.

**Ngan gon:** SQL databases thuong relational, schema ro, query SQL, ACID manh. NoSQL linh hoat hon ve model va scale ngang, gom document/key-value/wide-column/graph.

**Senior view:** Khac biet that su nam o data model, consistency, query pattern va operational trade-off. NoSQL thuong yeu cau denormalization/query-first design; SQL manh ve constraints, joins va ad-hoc query.

**Production example:** User profile JSON co schema thay doi nhanh phu hop document DB; financial ledger can relational DB voi transaction va constraints.

**Anti-pattern / trade-off:** NoSQL khong co nghia la khong can schema. SQL co the scale rat xa voi partitioning/read replicas truoc khi can NoSQL.

**Follow-up:** CAP theorem anh huong lua chon the nao? Khi nao dung graph database?

## 053. What is data partitioning and its strategies?

**Ngan gon:** Partitioning chia table/file theo key de giam scan, tang parallelism va quan ly data de hon.

**Senior view:** Strategies gom range, list, hash, composite, time-based. Analytics hay partition by date; OLTP co the hash/range theo tenant/customer. Key tot phai can bang partition size va match filter.

**Production example:** Fact events partition by `event_date`, cluster by `user_id`; multi-tenant DB partition by tenant group de tranh hot tenant.

**Anti-pattern / trade-off:** Partition cardinality cao tao qua nhieu small partitions. Partition sai key khong giup query pruning.

**Follow-up:** Lam sao xu ly skew? Partition co thay the index khong?

## 054. Describe the concept of data indexing and its benefits.

**Ngan gon:** Index la cau truc phu giup database tim rows nhanh hon ma khong scan toan bang.

**Senior view:** Index tang read performance nhung lam cham write va ton storage. Can chon index theo query predicates, joins, sort. Columnar warehouse dung clustering/zone maps thay vi B-tree truyen thong.

**Production example:** OLTP orders can index `(customer_id, created_at)` cho query lich su don hang cua customer.

**SQL example:**

```sql
create index idx_orders_customer_created
on orders (customer_id, created_at);
```

**Anti-pattern / trade-off:** Tao index cho moi cot lam write cham. Index khong duoc dung neu function wrap column hoac predicate khong selective.

**Follow-up:** Composite index order quan trong the nao? Explain plan doc gi?

## 055. What is data sharding and when is it used?

**Ngan gon:** Sharding chia data cua mot logical database ra nhieu nodes theo shard key de scale ngang.

**Senior view:** Sharding la buoc lon vi anh huong query, transaction, rebalancing, hotspots va operations. Dung khi vertical scaling/read replicas/partitioning khong du. Shard key phai phan bo deu va match access pattern.

**Production example:** Messaging system shard conversations theo `conversation_id` de ghi/doc song song tren nhieu DB nodes.

**Anti-pattern / trade-off:** Shard theo country de de hieu nhung country lon tao hot shard. Cross-shard joins/transactions rat dat.

**Follow-up:** Re-sharding khi tang tu 16 len 64 shards lam sao? Global unique id tao the nao?

## 056. Explain the difference between vertical and horizontal scaling in databases.

**Ngan gon:** Vertical scaling tang tai nguyen mot machine; horizontal scaling them nhieu machines.

**Senior view:** Vertical don gian, it thay doi app, nhung co gioi han va single-node risk. Horizontal scale tot hon cho growth lon nhung tang complexity ve partitioning, consistency, routing va monitoring.

**Production example:** Tang Postgres instance tu 8 CPU len 32 CPU la vertical. Them read replicas/shards la horizontal.

**Anti-pattern / trade-off:** Scale out qua som tang complexity khong can thiet. Scale up mai co the den tran vat ly va chi phi cao.

**Follow-up:** Khi nao read replica du? Workload write-heavy scale the nao?

## 057. What is data replication and its types?

**Ngan gon:** Replication sao chep data sang nodes/regions khac de tang availability, read scalability va disaster recovery.

**Senior view:** Types gom synchronous/asynchronous, physical/logical, leader-follower, multi-leader, peer-to-peer. Moi loai co trade-off consistency, latency va conflict resolution.

**Production example:** Primary DB ghi o region A, async replica o region B cho DR. Analytics replica tach workload report khoi primary.

**Anti-pattern / trade-off:** Multi-leader nghe hap dan nhung conflict resolution kho. Async replica co lag nen khong doc sau ghi neu can consistency manh.

**Follow-up:** RPO/RTO la gi? Replica lag lam sai report nhu the nao?

## 058. Describe the role of caching in data retrieval.

**Ngan gon:** Cache luu ket qua/du lieu hay truy cap o tang nhanh hon de giam latency va tai cho source.

**Senior view:** Cache can invalidation strategy, TTL, key design, stampede protection va observability. Data engineering co cache query results, dimension lookup, metadata, API responses.

**Production example:** Feature service cache customer segment 5 phut trong Redis de giam query warehouse realtime.

**Anti-pattern / trade-off:** Cache stale co the gay quyet dinh sai. TTL ngan giam stale nhung giam hit rate.

**Follow-up:** Cache invalidation lam sao? Cache hit ratio va stale rate monitor the nao?

## 059. What is a data lake and its architecture?

**Ngan gon:** Data lake la kien truc luu raw va processed data tren object/distributed storage voi nhieu format va schema.

**Senior view:** Lake tot can zones: landing/raw, cleaned, curated, sandbox; catalog/metastore; table format; access control; lifecycle policy. Metadata quan trong ngang storage.

**Production example:** S3 lake: `bronze/events`, `silver/sessions`, `gold/revenue_mart`, quan ly bang Glue Catalog va Iceberg.

**Anti-pattern / trade-off:** Cho tat ca ghi tu do vao lake se mat trust. Table format nhu Delta/Iceberg tang governance nhung can ops/version compatibility.

**Follow-up:** Lakehouse khac lake ra sao? Ban xu ly small files the nao?

## 060. Explain the concept of data archiving and its importance.

**Ngan gon:** Archiving chuyen data cu/it dung sang storage re hon nhung van co the truy xuat khi can.

**Senior view:** Archive giam cost, cai thien performance bang chinh va dap ung retention/compliance. Can ro retention, legal hold, restore time va metadata de tim lai.

**Production example:** Raw clickstream sau 18 thang chuyen tu hot S3 Standard sang Glacier, giu aggregate trong warehouse.

**Anti-pattern / trade-off:** Archive khong co index/catalog thi restore nhu tim kim. Archive qua som lam backfill va audit cham.

**Follow-up:** RTO cho archive la bao lau? Data nao phai delete thay vi archive?

## 061. What is data governance and its key components?

**Ngan gon:** Data governance la bo quy tac, roles va process de data duoc quan ly dung, an toan, co owner va dang tin.

**Senior view:** Components gom ownership, catalog, lineage, quality, privacy/security, access control, policy, retention, stewardship va metric definitions. Governance tot la enablement, khong chi phe duyet.

**Production example:** Finance metric `net_revenue` co owner, definition, tests, lineage, access policy va SLA trong catalog.

**Anti-pattern / trade-off:** Governance chi la spreadsheet va committee se cham. Tu do hoan toan tao metric conflict va PII risk.

**Follow-up:** Ai la data owner vs steward? Governance do thanh cong bang metric nao?

## 062. Explain the difference between data governance and data management.

**Ngan gon:** Governance quy dinh ai co quyen, rule nao, standard nao; data management la thuc thi ky thuat va van hanh data theo rule do.

**Senior view:** Governance tra loi "should"; management tra loi "how". Vi du governance yeu cau PII masked; management implement masking, RBAC, audit logs va tests.

**Production example:** Policy: customer email chi cho support/marketing. Implementation: column-level permissions, tokenization, access audit.

**Anti-pattern / trade-off:** Governance khong co implementation la ly thuyet. Management khong co governance tao he thong tuy tien.

**Follow-up:** Khi policy va delivery deadline xung dot thi xu ly sao? Data platform enforce policy bang cach nao?

## 063. What are the common data governance frameworks?

**Ngan gon:** Frameworks pho bien gom DAMA-DMBOK, DCAM, COBIT, ISO 27001 lien quan security, va noi bo theo domain/data mesh.

**Senior view:** Framework chi la khung; can customize theo org maturity. Data mesh nhan manh domain ownership va data products, nhung can platform standards de tranh chaos.

**Production example:** Cong ty tai chinh dung DAMA cho data quality/metadata, ISO controls cho security, va domain ownership cho marts.

**Anti-pattern / trade-off:** Copy framework day du lam qua tai team. Khong framework nao thay the duoc ownership ro va automation.

**Follow-up:** Framework nao phu hop startup? Data product co SLA va contract gi?

## 064. Describe the role of data lineage in data governance.

**Ngan gon:** Lineage cho governance biet data den tu dau, bien doi the nao, ai dung va bi anh huong khi thay doi.

**Senior view:** Lineage ho tro compliance, access review, impact analysis va root cause. Column-level lineage giup biet PII di qua cot nao va report nao bi anh huong.

**Production example:** Truoc khi xoa cot `birth_date`, lineage cho thay cot nay feed vao age_group trong marketing mart va risk model.

**Anti-pattern / trade-off:** Lineage capture tu code nhung khong tu runtime co the thieu dynamic dependencies. Manual lineage nhanh loi thoi.

**Follow-up:** Lineage tu dbt/Airflow/Spark capture ra sao? Impact analysis truoc schema change gom gi?

## 065. What is data quality and its dimensions?

**Ngan gon:** Data quality la muc do data phu hop de su dung. Dimensions gom accuracy, completeness, consistency, uniqueness, validity, timeliness/freshness.

**Senior view:** Quality phai gan voi use case. Missing phone co the chap nhan cho analytics nhung khong chap nhan cho delivery. Can SLO va thresholds thay vi "100% perfect" mac dinh.

**Production example:** Dashboard daily orders yeu cau freshness < 2h, duplicate order_id = 0, null customer_id < 0.1%.

**Anti-pattern / trade-off:** Theo duoi perfect data lam delivery cham. Quality kem khong duoc quantify thi khong ai uu tien sua.

**Follow-up:** Ban dat threshold nhu the nao? Data quality incident runbook gom gi?

## 066. Explain the concept of data stewardship and its responsibilities.

**Ngan gon:** Data steward la nguoi cham soc quality, definition, metadata va usage cua mot data domain.

**Senior view:** Steward khong nhat thiet la engineer; thuong la domain expert ket hop voi data owner. Responsibilities gom approve definitions, triage quality issues, maintain catalog, review access va coordinate fixes.

**Production example:** Finance steward quyet dinh rule recognized revenue; DE implement pipeline va tests theo rule.

**Anti-pattern / trade-off:** Gan steward tren giay nhung khong co thoi gian/quyen quyet dinh. De engineer tu doan business rule la rui ro.

**Follow-up:** Steward khac owner the nao? Khi hai domain tranh chap definition thi ai quyet?

## 067. What is data security and its best practices?

**Ngan gon:** Data security bao ve data khoi truy cap, thay doi, ro ri trai phep qua IAM, encryption, masking, auditing va secure operations.

**Senior view:** Best practices: least privilege, RBAC/ABAC, encryption at rest/in transit, secrets management, network controls, PII classification, tokenization/masking, audit logs, data retention va incident response.

**Production example:** Analysts chi xem hashed email; raw PII chi cho service account co approval va access log.

**Anti-pattern / trade-off:** Share warehouse admin account. Mask data trong dashboard nhung raw table van mo. Bao mat chat co the lam workflow cham neu khong co self-service guardrails.

**Follow-up:** Ban protect PII trong lower environments ra sao? Key rotation lam the nao?

## 068. Describe the difference between authentication and authorization in data security.

**Ngan gon:** Authentication xac minh ban la ai; authorization quyet dinh ban duoc lam gi.

**Senior view:** Trong data platform, authn co the qua SSO/service accounts; authz qua roles, policies, row/column-level security. Ca hai can audit.

**Production example:** User login qua Okta la authentication. Chi duoc query `finance_mart` nhung khong duoc xem `salary_raw` la authorization.

**Anti-pattern / trade-off:** Xac thuc thanh cong khong co nghia co quyen tat ca. Role qua rong de van hanh nhanh nhung tang breach blast radius.

**Follow-up:** RBAC va ABAC khac nhau the nao? Service account permissions review ra sao?

## 069. What is data encryption and its types?

**Ngan gon:** Encryption bien data thanh dang khong doc duoc neu khong co key. Types chinh: encryption at rest, in transit, va sometimes in use.

**Senior view:** Encryption chi tot khi key management tot: KMS/HSM, rotation, separation of duties, audit. Field-level encryption/tokenization can cho PII nhay cam.

**Production example:** S3 bucket encrypted SSE-KMS, JDBC dung TLS, credit card tokenized truoc khi vao warehouse.

**Anti-pattern / trade-off:** Tu quan ly key trong code/env file la rui ro. Encryption tang an toan nhung co the anh huong search/join neu field encrypted.

**Follow-up:** Hashing khac encryption the nao? Envelope encryption la gi?

## 070. Explain the purpose of data auditing and its techniques.

**Ngan gon:** Auditing ghi nhan ai truy cap/thay doi data, luc nao, bang cach nao, de compliance va dieu tra incident.

**Senior view:** Audit can query logs, access logs, change logs, lineage, data quality history va approval records. Audit log phai tamper-resistant va co retention.

**Production example:** Khi PII export bat thuong, audit logs cho thay service account nao query cot email, query text, destination va user impersonation.

**Anti-pattern / trade-off:** Log moi thu khong co alert/review thi vo ich. Qua nhieu log ton cost va co the chua PII.

**Follow-up:** Audit log duoc luu bao lau? Lam sao detect anomalous access?

## 071. What is data monitoring and its importance?

**Ngan gon:** Data monitoring theo doi suc khoe pipeline va data: freshness, volume, quality, latency, errors, cost.

**Senior view:** Monitoring giup phat hien truoc khi stakeholder bao dashboard sai. Can monitor ca infrastructure va data semantics. Alert phai actionable, co owner va severity.

**Production example:** Alert neu `fact_orders` chua cap nhat sau 8:00, row count giam > 30%, duplicate rate > 0.

**Anti-pattern / trade-off:** Chi monitor job success nhung khong monitor data correctness. Alert qua nhieu gay fatigue.

**Follow-up:** SLI/SLO cho data pipeline la gi? Dashboard nao dung cho on-call?

## 072. Explain the difference between real-time and batch monitoring.

**Ngan gon:** Real-time monitoring phat hien gan ngay lap tuc; batch monitoring kiem tra theo run/window dinh ky.

**Senior view:** Real-time can cho streaming, fraud, ops alerts; batch phu hop daily marts, reconciliation va trend anomaly. Real-time monitoring ton chi phi va can low-noise rules.

**Production example:** Kafka consumer lag monitor realtime. Daily finance mart check row count va totals sau job ket thuc.

**Anti-pattern / trade-off:** Real-time alert cho metric khong can immediate action tao noise. Batch check qua muon co the lam report sai ca ngay.

**Follow-up:** Metric nao can page on-call? Batch validation fail thi rollback publish the nao?

## 073. What are the common data monitoring tools and techniques?

**Ngan gon:** Tools gom Airflow/Dagster UI, Prometheus/Grafana, CloudWatch, Datadog, dbt tests, Great Expectations, Monte Carlo/Bigeye, OpenLineage.

**Senior view:** Techniques gom freshness checks, volume anomaly, schema change detection, distribution drift, null/unique tests, reconciliation, lineage-based alert routing va cost monitoring.

**Production example:** Airflow monitor DAG state; dbt tests monitor constraints; Prometheus monitor Spark executor metrics; data observability tool monitor freshness va volume.

**Anti-pattern / trade-off:** Mua tool nhung khong co owner/runbook. Custom checks re ban dau nhung kho maintain khi scale domain.

**Follow-up:** Ban chon build vs buy the nao? Alert routing theo lineage ra sao?

## 074. Describe the role of data profiling in data monitoring.

**Ngan gon:** Profiling tinh thong ke ve data nhu null rate, distinct count, min/max, distribution de hieu va phat hien bat thuong.

**Senior view:** Profiling nen chay dinh ky va luu history de detect drift. No giup thiet ke validation rules va debug upstream changes. Can sample/approximate voi bang lon de giam cost.

**Production example:** Cot `discount_pct` binh thuong 0-70%, hom nay max 900% thi co the source doi don vi tu fraction sang percent.

**Anti-pattern / trade-off:** Profile full table TB moi gio rat dat. Profile khong co threshold/action chi la report.

**Follow-up:** Cot nao nen profile? Drift threshold dat bang statistical method nao?

## 075. What is data optimization and its strategies?

**Ngan gon:** Data optimization cai thien speed, cost, reliability va usability cua storage/query/pipeline.

**Senior view:** Strategies gom partitioning, clustering/indexing, file compaction, compression, pruning columns, pre-aggregation, materialized views, caching, query rewrite, resource tuning va lifecycle management.

**Production example:** Spark job cham do 2 trieu small Parquet files; compact ve file 256MB, partition by date, giam runtime tu 90 phut xuong 15 phut.

**Anti-pattern / trade-off:** Optimize truoc khi co metrics de toi uu sai cho workload. Precompute qua nhieu mart tang storage va stale data.

**Follow-up:** Ban bat dau optimize tu dau? Cost vs latency trade-off ra sao?

