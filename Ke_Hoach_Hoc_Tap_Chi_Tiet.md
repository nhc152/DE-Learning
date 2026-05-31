# Kế Hoạch Học Tập Data Engineering Chi Tiết (Thực Chiến 2026)

Kế hoạch này được thiết kế để bạn bắt đầu từ con số 0 (đã có nền tảng SQL/ETL cơ bản) tiến dần lên cấp độ **Senior-ready Data Engineer** trong vòng **24 - 28 tuần** (~6 tháng).

---

## 🧭 Bắt Đầu Từ Đâu? (Tuần 0: Setup Môi Trường)

Trước khi đọc bất kỳ dòng lý thuyết nào, bạn phải hoàn tất việc thiết lập "bàn làm việc" của mình.

### 📅 Lịch trình Tuần 0:
*   **Ngày 1 - 2: Cài đặt công cụ nền tảng**
    *   Cài đặt **Docker Desktop** (hoặc Docker Engine nếu dùng Linux/WSL2).
    *   Cài đặt **Python 3.11+** và tạo môi trường ảo (`venv` hoặc `conda`).
    *   Cài đặt **VS Code** và các extension quan trọng: *Python, SQLTools, Docker, GitLens, Jupyter*.
*   **Ngày 3 - 4: Setup Database & Git**
    *   Khởi chạy PostgreSQL container bằng Docker Compose.
    *   Tạo tài khoản GitHub và khởi tạo repository cá nhân tên là `de-roadmap-artifacts` để lưu toàn bộ bài tập sau này.
*   **Ngày 5 - 6: Spark local**
    *   Cài đặt Spark local và chạy thử 1 file notebook đơn giản để kiểm tra môi trường.
*   **Tài liệu đọc:** Mở trực tiếp [Week00_Setup.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week00_Setup.html) bằng trình duyệt.
*   **Exit Criteria (Tiêu chí qua môn):** Chụp ảnh màn hình terminal chạy lệnh `docker ps` có Postgres đang chạy + chạy thành công 1 câu lệnh SQL và 1 dòng lệnh Spark trên notebook. Commit ảnh này lên repo `de-roadmap-artifacts`.

---

## 📈 GIAI ĐOẠN 1: Nền Tảng Cốt Lõi (Tuần 1 – 4)
*Mục tiêu: Thành thạo SQL nâng cao, Python ETL tự viết, và tư duy thiết kế luồng dữ liệu.*

### 📚 Tuần 1: SQL Nâng Cao cho Data Engineer
*   **Tài liệu học:** [Week01_SQL_Advanced.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week01_SQL_Advanced.html) & [lộ trình sql.md](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/l%E1%BB%99%20tr%C3%ACnh%20sql.md)
*   **Lý thuyết cốt lõi:**
    *   Window functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `SUM() OVER`).
    *   Phân biệt Window Frame (`ROWS BETWEEN` vs `RANGE BETWEEN`).
    *   Recursive CTEs để duyệt dữ liệu dạng phân cấp (Hierarchy).
    *   `GROUPING SETS`, `ROLLUP`, `CUBE` để tổng hợp dữ liệu đa chiều.
    *   Đọc Execution Plan (`EXPLAIN ANALYZE`), hiểu cơ chế Index (B-Tree).
*   **Bài tập thực hành (Artifact):** Tạo file `week1_sql_advanced.sql` gồm:
    *   5 câu truy vấn phân tích thực tế (doanh thu luỹ tiến, xếp hạng sản phẩm, tính tỉ lệ retention).
    *   1 câu recursive CTE để phân tích cấu trúc tổ chức hoặc sơ đồ cây.
    *   Tối ưu hóa 1 query chạy chậm bằng cách thêm Index và chụp lại Execution Plan trước/sau.
*   **Exit Criteria:** Giải quyết được các bài toán Window Function cấp độ Hard trên DataLemur hoặc StrataScratch.

### 📚 Tuần 2: Python cho Data Engineering
*   **Tài liệu học:** [Week02_Python_DE.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week02_Python_DE.html)
*   **Lý thuyết cốt lõi:**
    *   Sử dụng thư viện `pandas` để xử lý tệp tin (CSV, Parquet, JSON).
    *   Kết nối database bằng `sqlalchemy` và `psycopg2`.
    *   Tương tác API bằng thư viện `requests` (xử lý phân trang - Pagination, Rate limit).
    *   Xây dựng hệ thống ghi log (`logging`) chuẩn chỉnh và cơ chế thử lại (`retry pattern`).
    *   Tư duy Module hóa code (tách biệt các hàm `extract`, `transform`, `load`).
