# Answers 001-025

## 001. What is data modeling and why is it important?

**Ngan gon:** Data modeling la cach thiet ke entities, relationships, constraints va grain truoc khi luu tru data. No quan trong vi giup team hieu cung mot ngon ngu business, tranh duplicate logic va tao nen tang cho query dung.

**Senior view:** Trong production, model tot phai tra loi duoc: fact co grain gi, dimension thay doi ra sao, primary/natural/surrogate key nao on dinh, va data contract nao duoc dam bao. Model sai thuong lam BI sai so, backfill kho, join cham va downstream phu thuoc vao cot khong on dinh.

**Production example:** Don hang e-commerce nen co `fact_order_line` o grain mot order item, khong gom tat ca vao mot bang order-level neu business can phan tich SKU, coupon, refund rieng.

**Anti-pattern / trade-off:** Over-normalize trong analytics lam query phuc tap; over-denormalize lam metric bi double count. Trade-off la giua data integrity, usability va performance.

**Follow-up:** Grain cua fact table la gi? Khi natural key thay doi thi xu ly the nao? Model nay support backfill khong?

## 002. Explain the difference between conceptual, logical, and physical data models.

**Ngan gon:** Conceptual model noi ve business concepts; logical model noi ve entities, attributes, relationships; physical model noi ve cach implement trong database/storage.

**Senior view:** Conceptual giup align stakeholder, logical giup chot semantic va constraints, physical giup toi uu engine cu the: data type, partition, clustering, index, file format. Mot senior khong nhay thang vao DDL khi chua ro business meaning.

**Production example:** Conceptual: Customer dat Order. Logical: `customer`, `order`, `order_line`, cardinality. Physical: BigQuery partition `order_date`, cluster `customer_id`, column type `NUMERIC(18,2)`.

**Anti-pattern / trade-off:** Dung physical schema lam "source of truth" cho business definition se gay semantic drift. Qua nhieu document nhung khong gan voi code/dbt tests thi nhanh loi thoi.

**Follow-up:** Ai approve logical model? Physical optimization co lam thay doi semantic khong?

## 003. What are the key steps in the data modeling process?

**Ngan gon:** Lay requirement, xac dinh entities va grain, thiet ke logical model, chon physical design, implement, test bang use case that, va maintain khi business doi.

**Senior view:** Buoc bi bo qua nhieu nhat la define metric semantics va edge cases: refund, cancellation, late-arriving data, multi-currency. Modeling nen co data profiling truoc, sample query sau, va governance cho schema evolution.

**Production example:** Truoc khi tao `daily_revenue`, can thong nhat revenue tinh theo payment captured hay order created, timezone nao, co tru refund khong.

**SQL example:**

```sql
select order_date, count(*) rows, count(distinct order_id) orders
from raw.orders
group by order_date;
```

**Anti-pattern / trade-off:** Design bang theo dashboard hien tai se vo khi dashboard doi. Design qua tong quat lam delivery cham.

**Follow-up:** Ban validate model voi business nhu the nao? Khi can them dimension moi thi migration ra sao?

## 004. Describe the different types of relationships in a relational database.

**Ngan gon:** Co 1:1, 1:N va M:N. M:N thuong can junction table de tranh luu list trong mot cot.

**Senior view:** Relationship khong chi la ERD; no anh huong referential integrity, join cardinality, dedup va metric correctness. Data warehouse doi khi khong enforce foreign key vat ly, nen can tests va constraints logic.

**Production example:** Customer 1:N Orders. Product M:N Campaign thong qua `campaign_product`. Neu join sai M:N voi fact sales co the nhan doi revenue.

**SQL example:**

```sql
select order_id, count(*) lines
from fact_order_line
group by order_id;
```

**Anti-pattern / trade-off:** Luu `product_ids = '1,2,3'` trong mot cot lam kho join, validate, index. Enforce FK trong OLTP tot, nhung trong warehouse lon co the ton chi phi load.

**Follow-up:** Lam sao phat hien join fan-out? Khi nao chap nhan denormalized array?

## 005. What is normalization and why is it used in database design?

**Ngan gon:** Normalization tach data thanh cac bang co phu thuoc ro rang de giam redundancy va tranh update anomaly.

**Senior view:** OLTP thuong normalize de dam bao consistency. Analytics thuong denormalize co kiem soat de tang query speed. Phong van tot la noi duoc khi nao nen normalize va khi nao nen deliberately denormalize.

