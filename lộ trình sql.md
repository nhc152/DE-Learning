Senior Data Engineer cần biết SQL theo 3 tầng: **viết đúng**, **viết nhanh**, và **thiết kế được hệ thống dữ liệu chạy ổn ở quy mô lớn**.

**1. Nền tảng SQL bắt buộc**

Cần rất chắc các phần cơ bản:

- `SELECT`, `WHERE`, `ORDER BY`
- `GROUP BY`, `HAVING`
- `JOIN`: `INNER`, `LEFT`, `RIGHT`, `FULL`, `CROSS`
- `UNION`, `UNION ALL`, `INTERSECT`, `MINUS/EXCEPT`
- `CASE WHEN`
- `NULL` handling
- `DISTINCT`
- Subquery
- CTE: `WITH`
- Aggregate functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- Date/time functions
- String functions
- Numeric functions

Ví dụ cần hiểu rõ khác biệt:

```sql
WHERE status <> 'CANCELLED'
```

không tự động lấy dòng có `status IS NULL`.

Nếu muốn lấy cả `NULL`:

```sql
WHERE status <> 'CANCELLED'
   OR status IS NULL;
```

**2. JOIN và quan hệ dữ liệu**

Senior Data Engineer phải rất mạnh phần join, vì lỗi join là nguyên nhân phổ biến gây sai dữ liệu.

Cần biết:

- Join 1-1, 1-n, n-n
- Duplicate rows sau join
- Missing rows do dùng sai `INNER JOIN`
- Khi nào dùng `LEFT JOIN`
- Semi join: `EXISTS`
- Anti join: `NOT EXISTS`
- Cartesian product
- Join key không unique
- Join trên nhiều cột
- Join với dữ liệu bị thiếu hoặc `NULL`

Ví dụ lỗi thường gặp:

```sql
SELECT *
FROM orders o
JOIN order_items i
  ON o.order_id = i.order_id;
```

Nếu một order có 5 items, dòng order sẽ bị nhân 5 lần. Nếu sau đó `SUM(o.total_amount)` thì kết quả sai.

**3. Aggregation và phân tích dữ liệu**

Cần thành thạo:

- `GROUP BY`
- `HAVING`
- Aggregate theo nhiều chiều
- Conditional aggregation
- `COUNT(*)` vs `COUNT(column)`
- `COUNT(DISTINCT column)`
- Tính tỷ lệ, phần trăm
- Rollup/cube/grouping sets nếu database hỗ trợ

Ví dụ conditional aggregation:

```sql
SELECT
  customer_id,
  COUNT(*) AS total_orders,
  SUM(CASE WHEN status = 'PAID' THEN 1 ELSE 0 END) AS paid_orders,
  SUM(CASE WHEN status = 'CANCELLED' THEN 1 ELSE 0 END) AS cancelled_orders
FROM orders
GROUP BY customer_id;
```

**4. Window Functions**

Đây là phần rất quan trọng với Data Engineer.

Cần biết:

- `ROW_NUMBER`
- `RANK`
- `DENSE_RANK`
- `LAG`
- `LEAD`
- `SUM() OVER`
- `AVG() OVER`
- `COUNT() OVER`
- Running total
- Moving average
- Deduplication
- Top N per group
- First/last event per user
- Sessionization cơ bản

Ví dụ lấy bản ghi mới nhất mỗi user:

```sql
WITH ranked AS (
  SELECT
    user_id,
    event_time,
    event_name,
    ROW_NUMBER() OVER (
      PARTITION BY user_id
      ORDER BY event_time DESC
    ) AS rn
  FROM events
)
SELECT *
FROM ranked
WHERE rn = 1;
```

**5. Data Modeling bằng SQL**

Senior Data Engineer cần biết SQL không chỉ để query, mà còn để thiết kế dữ liệu.

Cần hiểu:

- OLTP vs OLAP
- Normalization
- Denormalization
- Star schema
- Snowflake schema
- Fact table
- Dimension table
- Grain của bảng
- Surrogate key
- Natural key
- Slowly Changing Dimension: SCD Type 1, Type 2
- Snapshot table
- Bridge table
- Aggregate table