*   **Bài tập thực hành (Artifact):** Tạo thư mục `week2_python_etl/` chứa:
    *   `extract.py`: Kéo dữ liệu từ 1 API công khai và đọc 1 file CSV.
    *   `transform.py`: Chuẩn hóa dữ liệu, định dạng ngày tháng, xử lý null.
    *   `load.py`: Ghi dữ liệu vào PostgreSQL dưới dạng Incremental Load (chỉ ghi dữ liệu mới).
    *   `pipeline.py`: File điều phối chạy toàn bộ luồng trên.
*   **Exit Criteria:** Pipeline chạy tự động qua command line, sinh log ra file `pipeline.log` và không bị trùng lặp dữ liệu khi chạy lại nhiều lần.

### 📚 Tuần 3: Làm Sạch Dữ Liệu & Khai Thác AI
*   **Tài liệu học:** [Week03_Data_Cleaning_Claude.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week03_Data_Cleaning_Claude.html) & [Huong-dan-su-dung-Claude-AI-hieu-qua.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Huong-dan-su-dung-Claude-AI-hieu-qua.html)
*   **Lý thuyết cốt lõi:**
    *   Nhận diện dữ liệu bẩn (missing values, duplicates, outliers, wrong format).
    *   Chiến lược tiền xử lý và làm sạch.
    *   Defensive Programming: Sử dụng thư viện `pandera` để validate schema của dữ liệu đầu vào.
    *   Prompt Engineering cho DE: Dùng AI viết regex phức tạp, tạo dữ liệu giả (mock data), review logic code.
*   **Bài tập thực hành (Artifact):** Tạo thư mục `week3_data_cleaning/` chứa:
    *   `validation_rules.py`: Định nghĩa schema kiểm tra dữ liệu bằng `pandera`.
    *   `cleaning_pipeline.py`: Code làm sạch dữ liệu tự động.
    *   `profiling_report.ipynb`: Phân tích chất lượng của 1 dataset bẩn trước và sau khi làm sạch.
*   **Exit Criteria:** Dữ liệu đầu vào sai schema bị từ chối ngay lập tức và ghi vào thư mục lỗi (Dead Letter Queue), dữ liệu đúng được ghi vào database.

### 📚 Tuần 4: Tư Duy Thiết Kế Pipeline
*   **Tài liệu học:** [Week04_Pipeline_Design.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week04_Pipeline_Design.html)
*   **Lý thuyết cốt lõi:**
    *   Khái niệm đồ thị tuần hoàn có hướng (DAG - Directed Acyclic Graph).
    *   Tính chất **Idempotency** (chạy đi chạy lại 1 pipeline với cùng input phải cho ra cùng output).
    *   Chiến lược tải dữ liệu: Full Refresh vs Incremental Load vs Backfill.
    *   Xử lý lỗi: Retry, alerting, dead-letter-queue.
    *   SLA (Service Level Agreement) và Data Contract.
*   **Bài tập thực hành (Artifact):** Tạo file `week4_pipeline_design.md` gồm:
    *   Bản vẽ kiến trúc DAG của một hệ thống ETL thực tế.
    *   Giải trình chi tiết về chiến lược đảm bảo Idempotency cho hệ thống đó.
    *   Ma trận xử lý lỗi (Failure Scenario Matrix) cho từng bước trong luồng dữ liệu.

---

## 💾 GIAI ĐOẠN 2: Core Skills — Modeling, dbt & Airflow (Tuần 5 – 12)
*Mục tiêu: Đạt trình độ Mid-level DE về thiết kế kho dữ liệu (DWH) và tự động hóa.*

### 📚 Tuần 5 - 6: Dimensional Data Modeling (Mô hình hóa dữ liệu)
*   **Tài liệu học:** [Week05_Dimensional_Modeling.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week05_Dimensional_Modeling.html)
*   **Lý thuyết cốt lõi:**
    *   Mô hình Kimball: Star Schema vs Snowflake Schema.
    *   Xác định hạt dữ liệu (Grain) của bảng Fact và Dimension.
    *   Phân biệt Surrogate Key (Khóa thay thế) và Natural Key (Khóa tự nhiên).
    *   Thiết kế Slowly Changing Dimensions (SCD Type 1, SCD Type 2, SCD Type 3).
    *   Thiết kế Cumulative Table (Mô hình tích lũy theo thời gian).