**Production example:** Customer address trong OLTP nen tach de update mot noi. Trong mart report, co the snapshot address vao dimension SCD2 de giu lich su tai thoi diem mua hang.

**Anti-pattern / trade-off:** Ap dung 3NF may moc trong BI lam analyst phai join 12 bang. Denormalize khong co grain ro rang lam double count.

**Follow-up:** 1NF/2NF/3NF khac nhau the nao? Normalization co luon cai thien performance khong?

## 006. Explain the difference between OLTP and OLAP systems.

**Ngan gon:** OLTP phuc vu giao dich hien tai, ghi/transaction nhieu, latency thap. OLAP phuc vu phan tich, doc nhieu, query lon, data lich su.

**Senior view:** OLTP toi uu ACID, indexes cho lookup/update nho. OLAP toi uu scan, compression, columnar storage, partition, aggregate. Dung OLTP cho report nang se anh huong san pham chinh.

**Production example:** MySQL order service la OLTP. Snowflake/BigQuery/Redshift cho dashboard doanh thu la OLAP. Data di qua CDC hoac batch export.

**Anti-pattern / trade-off:** Query BI truc tiep production DB co the lock table, tang replica lag. Copy sang warehouse tang latency nhung cach ly workload.

**Follow-up:** Neu dashboard can near-real-time thi ban thiet ke gi? HTAP co phai luc nao cung tot?

## 007. What is a star schema and when would you use it?

**Ngan gon:** Star schema gom fact table o giua va cac dimension xung quanh. Dung cho analytics/reporting khi can query de hieu va performance tot.

**Senior view:** Diem quan trong nhat la fact grain. Dimension nen co attributes de filter/group, fact nen co measures additive/semi-additive/non-additive. Star schema tot giup metric layer on dinh.

**Production example:** `fact_sales_order_line` join `dim_date`, `dim_customer`, `dim_product`, `dim_store`. Analysts co the tinh revenue by category/month ma khong doc raw events.

**SQL example:**

```sql
select d.month, p.category, sum(f.net_amount) revenue
from fact_sales f
join dim_date d on f.date_key = d.date_key
join dim_product p on f.product_key = p.product_key
group by d.month, p.category;
```

**Anti-pattern / trade-off:** Dua text attribute vao fact qua nhieu lam bang phinh to. Snowflake dimension tiet kiem storage nhung tang join complexity.

**Follow-up:** Fact grain la gi? SCD2 dimension join voi fact bang key nao?

## 008. Describe the concept of slowly changing dimensions (SCDs) in data warehousing.

**Ngan gon:** SCD la cach quan ly dimension thay doi theo thoi gian. Type 1 overwrite, Type 2 tao version moi, Type 3 luu mot vai gia tri cu trong cot rieng.

**Senior view:** SCD2 can `effective_from`, `effective_to`, `is_current`, surrogate key va logic dong ban ghi cu. Thach thuc production la late arriving changes, duplicate source events, timezone va backfill.

**Production example:** Customer doi segment tu Silver sang Gold. Report doanh thu lich su thang truoc phai dung segment tai thoi diem giao dich, nen fact nen tham chieu customer surrogate key SCD2.

**Anti-pattern / trade-off:** Type 1 don gian nhung mat lich su. Type 2 dung lich su nhung tang row count va join phuc tap.

**Follow-up:** Xu ly update den tre nhu the nao? Lam sao dam bao chi co mot `is_current = true`?

## 009. What is a fact table and how does it differ from a dimension table?

**Ngan gon:** Fact table chua measurements/events o grain cu the; dimension table chua context de cat lat facts.

**Senior view:** Fact co additive measures nhu amount, quantity; dimension co attributes nhu customer segment, product category. Xac dinh sai grain fact la nguyen nhan lon cua duplicated metrics.

**Production example:** `fact_payment` co payment_id, amount, status, date_key. `dim_customer` co customer profile. Khong nen dat `customer_name` thay doi truc tiep vao fact neu can history.

**Anti-pattern / trade-off:** Mot bang "wide everything" de query nhanh ban dau nhung kho governance. Tach qua nhieu dimension nho lam BI kho dung.

**Follow-up:** Snapshot fact va transaction fact khac nhau the nao? Measure nao khong additive?

## 010. Explain the purpose of surrogate keys in data modeling.

**Ngan gon:** Surrogate key la key do he thong tao, khong mang y nghia business, dung de dinh danh row on dinh.

