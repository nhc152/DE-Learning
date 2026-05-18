Được, đây là toàn bộ danh sách câu hỏi theo từng chủ đề:

---

## 🏗 1. Kiến trúc (Architecture)

1. Sự khác biệt Oracle vs PostgreSQL về kiến trúc tổng thể?
2. SGA, PGA trong Oracle là gì? Cấu hình như thế nào?
3. WAL (Write-Ahead Log) trong PostgreSQL hoạt động ra sao?
4. Schema, Tablespace, Datafile trong Oracle khác gì PostgreSQL?
5. Oracle RAC là gì? Khi nào dùng?
6. Shared Buffers, Work Mem trong PostgreSQL dùng để làm gì?

---

## 📝 2. SQL & Query

7. Phân biệt INNER JOIN, LEFT JOIN, FULL OUTER JOIN — cho ví dụ thực tế
8. Window Functions là gì? ROW_NUMBER vs RANK vs DENSE_RANK?
9. CTE (WITH clause) vs Subquery — khi nào dùng cái nào?
10. MERGE statement trong Oracle dùng như thế nào?
11. UPSERT trong PostgreSQL (INSERT ON CONFLICT)?
12. Phân biệt UNION vs UNION ALL — performance khác nhau ra sao?
13. Explain Plan / EXPLAIN ANALYZE — đọc kết quả như thế nào?

---

## ⚡ 3. Performance Tuning

14. Index là gì? B-Tree Index vs Bitmap Index vs Function-Based Index?
15. Khi nào index không được dùng (index skip)?
16. Partition Table là gì? Range, List, Hash Partition?
17. Oracle Parallel Query — PARALLEL hint dùng khi nào?
18. PostgreSQL VACUUM và AUTOVACUUM — tại sao quan trọng?
19. Slow query xử lý như thế nào? Quy trình troubleshoot?
20. Statistics trong Oracle (DBMS_STATS) và PostgreSQL (ANALYZE)?

---

## 🔒 4. Transaction & Concurrency

21. ACID là gì? Giải thích từng thành phần?
22. Các mức Isolation Level — READ COMMITTED, SERIALIZABLE?
23. Deadlock là gì? Xử lý thế nào trong Oracle/PostgreSQL?
24. MVCC (Multi-Version Concurrency Control) hoạt động ra sao?
25. Oracle Undo vs PostgreSQL MVCC — khác nhau điểm gì?
26. Lock types trong Oracle — Row Lock, Table Lock, Deadlock?

---

## 💾 5. Backup & High Availability

27. Oracle RMAN backup là gì? Full vs Incremental?
28. PostgreSQL pg_dump vs pg_basebackup — dùng khi nào?
29. Oracle DataGuard hoạt động như thế nào?
30. PostgreSQL Streaming Replication — Primary/Standby setup?
31. RPO và RTO là gì? Liên quan gì đến backup strategy?
32. Point-in-Time Recovery (PITR) trong PostgreSQL?

---

## 🔶 6. Oracle Specific

33. PL/SQL Stored Procedure vs Function vs Package?
34. Oracle Sequence — dùng thế nào trong ETL?
35. Oracle Hint — APPEND, PARALLEL, NO_INDEX dùng khi nào?
36. Oracle Flashback — Flashback Query, Flashback Table?
37. Oracle Scheduler (DBMS_SCHEDULER) vs cron?
38. Materialized View trong Oracle — refresh FAST vs COMPLETE?

---

## 🐘 7. PostgreSQL Specific

39. PostgreSQL Extension là gì? pg_stat_statements, pgcrypto?
40. JSONB trong PostgreSQL — khi nào dùng thay relational?
41. PostgreSQL Inheritance và Partition Table?
42. pg_stat_activity — monitor active queries như thế nào?
43. PostgreSQL Role vs User — phân quyền như thế nào?
44. Foreign Data Wrapper (FDW) là gì?

---

## 🏦 8. Thực chiến Banking/ETL

45. Thiết kế bảng transaction cho hệ thống banking — lưu ý gì?
46. ETL pipeline của bạn xử lý data lớn thế nào? (Oracle/Talend/ODI)
47. Truncate & Load vs Delete & Insert — khi nào dùng cái nào?
48. Xử lý duplicate data trong ETL như thế nào?
49. Audit logging trong database banking — thiết kế ra sao?
50. Data masking — bạn đã làm với DBMS_CRYPTO như thế nào?

---
## 📊 9. Monitoring & Grafana
Oracle Monitoring:
51. Làm thế nào để monitor Oracle DB performance? Các metric quan trọng?
52. V$ views quan trọng cần biết: VSESSION,VSESSION, V
SESSION,VSQL, V$WAIT_CLASS?
53. AWR Report là gì? Đọc AWR như thế nào?
54. ASH (Active Session History) dùng để làm gì?
55. Oracle Alert Log — monitor lỗi như thế nào?
PostgreSQL Monitoring:
56. pg_stat_activity — query nào đang chạy, block nhau không?
57. pg_stat_bgwriter — hiểu checkpoint performance?
58. pg_locks — detect deadlock và blocking query?
59. pg_stat_user_tables — bloat, dead tuples, last vacuum?
60. long-running query — phát hiện và kill như thế nào?
Prometheus + Grafana:
61. Prometheus scrape metric từ DB như thế nào? (oracle_exporter, postgres_exporter)
62. Các metric DB quan trọng cần dashboard trong Grafana?
63. Alerting rule trong Grafana — ví dụ alert khi connection pool đầy?
64. Grafana dashboard cho Oracle: active sessions, wait events, buffer hit ratio?
65. Grafana dashboard cho PostgreSQL: TPS, cache hit ratio, replication lag?

---

 🔍 10. Database trong môi trường Dynatrace/APM
DB Monitoring qua APM tool:

66. Dynatrace monitor database như thế nào? OneAgent detect DB connection ra sao?
67. Slow query trong Dynatrace — Davis AI phân tích bottleneck DB thế nào?
68. Database response time baseline — bạn set threshold alert như thế nào?
69. Phân biệt DB-side monitoring (AWR, pg_stat) vs APM-side monitoring (Dynatrace)?

---

## ☁️ 11. Database trên Cloud & Container
Cloud DB:

70. Oracle DB trên AWS RDS khác gì on-premise Oracle?
71. PostgreSQL trên AWS RDS / Azure Database — managed service khác gì tự host?
72. Connection pooling trong môi trường cloud — PgBouncer, HikariCP?

Containerized DB:

73. Chạy PostgreSQL trong Docker/Kubernetes — persistent volume cần lưu ý gì?
74. StatefulSet trong Kubernetes cho DB — khác gì Deployment?
75. DB trong microservices — mỗi service 1 DB (Database per Service pattern)?

---

## 🔗 12. Database trong CI/CD & DevOps

76. Database migration trong CI/CD pipeline — Flyway, Liquibase là gì?
77. Schema versioning — quản lý DDL change như thế nào trong team?
78. Blue/Green deployment có ảnh hưởng gì đến DB schema?
79. Database rollback strategy khi deploy fail?

---

## 🏗 13. Distributed & Microservices DB

80. CAP Theorem là gì? Liên quan gì đến chọn DB?
81. Distributed transaction — 2PC (Two-Phase Commit) vs SAGA pattern?
82. Database sharding là gì? Khi nào áp dụng trong banking?
83. Event Sourcing và CQRS — liên quan gì đến DB design?

---