*   **Bài tập thực hành (Artifact):**
    *   DDL cho bảng chiều khách hàng lưu lịch sử đổi địa chỉ (`actors_history_scd` sử dụng SCD Type 2).
    *   Viết query SQL thực hiện cập nhật tích lũy (Cumulative) dữ liệu hoạt động của người dùng qua từng năm.
*   **Exit Criteria:** Trả lời trôi chảy câu hỏi: *"Làm thế nào để truy vấn dữ liệu của một khách hàng tại một thời điểm chính xác trong quá khứ khi họ liên tục thay đổi thông tin?"*

### 📚 Tuần 7: Fact Data Modeling (Mô hình hóa bảng Fact)
*   **Tài liệu học:** [Week07_Fact_Modeling.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week07_Fact_Modeling.html)
*   **Lý thuyết cốt lõi:**
    *   Phân loại bảng Fact: Transaction Fact, Periodic Snapshot Fact, Accumulating Snapshot Fact.
    *   Deduplication (Loại bỏ trùng lặp dữ liệu) bằng phương pháp `ROW_NUMBER()` hoặc Microbatch.
    *   Tối ưu hóa dung lượng lưu trữ bảng Fact: Dùng Bit Arrays / Compressed Format.
*   **Bài tập thực hành (Artifact):**
    *   Viết script SQL tải dữ liệu gia tăng (Incremental) cho bảng Fact mà không gây trùng lặp.
    *   Code tối ưu lưu trữ bảng hoạt động của máy chủ dạng Bit-packed.

### 📚 Tuần 8 - 9: Analytics Engineering với dbt (Data Build Tool)
*   **Tài liệu học:** [Week08_dbt.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week08_dbt.html)
*   **Lý thuyết cốt lõi:**
    *   Mô hình ELT (Extract - Load - Transform): dbt đảm nhiệm chữ T.
    *   Cấu trúc dự án dbt: `models/`, `tests/`, `macros/`, `snapshots/`.
    *   Phân cấp mô hình dữ liệu: **Staging** (làm sạch sơ bộ) ➔ **Intermediate** (logic nghiệp vụ) ➔ **Marts** (bảng Fact/Dim cuối cùng cho BI).
    *   Sử dụng hàm `ref()` và `source()` để dbt tự động vẽ biểu đồ phụ thuộc (Lineage).
    *   Viết các bài kiểm tra chất lượng dữ liệu (dbt tests) và viết tài liệu tự động (`dbt docs`).
*   **Bài tập thực hành (Artifact):** Xây dựng thư mục `dbt_project/` chứa:
    *   Các model staging (`stg_orders.sql`, `stg_customers.sql`).
    *   Model marts (`fct_orders.sql`, `dim_customers.sql`).
    *   Các file cấu hình test schema (`schema.yml`) kiểm tra tính độc nhất (`unique`) và không null (`not_null`).
*   **Exit Criteria:** Chạy thành công lệnh `dbt build` không lỗi, tạo được trang tài liệu Lineage sạch đẹp.

### 📚 Tuần 10 - 11: Orchestration với Apache Airflow
*   **Tài liệu học:** [Week10_Airflow.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week10_Airflow.html)
*   **Lý thuyết cốt lõi:**
    *   Kiến trúc Airflow: Scheduler, Webserver, Worker, Metadata Database.
    *   Định nghĩa DAG bằng Python, thiết lập lịch chạy (Schedule Interval).
    *   Sử dụng các Operators: `PythonOperator`, `BashOperator`, `SQLExecuteQueryOperator`.
    *   Truyền dữ liệu nhỏ giữa các task qua **XComs**.
    *   Kỹ thuật **Backfill** (chạy bù dữ liệu lịch sử) và thiết kế DAG Idempotent.
    *   Liên kết Airflow với dbt: Chạy dbt models thông qua Airflow task.
*   **Bài tập thực hành (Artifact):** Tạo thư mục `airflow_dags/` chứa:
    *   `etl_orders_daily.py`: DAG chạy hàng ngày lúc 6:00 AM để kéo dữ liệu.
    *   `dbt_pipeline.py`: DAG kích hoạt dbt biến đổi dữ liệu sau khi ETL hoàn tất.
    *   `backfill_historical.py`: File cấu hình chạy bù dữ liệu cho 30 ngày trước.