**Senior view:** Surrogate key dac biet huu ich cho SCD2 va khi natural key thay doi, bi recycle, hoac khac format giua source systems. Natural key van can unique test de mapping.

**Production example:** `customer_id` tu CRM va app co the khac nhau; warehouse tao `customer_key` de facts join on dinh voi dimension da resolve identity.

**Anti-pattern / trade-off:** Chi dung surrogate key ma khong luu natural key se kho trace ve source. Dung natural key lam FK trong SCD2 khong phan biet duoc version.

**Follow-up:** Surrogate key nen generated o dau? Khi merge dimension, lookup key that bai thi lam gi?

## 011. What is a data warehouse and its key characteristics?

**Ngan gon:** Data warehouse la kho du lieu phuc vu analytics, gom data tich hop tu nhieu source, co lich su, toi uu doc/query va bao cao.

**Senior view:** Warehouse production can separation layers: raw/staging, cleaned, curated marts. Can lineage, access control, data quality tests, cost governance va SLA freshness.

**Production example:** Cong ty SaaS dua data tu Postgres, Stripe, Salesforce vao warehouse de tinh ARR, churn, activation funnel.

**Anti-pattern / trade-off:** Dump raw data vao warehouse khong co model/ownership se thanh data swamp. Curated mart tang maintenance nhung tang trust va speed.

**Follow-up:** Warehouse khac lakehouse the nao? Ban thiet ke layer bronze/silver/gold ra sao?

## 012. Explain the ETL (Extract, Transform, Load) process and its stages.

**Ngan gon:** ETL gom extract data tu source, transform de clean/enrich/standardize, load vao target.

**Senior view:** Production ETL phai idempotent, retry duoc, co checkpoint, schema handling, data quality gate va observability. Transform khong chi clean data; no encode business rules.

**Production example:** Moi gio extract orders tu API, stage raw JSON, transform currency/timezone, dedup theo order_id + updated_at, merge vao warehouse.

**Python example:**

```python
df = raw.drop_duplicates(["order_id"]).assign(load_date=today)
```

**Anti-pattern / trade-off:** Load truc tiep vao mart khong co raw backup lam kho reprocess. ETL ngoai warehouse giam warehouse cost nhung tang infra complexity.

**Follow-up:** Pipeline co idempotent khong? Neu transform fail sau extract thi recover the nao?

## 013. What are the common challenges faced during ETL processes?

**Ngan gon:** Challenges gom data quality, schema drift, scale, retries, late data, security, lineage, monitoring va source system limits.

**Senior view:** Van de thuc te thuong khong nam o code transform ma o operational behavior: API rate limit, partial load, duplicate messages, timezone, source backfill, PII leakage. Can design failure isolation.

**Production example:** CRM API thay field `company_size` tu number sang string lam load fail. Pipeline tot se detect schema change, quarantine records, alert owner.

**Anti-pattern / trade-off:** Catch exception va continue im lang lam dashboard sai. Fail-fast bao ve quality nhung co the anh huong SLA neu rule qua chat.

**Follow-up:** Ban monitor nhung metric nao? Khi source gui duplicate 5% thi xu ly sao?

## 014. Describe the difference between full load and incremental load in ETL.

**Ngan gon:** Full load reload toan bo dataset. Incremental load chi load record moi/thay doi dua tren watermark, CDC hoac updated timestamp.

**Senior view:** Full load don gian va tot cho bang nho/reference. Incremental can chuan hoa watermark, handle deletes, late updates, clock skew va reprocessing. Merge logic phai idempotent.

**Production example:** Product categories 5k rows co the full reload hang ngay. Orders 2 ty rows phai incremental qua `updated_at` hoac CDC log.

**SQL example:**

```sql
merge into dim_product t
using staging_product s
on t.product_id = s.product_id
when matched then update set name = s.name
when not matched then insert (product_id, name) values (s.product_id, s.name);
```

**Anti-pattern / trade-off:** Tin `updated_at` neu source khong update khi delete. Full reload bang lon ton cost nhung de reconcile.

**Follow-up:** Ban luu watermark o dau? Xu ly hard delete the nao?

## 015. What is data staging and why is it important in ETL?

**Ngan gon:** Staging la lop trung gian luu raw/near-raw data truoc khi transform vao target.

**Senior view:** Staging giup audit, replay, debug, dedup va tach extract khoi transform. Trong production, staging nen co partition by load time, metadata source file/batch id va retention ro rang.

**Production example:** Load file daily tu SFTP vao `stg_bank_transactions` truoc, validate row count/hash, sau do moi merge vao fact.