Câu hỏi quan trọng nhất khi thiết kế bảng fact:

```text
Mỗi dòng trong bảng này đại diện cho điều gì?
```

Đó là “grain” của bảng.

Ví dụ:

```text
fact_order_items
Grain: mỗi dòng là một sản phẩm trong một đơn hàng.
```

**6. SQL cho ETL/ELT**

Cần biết viết SQL phục vụ pipeline:

- Insert từ staging sang target
- Incremental load
- Full refresh
- Upsert/Merge
- Dedup dữ liệu
- Validate dữ liệu
- Backfill dữ liệu
- Late arriving data
- Idempotent SQL
- Audit columns: `created_at`, `updated_at`, `batch_id`
- Soft delete
- CDC: Change Data Capture

Ví dụ `MERGE`:

```sql
MERGE INTO dim_customer t
USING stg_customer s
ON (t.customer_id = s.customer_id)
WHEN MATCHED THEN
  UPDATE SET
    t.full_name = s.full_name,
    t.email = s.email,
    t.updated_at = CURRENT_TIMESTAMP
WHEN NOT MATCHED THEN
  INSERT (customer_id, full_name, email, created_at)
  VALUES (s.customer_id, s.full_name, s.email, CURRENT_TIMESTAMP);
```

**7. SQL Performance Tuning**

Senior cần biết đọc query chậm và tối ưu.

Cần nắm:

- Execution plan
- Index scan vs full table scan
- Predicate pushdown
- Partition pruning
- Join strategy
- Sort/hash cost
- Statistics
- Cardinality estimation
- Data skew
- Query rewrite
- Avoid unnecessary `DISTINCT`
- Avoid unnecessary CTE materialization nếu database có hành vi đó
- Filter sớm
- Chỉ chọn cột cần dùng
- Tránh function trên indexed column
- Tránh implicit type conversion

Ví dụ không tốt:

```sql
WHERE DATE(created_at) = '2026-05-08'
```

Tốt hơn:

```sql
WHERE created_at >= TIMESTAMP '2026-05-08 00:00:00'
  AND created_at <  TIMESTAMP '2026-05-09 00:00:00'
```

**8. Partitioning và dữ liệu lớn**

Cần hiểu:

- Partition theo ngày/tháng
- Partition pruning
- Cluster/sort key
- Bucketing
- Sharding cơ bản
- Table statistics
- File size trong data lake
- Small files problem
- Compaction
- Z-order / clustering nếu dùng Databricks, Delta, Snowflake, BigQuery tương ứng

Ví dụ query tận dụng partition:

```sql
SELECT *
FROM fact_events
WHERE event_date = DATE '2026-05-08';
```

Nếu bảng partition theo `event_date`, query này chỉ đọc partition cần thiết.

**9. Transaction và Consistency**

Cần biết:

- `COMMIT`
- `ROLLBACK`
- Isolation level
- Read committed
- Repeatable read
- Serializable
- Lock
- Deadlock
- Dirty read
- Non-repeatable read
- Phantom read
- MVCC
- Idempotency trong pipeline

Data Engineer không nhất thiết phải như DBA, nhưng phải hiểu đủ để tránh pipeline gây lock hoặc ghi dữ liệu sai.

**10. Data Quality bằng SQL**

Cần viết được SQL kiểm tra chất lượng dữ liệu:

- Duplicate check
- Null check
- Referential integrity check
- Range check
- Freshness check
- Reconciliation
- Row count check
- Sum check
- Anomaly check
- Schema drift check

Ví dụ kiểm tra duplicate:

```sql
SELECT customer_id, COUNT(*) AS cnt
FROM dim_customer
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

Kiểm tra fact không có dimension tương ứng:

```sql
SELECT f.customer_id, COUNT(*) AS cnt
FROM fact_orders f
LEFT JOIN dim_customer d
  ON f.customer_id = d.customer_id