*   **Exit Criteria:** Khởi chạy được Airflow trên Docker Compose local, kích hoạt chạy thử một DAG và kiểm tra lịch sử chạy thành công trên giao diện Web UI.

### 📚 Tuần 12: Đảm Bảo Chất Lượng Dữ Liệu & Mini-Project Tổng Hợp
*   **Tài liệu học:** Xem lại toàn bộ tài liệu Giai đoạn 1-2.
*   **Lý thuyết cốt lõi:**
    *   Quy trình kiểm tra chất lượng: Unit Test ➔ Integration Test ➔ Data Quality Test.
    *   Sử dụng công cụ **Soda SQL** hoặc **Great Expectations** để kiểm tra dữ liệu trước khi đẩy vào Marts.
    *   Thiết kế Data Contract giữa đội nguồn (Producer) và đội dữ liệu (Consumer).
*   **Bài tập thực hành (Artifact):** Xây dựng hệ thống Mini-Project hoàn chỉnh:
    *   Airflow tự động trigger ➔ Python script kéo data ➔ Validate bằng Great Expectations ➔ Nạp vào Postgres DWH ➔ Kích hoạt dbt transform sang Star Schema.
*   **Exit Criteria:** Toàn bộ hệ thống chạy tự động bằng 1 nút bấm hoặc theo lịch trình, tự động gửi cảnh báo nếu dữ liệu đầu vào không đạt chất lượng.

---

## ☁️ GIAI ĐOẠN 3: Cloud & Big Data Processing (Tuần 13 – 17)
*Mục tiêu: Đưa dữ liệu lên Cloud và xử lý dữ liệu lớn ở quy mô Terabyte.*

### 📚 Tuần 13: Hạ Tầng Điện Toán Đám Mây (AWS)
*   **Tài liệu học:** [Week13_Cloud_AWS.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week13_Cloud_AWS.html)
*   **Lý thuyết cốt lõi:**
    *   Lưu trữ đối tượng (Object Storage) với **Amazon S3**: Tạo bucket, phân chia thư mục (Partitioning), vòng đời tệp tin (Lifecycle Policy).
    *   Quản lý phân quyền với **IAM**: Tạo Role, Policy theo nguyên tắc cấp quyền tối thiểu (Least Privilege).
    *   Sử dụng serverless query engine **AWS Athena** để truy vấn trực tiếp dữ liệu trên S3 thông qua SQL.
*   **Bài tập thực hành (Artifact):** Tạo thư mục `cloud_setup/terraform/` (hoặc viết tài liệu cấu hình thủ công) để:
    *   Tạo 3 phân vùng S3 bucket: `raw-zone`, `staging-zone`, `curated-zone`.
    *   Cấu hình IAM Role cho phép Airflow local ghi dữ liệu lên S3 an toàn.

### 📚 Tuần 14: Kho Dữ Liệu Hiện Đại (Modern Data Warehouse & Lakehouse)
*   **Tài liệu học:** [Week14_Data_Warehouse.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week14_Data_Warehouse.html)
*   **Lý thuyết cốt lõi:**
    *   Kiến trúc Columnar Storage (Lưu trữ dạng cột) của các Cloud DWH: **Snowflake**, **Google BigQuery**.
    *   Cơ chế kiểm soát chi phí (Cost Control) khi truy vấn trên dữ liệu lớn.
    *   Định dạng bảng hiện đại: **Apache Iceberg**, Delta Lake (giúp hỗ trợ các tính năng ACID, Time Travel trên Data Lake).
*   **Bài tập thực hành (Artifact):**
    *   Cấu hình chuyển đổi (Migrate) dự án dbt từ PostgreSQL local sang kết nối với BigQuery hoặc Snowflake.
    *   Viết báo cáo ngắn so sánh chi phí chạy truy vấn giữa 3 nền tảng: Redshift, BigQuery, Snowflake cho cùng một lượng dữ liệu.

### 📚 Tuần 15: Tích Hợp Dữ Liệu & Công Cụ Ingestion
*   **Tài liệu học:** [Week15_Data_Integration.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week15_Data_Integration.html)
*   **Lý thuyết cốt lõi:**
    *   Tại sao mô hình ELT (Extract - Load - Transform) tối ưu hơn ETL trên Cloud.
    *   Sử dụng công cụ ingestion dựa trên Connector: **Airbyte**, **dlt (data load tool)**.
    *   Change Data Capture (CDC): Đọc log thay đổi từ cơ sở dữ liệu gốc bằng **Debezium**.