**Anti-pattern / trade-off:** Khong co staging thi fail giua pipeline kho biet du lieu nao da vao. Giu staging qua lau tang storage va PII risk.

**Follow-up:** Staging co overwrite hay append? Ban dat retention va access control the nao?

## 016. Explain the concept of data lineage and its significance in data warehousing.

**Ngan gon:** Data lineage cho biet data di tu dau, qua transformation nao, den bang/report nao.

**Senior view:** Lineage giup impact analysis, audit, root cause va compliance. Senior DE can lineage o table/column/job level, gan voi owner, SLA va version code.

**Production example:** Neu KPI `gross_margin` sai, lineage cho thay no lay tu `fact_orders`, `dim_product_cost`, transform dbt model nao va job run luc nao.

**Anti-pattern / trade-off:** Lineage ve bang anh dep nhung khong gan voi runtime metadata se it gia tri. Column-level lineage huu ich nhung kho maintain voi dynamic SQL.

**Follow-up:** Ban capture lineage tu Airflow/dbt/Spark nhu the nao? Lineage giup incident response ra sao?

## 017. What are the benefits of using a data warehouse?

**Ngan gon:** Warehouse gom nhieu source vao mot noi dang tin, co lich su va toi uu cho analytics/reporting.

**Senior view:** Loi ich lon nhat la semantic consistency: finance, product va sales dung cung metric definition. Ngoai ra warehouse cach ly workload analytics khoi OLTP, ho tro access control, lineage va governance.

**Production example:** Thay vi moi team tu query production DB, warehouse cung cap `mart_revenue`, `mart_customer_health`, `mart_inventory` co tests va owner.

**Anti-pattern / trade-off:** Warehouse khong tu dong tao trust; neu ingestion kem va khong co data contract thi no chi tap trung loi. Chi phi compute co the tang neu query tu do khong guardrail.

**Follow-up:** Ban do ROI warehouse bang gi? Lam sao tranh warehouse thanh dumping ground?

## 018. Describe the role of data quality in ETL processes.

**Ngan gon:** Data quality dam bao data sau ETL dung, day du, nhat quan, kip thoi va co the tin dung.

**Senior view:** Quality nen la gate trong pipeline, khong phai buoc manual cuoi cung. Tests gom schema, null, uniqueness, referential integrity, accepted values, freshness va anomaly.

**Production example:** Neu payment amount am bat thuong hoac row count giam 80%, pipeline nen fail/quarantine va alert truoc khi cap nhat executive dashboard.

**SQL example:**

```sql
select count(*) bad_rows
from fact_payment
where amount < 0 or payment_id is null;
```

**Anti-pattern / trade-off:** Qua nhieu test blocking lam pipeline hay fail vi false positive. Qua it test lam sai so di vao report.

**Follow-up:** Test nao blocking, test nao warning? Data quality owner la ai?

## 019. What is a slowly changing dimension (SCD) and how is it handled in ETL?

**Ngan gon:** SCD xu ly dimension thay doi cham theo thoi gian. ETL can quyet dinh overwrite, versioning hay luu mot phan lich su.

**Senior view:** SCD2 ETL thuong compare hash attributes, expire current row, insert row moi voi surrogate key moi. Can transaction/atomic merge de tranh hai current rows.

**Production example:** Supplier risk tier thay doi. Bao cao procurement lich su can biet tai ngay mua hang supplier thuoc tier nao.

**Anti-pattern / trade-off:** Hash all columns ke ca metadata load time se tao version gia. Bo qua deletes lam current row sai.

**Follow-up:** Ban xu ly late arriving dimension truoc fact the nao? SCD Type 6 la gi?

## 020. Explain the difference between a data warehouse and a data mart.

**Ngan gon:** Warehouse la kho du lieu toan doanh nghiep; data mart la phan con phuc vu mot domain/team nhu finance, sales, marketing.

**Senior view:** Mart nen duoc build tu curated warehouse/lakehouse layer de dam bao metric consistent. Independent mart nhanh luc dau nhung de tao silo va conflict definition.

**Production example:** `enterprise_warehouse` chua canonical customers/orders. `finance_mart` tinh revenue recognition; `growth_mart` tinh funnel conversion.

**Anti-pattern / trade-off:** Mart rieng tu source truc tiep giup delivery nhanh nhung tao reconciliation pain. Central warehouse chuan hoa tot nhung co the thanh bottleneck neu governance qua nang.