WHERE d.customer_id IS NULL
GROUP BY f.customer_id;
```

**11. SQL cho Analytical Use Cases**

Cần biết xử lý các bài toán phân tích phổ biến:

- Funnel analysis
- Retention analysis
- Cohort analysis
- Churn analysis
- Revenue metrics
- DAU, WAU, MAU
- Conversion rate
- Rolling metrics
- Ranking
- Attribution cơ bản
- Sessionization

Ví dụ rolling 7 days:

```sql
SELECT
  event_date,
  daily_users,
  SUM(daily_users) OVER (
    ORDER BY event_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS rolling_7d_users
FROM daily_active_users;
```

**12. SQL Dialects**

Senior nên biết SQL có nhiều biến thể:

- Oracle SQL
- PostgreSQL
- MySQL
- SQL Server
- BigQuery SQL
- Snowflake SQL
- Spark SQL
- Hive SQL
- Presto/Trino SQL

Cần biết khác biệt ở:

- Date functions
- String functions
- Window functions
- `MERGE`
- `QUALIFY`
- `LIMIT` vs `FETCH FIRST`
- Array/JSON functions
- Semi-structured data
- Temporary table
- CTE behavior
- Transaction support

**13. Semi-Structured Data**

Data Engineer hiện đại cần biết query:

- JSON
- ARRAY
- STRUCT
- MAP
- Nested data
- Flatten/un-nest

Ví dụ kiểu BigQuery:

```sql
SELECT
  user_id,
  item.item_id,
  item.quantity
FROM orders,
UNNEST(items) AS item;
```

Hoặc kiểu Oracle JSON:

```sql
SELECT jt.item_id, jt.quantity
FROM orders o,
JSON_TABLE(
  o.payload,
  '$.items[*]'
  COLUMNS (
    item_id  VARCHAR2(50) PATH '$.item_id',
    quantity NUMBER       PATH '$.quantity'
  )
) jt;
```

**14. Security và Governance**

Cần hiểu:

- Role, privilege
- Grant/revoke
- Row-level security
- Column masking
- PII data
- Encryption
- Audit log
- Least privilege
- Data retention
- GDPR/CCPA nếu làm với thị trường liên quan

Ví dụ không nên cấp quyền quá rộng:

```sql
GRANT SELECT ON customer_pii TO analyst_role;
```

nếu analyst chỉ cần dữ liệu đã masking hoặc aggregate.

**15. Khả năng debug dữ liệu**

Senior Data Engineer phải debug được câu hỏi kiểu:

```text
Vì sao số revenue hôm nay giảm 30%?
Vì sao dashboard lệch với source system?
Vì sao số dòng tăng gấp đôi?
Vì sao pipeline chạy chậm?
```

Cần biết dùng SQL để:

- So sánh source vs target
- Truy dấu từng bước pipeline
- Kiểm tra duplicate
- Kiểm tra missing data
- Kiểm tra logic join
- Kiểm tra thay đổi schema
- Kiểm tra late data
- Kiểm tra timezone

**16. Những lỗi SQL senior phải tránh**

- `SELECT *` trong pipeline production.
- Join không kiểm tra cardinality.
- Dùng `DISTINCT` để che lỗi duplicate.
- Không xác định grain của bảng.
- Dùng `INNER JOIN` làm mất dữ liệu ngoài ý muốn.
- So sánh date/timestamp sai timezone.
- Query không có filter partition.
- Pipeline không idempotent.
- Dùng `COUNT(column)` khi cần `COUNT(*)`.
- Không test dữ liệu null.
- Không kiểm tra duplicate key trước khi merge.
- Tạo index hoặc partition theo cảm tính.
- Tối ưu query mà không xem execution plan.

**17. Lộ trình học SQL cho Senior Data Engineer**

Thứ tự nên học:

1. SQL fundamentals thật chắc.
2. Join và aggregation.
3. Window functions.
4. CTE, subquery, query decomposition.
5. Data modeling: fact/dimension/star schema.
6. ETL/ELT SQL patterns.
7. Performance tuning.
8. Partitioning và large-scale SQL.
9. Data quality checks.
10. Analytical SQL patterns.
11. SQL dialects trên platform đang dùng.
12. Governance, security, lineage.

Tóm lại, senior data engineer không chỉ cần viết được SQL. Cần viết SQL **đúng dữ liệu, chạy hiệu quả, dễ bảo trì, phù hợp mô hình dữ liệu, và đủ an toàn để chạy trong pipeline production**.