*   **Bài tập thực hành (Artifact):**
    *   Viết một script Python sử dụng thư viện `dlt` để tự động kéo dữ liệu từ một API bên ngoài và ghi trực tiếp vào BigQuery/Snowflake.
    *   Cấu hình đồng bộ dữ liệu CDC qua Airbyte.

### 📚 Tuần 16 - 17: Xử Lý Dữ Liệu Lớn Với Apache Spark
*   **Tài liệu học:** [Week16_Spark.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week16_Spark.html)
*   **Lý thuyết cốt lõi:**
    *   Kiến trúc phân tán của Spark: Driver, Executor, Stage, Task, cơ chế Shuffle.
    *   Phân biệt RDD, DataFrame và Dataset. Tư duy Lazy Evaluation (Đánh giá lười biếng).
    *   Các chiến lược Join dữ liệu lớn: **Broadcast Join**, Sort-Merge Join, Shuffle Hash Join.
    *   Kỹ thuật phân chia dữ liệu: `repartition` vs `coalesce`, phân vùng khi ghi file Parquet (`partitionBy`).
    *   Đọc và gỡ lỗi hiệu năng bằng **Spark UI** (xác định nghẽn cổ chai - Bottleneck, lỗi lệch dữ liệu - Data Skew).
*   **Bài tập thực hành (Artifact):** Xây dựng thư mục `spark_jobs/` chứa:
    *   `broadcast_join_job.py`: Tối ưu hóa truy vấn bằng cách broadcast bảng danh mục nhỏ vào bảng giao dịch lớn.
    *   `sort_within_partitions.py`: Code tối ưu hóa sắp xếp dữ liệu trên từng phân vùng để giảm thiểu shuffle.
    *   `tests/test_transform.py`: Viết Unit Test cho các hàm biến đổi của Spark sử dụng dữ liệu giả lập (Mock DataFrame).
*   **Exit Criteria:** Chạy thành công Spark job xử lý tệp tin Parquet dung lượng trên 10GB mà không gặp lỗi OutOfMemory (OOM).

---

## ⚡ GIAI ĐOẠN 4: Real-time Streaming & Analytical Patterns (Tuần 18 – 22)
*Mục tiêu: Xây dựng luồng dữ liệu thời gian thực và thực hiện các phân tích nghiệp vụ phức tạp.*

### 📚 Tuần 18 - 19: Streaming Pipelines với Kafka & Apache Flink
*   **Tài liệu học:** [Week18_Flink_Kafka.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week18_Flink_Kafka.html)
*   **Lý thuyết cốt lõi:**
    *   Hệ thống tin nhắn phân tán **Apache Kafka**: Topic, Partition, Consumer Group, Offset.
    *   Kiến trúc xử lý luồng (Stream Processing) của **Apache Flink**: JobManager, TaskManager, State Backend (RocksDB).
    *   Các khái niệm thời gian: Event Time vs Processing Time.
    *   Xử lý dữ liệu đến muộn bằng **Watermarks**.
    *   Kỹ thuật phân nhóm sự kiện theo phiên truy cập (**Sessionization**).
*   **Bài tập thực hành (Artifact):** Xây dựng thư mục `flink_jobs/` chứa:
    *   `kafka_producer_mock.py`: Script giả lập liên tục sinh ra dữ liệu clickstream của người dùng gửi vào Kafka.
    *   `session_by_ip.py`: Flink job đọc từ Kafka, gom nhóm các clickstream theo IP của người dùng trong khoảng thời gian không hoạt động là 5 phút (Session Window).
*   **Exit Criteria:** Hệ thống streaming chạy liên tục, đọc dữ liệu từ Kafka, xử lý session và ghi kết quả thời gian thực vào PostgreSQL hoặc S3.

### 📚 Tuần 20: Công Cụ OLAP Hiện Đại (Modern OLAP Engines)
*   **Tài liệu học:** [Week20_Modern_OLAP.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week20_Modern_OLAP.html)
*   **Lý thuyết cốt lõi:**
    *   Tại sao cần các engine OLAP riêng biệt cho mục đích phân tích tốc độ cao.
    *   **DuckDB**: Chạy SQL phân tích cực nhanh trực tiếp trên máy cá nhân với tệp Parquet.
    *   **ClickHouse**: Cơ sở dữ liệu dạng cột cho các truy vấn phân tích thời gian thực với hàng tỷ bản ghi.