**Follow-up:** Ban cho team tu tao mart khong? Metric shared nam o dau?

## 021. What is Hadoop and its core components?

**Ngan gon:** Hadoop la ecosystem xu ly va luu tru du lieu phan tan, cot loi gom HDFS, YARN va MapReduce.

**Senior view:** Hadoop phu hop batch workload lon tren cluster commodity. Ngay nay nhieu he thong dung object storage + Spark/serverless thay Hadoop classic, nhung concepts ve distributed storage, replication va compute scheduling van quan trong.

**Production example:** Log clickstream hang TB/ngay duoc luu HDFS, xu ly batch nightly bang Spark/Hive de tao aggregates.

**Anti-pattern / trade-off:** Tu van hanh Hadoop cluster nho co the ton ops hon gia tri. HDFS tot cho throughput lon, khong tot cho nhieu file nho.

**Follow-up:** HDFS block replication hoat dong the nao? YARN khac Kubernetes cho data jobs ra sao?

## 022. Explain the difference between Hadoop and Spark.

**Ngan gon:** Hadoop la ecosystem gom storage va batch compute MapReduce; Spark la engine xu ly phan tan nhanh hon, ho tro in-memory, SQL, streaming, ML.

**Senior view:** Spark co the doc HDFS/S3/ADLS va thay MapReduce cho nhieu workload. Spark nhanh nhung can tuning shuffle, memory, partition va file size. Hadoop khong dong nghia voi MapReduce duy nhat.

**Production example:** Pipeline cu MapReduce 6 gio co the migrate sang Spark SQL 45 phut neu optimize partition va avoid skew.

**Anti-pattern / trade-off:** Dung Spark cho job nho co overhead lon. MapReduce cham nhung fault-tolerant don gian cho batch rat lon.

**Follow-up:** Spark lazy evaluation la gi? Khi nao MapReduce van chap nhan duoc?

## 023. What is MapReduce and how does it work?

**Ngan gon:** MapReduce chia job thanh map phase xu ly record thanh key-value, shuffle group theo key, reduce phase tong hop ket qua.

**Senior view:** MapReduce scale tot vi data locality va fault tolerance, nhung lap trinh verbose va moi stage ghi doc disk nen cham cho iterative workload. Concept shuffle van cuc ky quan trong trong Spark/Flink.

**Production example:** Dem page views theo URL: map emit `(url, 1)`, reduce sum theo url.

**Anti-pattern / trade-off:** Key skew lam reducer duy nhat bi qua tai. Combiner co the giam network IO neu operation associative/commutative.

**Follow-up:** Shuffle ton chi phi o dau? Lam sao xu ly hot key?

## 024. Describe the role of HDFS in Hadoop.

**Ngan gon:** HDFS la distributed file system cua Hadoop, chia file thanh blocks va replicate tren nhieu nodes de tang fault tolerance.

**Senior view:** HDFS toi uu sequential read/write throughput cho file lon. No khong phu hop low-latency random updates. NameNode la metadata control plane can duoc bao ve va monitor.

**Production example:** File log 1GB duoc chia block 128MB/256MB, replicate factor 3. Neu mot DataNode chet, cluster van doc duoc block tu replica khac.

**Anti-pattern / trade-off:** Nhieu file nho lam NameNode metadata pressure. Replication tang durability nhung ton storage.

**Follow-up:** Small files problem xu ly ra sao? HDFS khac object storage nhu S3 the nao?

## 025. What is Hive and how is it used in big data processing?

**Ngan gon:** Hive cung cap SQL layer tren du lieu lon trong HDFS/object storage, dung metadata catalog va query engine de xu ly batch analytics.

**Senior view:** Hive huu ich cho data warehouse tren Hadoop: schema-on-read, partitioned tables, external tables. Hien nay Hive Metastore van pho bien lam catalog cho Spark/Presto/Trino.

**Production example:** Raw logs luu Parquet partition theo `dt`, dang ky table Hive de analyst query bang SQL thay vi viet MapReduce.

**SQL example:**

```sql
create external table web_events (user_id string, event string)
partitioned by (dt string)
stored as parquet
location 's3://lake/web_events/';
```

**Anti-pattern / trade-off:** Partition qua nhieu cardinality cao tao qua nhieu folder/file. Schema-on-read linh hoat nhung loi chi lo khi query.

**Follow-up:** Managed vs external table khac nhau the nao? Hive Metastore dung trong lakehouse ra sao?