*   **Bài tập thực hành (Artifact):**
    *   Viết script benchmark tốc độ chạy cùng 1 câu truy vấn tổng hợp phức tạp trên 10 triệu dòng giữa: PostgreSQL local, DuckDB, và ClickHouse. Chụp lại bảng so sánh thời gian phản hồi.

### 📚 Tuần 21: Các Mô Hình Phân Tích Dữ Liệu Nâng Cao (Analytical Patterns)
*   **Tài liệu học:** [Week21_Analytical_Patterns.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week21_Analytical_Patterns.html)
*   **Lý thuyết cốt lõi:**
    *   State Change Tracking: Theo dõi và ghi nhận sự thay đổi trạng thái của thực thể theo thời gian.
    *   Phân tích Phễu chuyển đổi (Funnel Analysis): Đo lường tỉ lệ rớt của người dùng qua từng bước hành vi.
    *   Phân tích Tỉ lệ giữ chân (Cohort Retention Analysis).
    *   Mô hình phân bổ chuyển đổi (Attribution Modeling): First-touch, Last-touch, Multi-touch.
*   **Bài tập thực hành (Artifact):** Tạo file `analytical_patterns.sql` chứa các câu truy vấn chuẩn production cho:
    *   Truy vấn tính số ngày hoạt động liên tục lớn nhất của người dùng (Streak).
    *   Truy vấn tính tỉ lệ giữ chân khách hàng (Cohort Retention) theo chu kỳ 30 - 60 - 90 ngày.
    *   Truy vấn phân tích phễu mua hàng (từ Xem sản phẩm ➔ Thêm vào giỏ ➔ Thanh toán).

### 📚 Tuần 22: Thiết Kế Chỉ Số (KPI), Thử Nghiệm A/B & Dashboard
*   **Tài liệu học:** [Week22_KPI_Dashboard.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week22_KPI_Dashboard.html)
*   **Lý thuyết cốt lõi:**
    *   Xây dựng hệ thống chỉ số: Chỉ số mục tiêu tối thượng (North Star Metric) và các chỉ số bổ trợ.
    *   Lý thuyết thử nghiệm A/B: Thiết lập phân nhóm (Allocation), tính cỡ mẫu (Sample Size), p-value và khoảng tin cậy.
    *   Thiết kế Dashboard phục vụ vận hành (Operational) và phục vụ ban giám đốc (Executive).
*   **Bài tập thực hành (Artifact):**
    *   Tạo file `ab_experiment_design.md` mô tả thiết kế 3 thử nghiệm A/B thực tế kèm chỉ số đo lường.
    *   Dựng và xuất bản (Publish) một dashboard công khai trên Tableau Public hoặc Metabase kết nối với Marts dữ liệu đã xây dựng.

---

## 🛠️ GIAI ĐOẠN 5: Vận Hành Hệ Thống & Bảo Trì (Tuần 23)
*Mục tiêu: Học cách làm việc và quản trị hệ thống như một kỹ sư thực thụ trong môi trường thực tế.*

*   **Tài liệu học:** [Week23_Maintenance.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week23_Maintenance.html)
*   **Lý thuyết cốt lõi:**
    *   Mô hình chịu trách nhiệm hệ thống: Người chịu trách nhiệm chính (Primary Owner) và phụ (Secondary Owner).
    *   Cách xây dựng tài liệu xử lý sự cố nhanh (**Runbook**).
    *   Giám sát luồng đi của dữ liệu (**Data Lineage**) thông qua tiêu chuẩn mở **OpenLineage**.
    *   Định nghĩa SLI, SLO, SLA cho chất lượng và thời gian hoàn thành pipeline.
*   **Bài tập thực hành (Artifact):** Tạo các tài liệu sau trong repo:
    *   `runbook_pipeline_failure.md`: Tài liệu hướng dẫn từng bước xử lý cho kỹ sư trực ca khi pipeline dbt/Airflow bị lỗi.
    *   `risk_register.md`: Bản ghi nhận 5 rủi ro lớn nhất của hệ thống dữ liệu hiện tại và phương án giảm thiểu.

---

## 🏆 GIAI ĐOẠN 6: Dự Án Tốt Nghiệp (Capstone) & Phỏng Vấn (Tuần 24 – 28)
*Mục tiêu: Đóng gói tất cả kiến thức thành 1 dự án lớn và sẵn sàng chinh phục các buổi phỏng vấn.*

### 🚀 Capstone Project: Xây Dựng Hệ Thống Dữ Liệu End-to-End
*   **Tài liệu học:** [Week24_Capstone.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week24_Capstone.html)
*   **Đề bài:** Thiết kế và code hệ thống dữ liệu hoàn chỉnh cho một doanh nghiệp tự chọn (ví dụ: E-commerce hoặc Fintech) bao gồm đủ 7 tầng:
    1.  **Ingestion:** Dùng `dlt` hoặc Airbyte kéo dữ liệu tự động từ API/Database.
    2.  **Storage:** Lưu trữ dữ liệu thô trên AWS S3 dưới dạng Parquet/Iceberg.
    3.  **Batch Processing:** Spark job xử lý historical data lớn.
    4.  **Transform:** Dự án dbt phân chia Staging ➔ Marts trên Snowflake/BigQuery.
    5.  **Orchestration:** Airflow DAGs điều phối toàn bộ lịch chạy, thiết lập retry và cảnh báo.
    6.  **Analytics:** Viết SQL phân tích Cohort, Phễu chuyển đổi và dựng dashboard BI.
    7.  **Operations:** Cung cấp Runbook và sơ đồ Lineage.
*   **Artifact:** Repo riêng biệt trên GitHub chứa toàn bộ code và file `README.md` mô tả kiến trúc (kèm sơ đồ vẽ bằng Draw.io/Mermaid), các quyết định đánh đổi công nghệ (Trade-off).

### 💬 Luyện Phỏng Vấn (Interview Prep)
*   **Tài liệu học:** Đọc kỹ toàn bộ tệp trong thư mục [interview-prep/](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/interview-prep/) và [interview-prep-html/](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/interview-prep-html/).
*   **Các mảng cần ôn luyện:**
    *   **SQL Round:** Luyện giải bài tập trực tiếp trên bảng trắng (Whiteboard).
    *   **Data Modeling Round:** Thiết kế mô hình dữ liệu Star Schema cho 1 bài toán kinh doanh mới trong 30 phút.
    *   **System Design Round:** Thiết kế kiến trúc chịu tải lớn (ví dụ: *"Hãy thiết kế hệ thống xử lý 1TB dữ liệu/ngày"*).
    *   **Behavioral Round:** Chuẩn bị sẵn 3 câu chuyện thực tế về: Lần làm sập production và cách khắc phục; Cách xử lý bất đồng quan điểm kỹ thuật với đồng nghiệp; Cách tối ưu chi phí hạ tầng.

---

## 🛠️ CÔNG THỨC HỌC TẬP HÀNG NGÀY BẰNG AI (CLAUDE AI)
Để rút ngắn thời gian và học hiệu quả gấp 3 lần, hãy áp dụng quy trình 4 bước sau mỗi khi bạn mở một bài học `WeekXX_*.html`:

1.  **Bước 1 (Đọc & Tóm tắt):** copy phần nội dung lý thuyết của bài học vào Claude và yêu cầu: *"Tóm tắt cho tôi 3 khái niệm cốt lõi của bài học này dưới dạng sơ đồ tư duy dạng chữ."*
2.  **Bước 2 (Giải thích code):** Khi gặp các đoạn code Spark hoặc SQL phức tạp, hãy hỏi: *"Hãy giải thích từng dòng code này hoạt động như thế nào và chỉ ra 2 lỗi sai phổ biến nhất khi viết đoạn code này trong thực tế."*
3.  **Bước 3 (Thực hành có chấm điểm):** Trước khi tự code bài tập, yêu cầu Claude: *"Hãy tạo cho tôi một đề bài tập thực hành nhỏ dựa trên kiến thức của bài học này kèm theo bộ dữ liệu giả lập (mock data dạng CSV) để tôi làm thử."* Sau khi bạn viết xong code, gửi lại cho Claude và yêu cầu: *"Hãy chấm điểm code của tôi theo thang điểm 10 của Senior Data Engineer và đề xuất cách tối ưu."*
4.  **Bước 4 (Mock Interview hàng ngày):** Khi kết thúc tuần học, hỏi Claude: *"Đóng vai là Trưởng phòng Dữ liệu đang phỏng vấn tôi về chủ đề của tuần này. Hãy đặt cho tôi 3 câu hỏi phỏng vấn hóc búa nhất và đánh giá câu trả lời của tôi."*
