# MASTER PROMPT — Xây dựng file HTML Tutorial Data Engineering

> Copy toàn bộ prompt này và paste vào Claude khi muốn build từng tuần.  
> Thay các placeholder `[...]` bằng nội dung cụ thể của tuần đó.

---

## 🧭 CONTEXT (đưa vào đầu mỗi prompt)

```
Tôi đang xây dựng bộ tài liệu học Data Engineering dạng HTML tương tác,
dựa trên repo: https://github.com/DataExpert-io/data-engineer-handbook

Roadmap học gồm 6 giai đoạn, 24-28 tuần, xuất phát điểm là người đã biết ETL + SQL.
Mỗi tuần sẽ có 1 file HTML độc lập, tự học được không cần backend.

File mẫu tham chiếu: "Data_Engineering_Handbook___Intermediate_Week_1_Tutorial.html"
(file này tôi đã cung cấp ở trên — hãy dùng đúng format, CSS variables, 
component patterns, và JavaScript logic từ file đó)
```

---

## 📋 FORMAT CHUẨN CẦN GIỮ NGUYÊN (không được thay đổi)

### CSS Variables bắt buộc
```css
:root {
  --bg: #0d1117;
  --surface: #161b22;
  --surface2: #21262d;
  --border: #30363d;
  --accent: #58a6ff;       /* xanh dương — tiêu đề, active nav */
  --accent2: #3fb950;      /* xanh lá — đúng, tip */
  --accent3: #f78166;      /* đỏ cam — sai, cảnh báo */
  --accent4: #d2a8ff;      /* tím — code inline */
  --accent5: #ffa657;      /* cam — warn, practice */
  --text: #e6edf3;
  --text-muted: #8b949e;
  --code-bg: #0d1117;
  --highlight: #388bfd26;
}
```

### Layout bắt buộc
```
[Hero Banner]
  ├── h1: tên tutorial
  ├── p: mô tả ngắn
  └── badge-row: phase badge + week badge + level badge

[Container]
  ├── [Sidebar - 290px fixed]
  │    ├── sidebar-title: "CHƯƠNG TRÌNH HỌC"
  │    └── nav-items: danh sách module, click để show/hide
  └── [Main content]
       └── [Modules - display:none, active = display:block]
            └── [Module]
                 ├── module-header (badge + title + subtitle + progress-bar)
                 └── sections (collapsible, mỗi section có header + content)
```

### Cấu trúc bắt buộc của mỗi Module
Mỗi module PHẢI có đủ 6 section theo thứ tự này:

```
Section 1: 📋 Menu Tổng Thể        (icon-purpose) — bảng tóm tắt các bước
Section 2: 🎯 Mục Đích Module      (icon-purpose) — bullet list mục tiêu
Section 3: 📖 Giải Thích Chi Tiết  (icon-detail)  — nội dung + code blocks + tables
Section 4: ❓ Câu Hỏi Ôn Tập       (icon-quiz)    — 10 quiz items interactive
Section 5: 📌 Tổng Kết             (icon-summary) — summary-grid 2 cột, 6 ô
Section 6: 🔬 Bài Tập Thực Hành   (icon-practice)— practice-tasks + solution toggle
```

### JavaScript functions bắt buộc
```javascript
showModule(idx, el)      // show/hide module, update nav active
goNext(idx)              // nút "Module tiếp theo →"
goPrev(idx)              // nút "← Module trước"
toggleSection(header)    // collapse/expand section
answerQuiz(el, correct, explanation)  // interactive quiz
toggleSolution(btn)      // show/hide solution box
gradeFinalTest()         // chấm điểm mini test cuối file
resetFinalTest()         // reset radio buttons + result
```

### Components bắt buộc
**Code block (cmd-block):**
```html
<div class="cmd-block">
  <div class="cmd-header">
    <div class="cmd-dots">
      <div class="dot dot-red"></div>
      <div class="dot dot-yellow"></div>
      <div class="dot dot-green"></div>
    </div>
    <span>[Tên file / ngôn ngữ]</span>
  </div>
  <div class="cmd-body"><pre>[code với span.prompt, span.comment, span.output]</pre></div>
</div>
```

**Info boxes:**
```html
<div class="info-box tip">✅ <span>[nội dung]</span></div>   <!-- xanh lá -->
<div class="info-box warn">⚠️ <span>[nội dung]</span></div>  <!-- cam -->
<div class="info-box note">📌 <span>[nội dung]</span></div>  <!-- xanh dương -->
```

**Quiz item:**
```html
<div class="quiz-item">
  <div class="quiz-q">[Câu hỏi]</div>
  <div class="quiz-options">
    <div class="quiz-opt" onclick="answerQuiz(this, false, '[giải thích sai]')">A. [đáp án]</div>
    <div class="quiz-opt" onclick="answerQuiz(this, true, '[giải thích đúng]')">B. [đáp án đúng]</div>
    <div class="quiz-opt" onclick="answerQuiz(this, false, '[giải thích sai]')">C. [đáp án]</div>
    <div class="quiz-opt" onclick="answerQuiz(this, false, '[giải thích sai]')">D. [đáp án]</div>
  </div>
  <div class="quiz-explain"></div>
</div>
```

**Practice task với solution:**
```html
<div class="practice-task">
  <div class="practice-task-header">[Tên bài tập]</div>
  <div class="practice-task-body">
    <p>[Đề bài]</p>
    <button class="solution-toggle" onclick="toggleSolution(this)">💡 Xem lời giải</button>
    <div class="solution-box">
      [code block hoặc text giải]
    </div>
  </div>
</div>
```

**Summary grid (section 5):**
```html
<div class="summary-grid">
  <div class="summary-item"><strong>[Label]</strong>[Mô tả ngắn]</div>
  <!-- 6 ô, 2 cột -->
</div>
```

**Mini test cuối file (module cuối):**
```html
<div id="final-test">
  <!-- 15-20 test-question với data-q="N" data-correct="[A/B/C/D]" -->
  <div class="test-question" data-q="1" data-correct="B">
    <div class="test-question-title">Q1. [Câu hỏi]</div>
    <div class="test-options">
      <label class="test-option"><input type="radio" name="q1" value="A"> A. [đáp án]</label>
      <label class="test-option"><input type="radio" name="q1" value="B"> B. [đáp án đúng]</label>
      <label class="test-option"><input type="radio" name="q1" value="C"> C. [đáp án]</label>
      <label class="test-option"><input type="radio" name="q1" value="D"> D. [đáp án]</label>
    </div>
  </div>
  <!-- ... -->
  <div class="test-actions">
    <button class="nav-btn primary" onclick="gradeFinalTest()">✅ Chấm điểm mini test</button>
    <button class="nav-btn" onclick="resetFinalTest()">🔁 Làm lại từ đầu</button>
  </div>
  <div class="test-result" id="final-test-result" style="display:none"></div>
</div>
```

---

## 🎯 TEMPLATE PROMPT THEO TỪNG TUẦN

### ── TUẦN 0: Setup Môi Trường ──

```
Hãy tạo file HTML tương tác tên "Week00_Setup.html" theo đúng format
của file mẫu "Data_Engineering_Handbook___Intermediate_Week_1_Tutorial.html".

=== THÔNG TIN TUẦN ===
Tên: Tuần 0 – Setup Môi Trường
Giai đoạn: Giai đoạn 0 (Trước khi bắt đầu)
Level: Beginner → Tất cả cấp độ
Mục tiêu: Cài đặt và xác nhận toàn bộ môi trường học trước khi bắt đầu bất kỳ module nào

=== CÁC MODULE (sidebar navigation) ===
W0.01 – Tổng Quan & Checklist
W0.02 – Cài Docker + PostgreSQL
W0.03 – Cài Python 3.11+ & VS Code
W0.04 – Setup Git & GitHub
W0.05 – Chạy thử Spark Local
W0.06 – Xác minh toàn bộ & Exit Criteria
W0.07 – Mini Test Tổng Kết

=== NỘI DUNG CHI TIẾT TỪNG MODULE ===

[W0.01] Tổng Quan & Checklist
- Hero badge: "Giai đoạn 0" (green) + "Setup Environment" (orange) + "Bắt buộc hoàn thành trước tuần 1" (blue)
- Giải thích TẠI SAO setup quan trọng: môi trường sai → học sai → mất thời gian
- Checklist exit criteria của toàn bộ tuần 0:
  □ Docker chạy được, docker compose up thành công
  □ PostgreSQL truy cập được từ SQL client
  □ Python 3.11+ cài xong, pip hoạt động
  □ Git config xong, có repo de-roadmap-artifacts trên GitHub
  □ VS Code với extensions: Python, SQLTools, Docker, Jupyter
  □ Spark local chạy được 1 notebook đơn giản
  □ Chụp screenshot tất cả exit criteria, commit lên GitHub
- Bảng tổng quan tech stack theo giai đoạn (từ roadmap):
  | Giai đoạn | Tuần | Tech Stack chính |
  | 0-1 | 0-4 | SQL · Python · PostgreSQL · Docker · Git |
  | 2 | 5-12 | dbt · Airflow · Data Modeling |
  | 3 | 13-17 | Spark · Cloud · Snowflake · Airbyte |
  | 4 | 18-22 | Flink · Kafka · ClickHouse |
  | 5-6 | 23-27 | KPI · Dashboard · Capstone |
- Info box tip: "Đừng bỏ qua tuần này — setup sai là nguồn gốc của 80% lỗi kỳ lạ sau này"
- Quiz: 10 câu về tầm quan trọng của môi trường, exit criteria

[W0.02] Cài Docker + PostgreSQL
- Giải thích Docker là gì và tại sao dùng Docker thay vì cài native
- Hướng dẫn cài Docker Desktop (Windows/Mac/Linux — 3 tab khác nhau)
- Lệnh kiểm tra Docker hoạt động:
  docker --version
  docker run hello-world
  docker compose version
- Chạy PostgreSQL bằng Docker Compose:
  Tạo file docker-compose.yml mẫu với postgres:15 + pgadmin4
  Lệnh: docker compose up -d
  Kiểm tra: docker ps, truy cập pgadmin tại localhost:5050
- Kết nối SQL client (DBeaver hoặc DataGrip):
  host: localhost, port: 5432, db: postgres, user: postgres, pass: postgres
- Chạy query kiểm tra: SELECT version();
- Info box warn: "Windows: bật WSL2 trước khi cài Docker Desktop"
- Code blocks: PowerShell + bash song song
- Quiz: 6 câu về Docker commands, ports, docker compose
- Practice: Chạy stack, chụp kết quả docker ps và SELECT version()

[W0.03] Cài Python 3.11+ & VS Code
- Tải Python 3.11+ từ python.org (Windows dùng installer, Mac dùng pyenv)
- Virtual environment: python -m venv .venv, activate, kiểm tra
- Cài các thư viện cốt lõi DE:
  pip install pandas sqlalchemy psycopg2-binary requests jupyter
  pip install dbt-postgres dbt-snowflake (preview — sẽ dùng ở giai đoạn 2)
- VS Code extensions bắt buộc:
  - Python (ms-python)
  - SQLTools + SQLTools PostgreSQL Driver
  - Docker
  - Jupyter
  - GitLens
- Kiểm tra Python hoạt động:
  import pandas as pd; print(pd.__version__)
  import sqlalchemy; print(sqlalchemy.__version__)
- Kết nối PostgreSQL từ Python:
  engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
  df = pd.read_sql("SELECT version()", engine)
  print(df)
- Quiz: 10 câu về virtual env, thư viện, extensions
- Practice: Chạy script Python kết nối DB thành công, in ra version

[W0.04] Setup Git & GitHub
- Git config: user.name, user.email, default branch main
- SSH key setup (Windows + Mac/Linux hướng dẫn riêng)
- Tạo repo "de-roadmap-artifacts" trên GitHub:
  - Public repo
  - README.md với mô tả roadmap
  - Cấu trúc thư mục gợi ý:
    de-roadmap-artifacts/
    ├── week00_setup/
    ├── week01_sql_advanced/
    ├── week02_python_etl/
    ...
- Git workflow cơ bản cho DE:
  git init, git add, git commit -m "feat: week00 setup done"
  git push origin main
- Conventional commits cho DE: feat / fix / docs / test / chore
- .gitignore mẫu cho DE project: .env, __pycache__, .venv, *.pyc, .DS_Store
- Quiz: 10 câu về git commands, SSH, gitignore
- Practice: Tạo repo, commit file README.md đầu tiên, push lên GitHub

[W0.05] Chạy thử Spark Local
- Spark là gì — giải thích đơn giản: "pandas cho dữ liệu không vừa RAM"
- Cài PySpark: pip install pyspark
- Tạo SparkSession đầu tiên:
  from pyspark.sql import SparkSession
  spark = SparkSession.builder.appName("Week0Test").getOrCreate()
  df = spark.createDataFrame([{"name": "Alice", "age": 30}])
  df.show()
  print(spark.version)
- Chạy Jupyter Notebook với PySpark
- Xem Spark UI tại localhost:4040 khi job đang chạy
- Info box note: "Spark sẽ dùng nhiều RAM — đảm bảo máy có ít nhất 8GB"
- Info box warn: "Java 8/11/17 phải được cài trước — Spark cần JVM"
- Quiz: 10 câu về Spark basic, SparkSession, UI port
- Practice: Chạy SparkSession, tạo DataFrame, show() thành công

[W0.06] Xác Minh Toàn Bộ & Exit Criteria
- Script tự kiểm tra toàn bộ môi trường (Python):
  Kiểm tra docker, python version, git, các thư viện
  In ra PASS/FAIL cho từng mục
- Checklist cuối cùng có thể tick:
  □ docker --version → Docker 24.x+
  □ docker compose version → 2.x+
  □ PostgreSQL SELECT version() → 15.x
  □ python --version → 3.11+
  □ import pandas, sqlalchemy, pyspark thành công
  □ git --version + remote repo tồn tại
  □ Spark DataFrame show() chạy được
  □ Tất cả đều đã commit lên de-roadmap-artifacts
- Lệnh tổng hợp xác minh:
  docker ps (phải thấy postgres + pgadmin running)
  python verify_setup.py (script tự viết)
  git log --oneline (phải thấy ít nhất 1 commit)
- Screenshot template: hướng dẫn chụp gì để commit
- Info box tip: "Xong bước này = bạn đã sẵn sàng 100% cho tuần 1"

[W0.07] Mini Test Tổng Kết
- 20 câu trắc nghiệm bao phủ toàn bộ tuần 0:
  - Docker: commands, ports, volumes (10 câu)
  - Python/pip: venv, thư viện, kết nối DB (4 câu)
  - Git/GitHub: workflow, SSH, gitignore (4 câu)
  - Spark: SparkSession, UI, JVM (4 câu)
  - Tổng hợp exit criteria (3 câu)
- Hướng dẫn sau test:
  < 12 điểm: Làm lại module còn yếu trước khi sang tuần 1
  12-15 điểm: Ổn, nhưng ôn lại 1-2 điểm chưa chắc
  16-18 điểm: Tốt, sẵn sàng cho tuần 1
  19-20 điểm: Xuất sắc, có thể bắt đầu tuần 1 ngay

=== YÊU CẦU KỸ THUẬT ===
- File HTML hoàn chỉnh, không cần backend, chạy được bằng cách mở trực tiếp
- Tất cả CSS inline trong <style> tag
- Tất cả JS inline trong <script> tag cuối file
- Không dùng framework external (không React, không Vue, không Bootstrap)
- Font: 'Segoe UI', -apple-system, sans-serif (giống file mẫu)
- Responsive: sidebar ẩn trên mobile (<768px)
- Code blocks phải có syntax highlight bằng CSS span classes:
  .prompt (xanh lá), .comment (muted), .output (cam)
- Mỗi section mặc định OPEN (không collapsed) trừ section 6 (Practice)
- Nav buttons cuối mỗi module: "← Module trước" | "Module tiếp theo →"
- Module đầu tiên (W0.01) active mặc định khi load
- Title tab: "DE Handbook · Tuần 0 · Setup Môi Trường"

=== TIÊU CHUẨN CHẤT LƯỢNG NỘI DUNG ===
- Tiếng Việt hoàn toàn, giữ thuật ngữ kỹ thuật tiếng Anh
- Mỗi code block phải chạy được thực tế — không pseudo-code
- Mỗi quiz item phải có đúng 4 đáp án A/B/C/D với giải thích cho từng đáp án
- Explanation khi chọn sai phải giải thích TẠI SAO sai, không chỉ "không đúng"
- Practice task phải có đề bài cụ thể + expected output + lời giải ẩn
- Không dùng nội dung chung chung — tất cả ví dụ phải liên quan đến Data Engineering
- Info boxes dùng đúng loại: tip (mẹo tốt), warn (cẩn thận), note (thông tin quan trọng)
- Summary grid mỗi section tóm tắt 6 điểm quan trọng nhất

=== OUTPUT ===
Tạo 1 file HTML duy nhất, đặt tên "Week00_Setup.html"
Viết đầy đủ — không dùng comment "// thêm nội dung tương tự" hay "..."
Mỗi module phải đầy đủ 6 section với nội dung thật, không placeholder
```

---

### ── TUẦN 1: SQL Nâng Cao cho DE ──

```
Hãy tạo file HTML tương tác tên "Week01_SQL_Advanced.html" theo đúng format
của file mẫu "Data_Engineering_Handbook___Intermediate_Week_1_Tutorial.html".

=== THÔNG TIN TUẦN ===
Tên: Tuần 1 – SQL Nâng Cao cho Data Engineer
Giai đoạn: Giai đoạn 1 · Foundation
Level: Beginner-Intermediate
Mục tiêu: Thành thạo SQL ở mức Data Engineer — window functions, SCD, incremental, optimization

=== CÁC MODULE ===
W1.01 – Tổng Quan Tuần & Mục Tiêu
W1.02 – Window Functions Nâng Cao
W1.03 – GROUPING SETS, ROLLUP, CUBE
W1.04 – Slowly Changing Dimensions (SCD)
W1.05 – Incremental Load Patterns
W1.06 – Query Optimization & EXPLAIN
W1.07 – Artifact: week1_sql_advanced.sql
W1.08 – Mini Test Tổng Kết

=== NỘI DUNG CHI TIẾT ===

[W1.01] Tổng Quan Tuần & Mục Tiêu
- Hero badges: "Giai đoạn 1 · Foundation" + "Tuần 1: SQL Nâng Cao" + "~15 giờ"
- Tại sao SQL của DE khác SQL thông thường:
  Analyst SQL → SELECT, JOIN, GROUP BY để trả lời câu hỏi
  Engineer SQL → xây pipeline, model lịch sử, optimize cho million+ rows
- Bảng so sánh SQL Analyst vs SQL Data Engineer:
  | Kỹ năng | Analyst | Data Engineer |
  | Window functions | Cơ bản | Nâng cao, production |
  | Lịch sử dữ liệu | Không cần | SCD Type 1/2/3 |
  | Load strategy | Full load | Incremental bắt buộc |
  | Performance | Không quan tâm | EXPLAIN ANALYZE, partition |
  | Pipeline | Không | Idempotent, backfill |
- Checklist kết thúc tuần:
  □ Viết được window function cho mọi use case analytics
  □ Implement SCD Type 1 và Type 2 từ đầu bằng SQL
  □ Viết incremental load script có idempotency
  □ Dùng EXPLAIN ANALYZE để tìm bottleneck
  □ Hoàn thành artifact week1_sql_advanced.sql
- Artifact đầu ra: 1 file SQL có 11 queries, mỗi query có comment giải thích

[W1.02] Window Functions Nâng Cao
- Giải thích OVER clause: PARTITION BY, ORDER BY, frame specification
- 5 nhóm window functions cần thành thạo:
  1. Ranking: ROW_NUMBER, RANK, DENSE_RANK, NTILE
  2. Offset: LAG, LEAD (n periods, default value)
  3. Aggregate: SUM/AVG/COUNT OVER, MIN/MAX OVER
  4. Frame: ROWS BETWEEN, RANGE BETWEEN, UNBOUNDED
  5. Statistical: PERCENT_RANK, CUME_DIST
- Ví dụ 1: Running total doanh thu + moving average 7 ngày
- Ví dụ 2: Xếp hạng sản phẩm trong từng danh mục (RANK vs DENSE_RANK vs ROW_NUMBER)
- Ví dụ 3: So sánh với kỳ trước (LAG), dự đoán xu hướng (LEAD)
- Ví dụ 4: Phân vị retention (PERCENT_RANK) — dùng thực tế ở DE
- Ví dụ 5: Top 3 sản phẩm bán chạy nhất mỗi tháng (window + filter)
- Info box tip: "5 hàm phỏng vấn hay hỏi nhất: ROW_NUMBER, RANK, LAG, LEAD, SUM OVER"
- Code blocks đầy đủ SQL chạy được trên PostgreSQL
- Quiz 6 câu: frame specification, RANK vs ROW_NUMBER, LAG vs LEAD, partition
- Practice: 3 bài tập với dataset orders — solution ẩn

[W1.03] GROUPING SETS, ROLLUP, CUBE
- Vấn đề: phân tích đa chiều cần nhiều GROUP BY → UNION ALL → chậm và dài
- GROUPING SETS: chỉ định chính xác từng tổ hợp grouping
- ROLLUP: subtotal theo hierarchy (năm → quý → tháng → ngày)
- CUBE: tất cả tổ hợp (dùng cho cross-dimensional analysis)
- Hàm GROUPING(): phân biệt NULL từ grouping với NULL từ data
- Use case thực tế:
  - Sales report: tổng theo (store, category), (store), (category), tổng toàn bộ
  - User activity: pivot theo platform + action type
- Code block: ví dụ đầy đủ với GROUPING SETS → ROLLUP → CUBE cho cùng 1 dataset
- So sánh output khi dùng UNION ALL vs GROUPING SETS (số dòng scan)
- Quiz 10 câu: khi nào dùng ROLLUP vs CUBE, GROUPING() function
- Practice: 2 bài tập phân tích đa chiều

[W1.04] Slowly Changing Dimensions (SCD)
- Tại sao cần SCD: dữ liệu thực tế thay đổi theo thời gian (khách hàng đổi địa chỉ, giá thay đổi)
- SCD Type 1: ghi đè (overwrite) — khi nào dùng, ưu nhược điểm
- SCD Type 2: thêm row mới với effective_from, effective_to, is_current — phổ biến nhất
  - DDL mẫu cho dim_customer SCD2
  - INSERT cho record mới (chưa có trong DWH)
  - UPDATE record cũ: đóng effective_to, set is_current = false
  - INSERT record mới: effective_from = today, effective_to = '9999-12-31'
  - MERGE statement tổng hợp (PostgreSQL dùng INSERT ON CONFLICT)
- SCD Type 3: thêm cột previous_value — khi nào phù hợp
- Validation sau khi chạy SCD2:
  - Không có chồng lấn date range cùng 1 customer_id
  - Mỗi customer có đúng 1 is_current = true
  - COUNT(*) không giảm sau incremental
- Code blocks đầy đủ SQL cho từng SCD type trên PostgreSQL
- Info box warn: "SCD Type 2 sai date range là lỗi production nghiêm trọng — luôn validate"
- Quiz 6 câu: SCD type selection, validation, effective_to logic
- Practice: Implement SCD2 cho bảng dim_product với dataset mẫu

[W1.05] Incremental Load Patterns
- Full load vs Incremental: khi nào dùng gì
- Yêu cầu của incremental: cột watermark (updated_at, created_at, event_date)
- 3 pattern phổ biến:
  1. Timestamp-based: WHERE updated_at > last_load_timestamp
  2. Date partition: WHERE event_date = :target_date (idempotent)
  3. CDC-based: chỉ load Changed rows từ source system
- Idempotency: pipeline chạy nhiều lần = cùng kết quả
  - Dùng MERGE / UPSERT thay INSERT
  - Dùng partition overwrite cho big data
  - Test bằng cách chạy 2 lần, đếm rows phải giống nhau
- Pattern backfill vs incremental:
  - Backfill: chạy 1 lần cho toàn bộ lịch sử
  - Incremental: chạy mỗi ngày cho dữ liệu mới
- Script mẫu: stored procedure tự lấy max(updated_at) và load incremental
- Script mẫu: idempotent daily partition load
- Info box tip: "Luôn test idempotency trước khi deploy production"
- Quiz 6 câu: watermark column, idempotency, backfill vs incremental
- Practice: Viết incremental load script cho bảng orders, test chạy 2 lần

[W1.06] Query Optimization & EXPLAIN
- Khi nào cần optimize: query > 1 giây là có vấn đề trong OLTP; > 10 giây trong OLAP
- EXPLAIN: đọc query plan (Seq Scan vs Index Scan, Hash Join vs Nested Loop)
- EXPLAIN ANALYZE: chạy thật và đo thời gian từng bước
- Các nguyên nhân query chậm thường gặp:
  - Full table scan do thiếu index
  - N+1 query pattern
  - Implicit type casting phá vỡ index
  - OR condition không dùng được index
  - SELECT * khi chỉ cần vài cột
- Index strategies cho DE:
  - B-tree index: equality + range
  - Partial index: WHERE is_active = true
  - Composite index: thứ tự cột quan trọng
  - Expression index: index trên function result
- Partition pruning: truy vấn chỉ scan partition cần thiết
- Ví dụ: query chậm (Seq Scan 2M rows) → thêm index → Index Scan nhanh hơn 100x
- Before/after EXPLAIN ANALYZE output với annotation giải thích từng dòng
- Quiz 10 câu: đọc EXPLAIN output, index selection, Seq Scan vs Index Scan
- Practice: Tối ưu 2 query chậm cho trước bằng EXPLAIN ANALYZE

[W1.07] Artifact: week1_sql_advanced.sql
- Tổng kết toàn bộ kiến thức tuần 1 thành 1 file SQL có thể commit
- File SQL cần có 11 queries có comment đầy đủ:
  01_running_total.sql        — window: running total + moving avg 7 ngày
  02_rank_in_category.sql     — window: top 3 per category
  03_lag_lead_compare.sql     — window: so sánh với kỳ trước
  04_retention_percentile.sql — window: PERCENT_RANK cho retention
  05_consecutive_active.sql   — window: streak analysis
  06_grouping_sets.sql        — grouping sets đa chiều
  07_rollup_sales.sql         — rollup hierarchy report
  08_scd_type1.sql            — SCD Type 1 implementation
  09_scd_type2.sql            — SCD Type 2 full implementation + validation
  10_incremental_load.sql     — idempotent incremental load
  11_explain_optimize.sql     — EXPLAIN ANALYZE before/after
- Hướng dẫn commit: git add, git commit -m "feat: week01 sql advanced artifact"
- README template cho thư mục week01:
  # Week 01 – SQL Advanced
  ## Mục tiêu
  ## Dataset dùng
  ## Kết quả từng query
  ## Bài học rút ra
- Info box tip: "Đây là file portfolio đầu tiên — viết comment rõ ràng như cho người khác đọc"

[W1.08] Mini Test Tổng Kết
- 20 câu bao phủ toàn bộ tuần 1:
  - Window functions: 6 câu
  - GROUPING SETS/ROLLUP/CUBE: 3 câu
  - SCD: 4 câu
  - Incremental load: 4 câu
  - EXPLAIN/optimization: 3 câu
- Thang điểm:
  < 12: Ôn lại W1.02-W1.05 trước khi sang tuần 2
  12-15: Nắm nền tảng tốt, luyện thêm SCD và incremental
  16-18: Sẵn sàng sang tuần 2 - Python cho DE
  19-20: Xuất sắc, thử tự đặt thêm câu hỏi cho từng pattern

=== YÊU CẦU KỸ THUẬT ===
[Giữ nguyên phần YÊU CẦU KỸ THUẬT từ template Tuần 0 — áp dụng cho mọi tuần]
- Title tab: "DE Handbook · Tuần 1 · SQL Nâng Cao"
- File output: "Week01_SQL_Advanced.html"
```

---

### ── TUẦN 2: Python cho DE ──

```
Tên: Tuần 2 – Python cho Data Engineer
File: "Week02_Python_DE.html"

=== CÁC MODULE ===
W2.01 – Tổng Quan & Tại Sao Python
W2.02 – pandas cho Data Engineering
W2.03 – SQLAlchemy & Kết Nối Database
W2.04 – Gọi REST API & Xử Lý Response
W2.05 – Error Handling & Logging
W2.06 – Cấu Trúc ETL Script Production
W2.07 – Artifact: week2_python_etl/
W2.08 – Mini Test Tổng Kết

Nội dung module:
- W2.02: pd.read_csv/json/parquet, xử lý null (dropna, fillna), merge/join, groupby, agg,
  to_sql, đọc nhiều file cùng lúc (glob), xử lý dtype, memory efficient reading
- W2.03: create_engine, execute query, read_sql_query, to_sql (append/replace/fail),
  connection pooling, context manager, parameterized query để chống SQL injection
- W2.04: requests.get/post, pagination pattern (next_page_token, page number),
  rate limit handling (time.sleep, retry với exponential backoff), parse JSON response,
  auth header (Bearer token, API key)
- W2.05: try/except/finally, custom exceptions, logging levels (DEBUG/INFO/WARNING/ERROR),
  structured logging (JSON format), log rotation, decorator cho retry pattern
- W2.06: class-based ETL với extract/transform/load methods, config từ .env,
  argparse cho CLI, __main__ guard, type hints, docstrings
- Artifact: 4 files Python + README, có thể chạy ngay: python pipeline.py --date 2024-01-01
```

---

### ── TUẦN 3: Data Cleaning ──

```
Tên: Tuần 3 – Data Cleaning & Quality
File: "Week03_Data_Cleaning.html"

=== CÁC MODULE ===
W3.01 – Tổng Quan & Tidy Data Principles
W3.02 – Data Profiling: Hiểu Data Trước Khi Làm
W3.03 – Xử Lý Missing Values
W3.04 – Deduplication Strategies
W3.05 – Outlier Detection & Treatment
W3.06 – Schema Validation với pandera
W3.07 – Artifact: week3_data_cleaning/
W3.08 – Mini Test Tổng Kết

Dựa trên: data_cleaning.md trong repo + Tidy Data whitepaper của Hadley Wickham
```

---

### ── TUẦN 4: Tư Duy Pipeline ──

```
Tên: Tuần 4 – Pipeline Design & Tư Duy DE
File: "Week04_Pipeline_Design.html"

=== CÁC MODULE ===
W4.01 – Tổng Quan & Pipeline là gì
W4.02 – DAG: Directed Acyclic Graph
W4.03 – Idempotency & Reliability
W4.04 – Failure Handling & Retry Patterns
W4.05 – Monitoring & Data Contracts
W4.06 – SLA, SLO, SLI cho Data Pipeline
W4.07 – Artifact: week4_pipeline_design.md
W4.08 – Mini Test Tổng Kết
```

---

### ── TUẦN 5-6: Dimensional Data Modeling ──

```
Tên: Tuần 5-6 – Dimensional Data Modeling
File: "Week05_Dimensional_Modeling.html"

=== CÁC MODULE ===
W5.01 – Tổng Quan & Kimball Methodology
W5.02 – Grain: Nền Tảng Của Mọi Model
W5.03 – Dimension Tables (SCD1/2/3)
W5.04 – Fact Tables (Transaction/Snapshot/Accumulating)
W5.05 – Star Schema vs Snowflake Schema
W5.06 – Cumulative Table Design (design pattern repo)
W5.07 – Backfill Strategy
W5.08 – Homework: actors + actors_history_scd
W5.09 – Mini Test Tổng Kết

Dựa trên: intermediate-bootcamp/materials/1-dimensional-data-modeling/
Homework từ: homework/homework.md trong repo
```

---

### ── TUẦN 7: Fact Data Modeling ──

```
Tên: Tuần 7 – Fact Data Modeling
File: "Week07_Fact_Modeling.html"

=== CÁC MODULE ===
W7.01 – Tổng Quan Fact Tables
W7.02 – Transaction Fact vs Periodic Snapshot vs Accumulating
W7.03 – Deduplication: ROW_NUMBER + Microbatch Pattern
W7.04 – Reduced Fact Tables (Compressed/Array format)
W7.05 – Incremental Load cho Fact Tables (MERGE/UPSERT)
W7.06 – Homework: user_devices + hosts + host_activity_reduced
W7.07 – Mini Test Tổng Kết

Dựa trên: intermediate-bootcamp/materials/2-fact-data-modeling/
Link repo: https://github.com/EcZachly/microbatch-hourly-deduped-tutorial
```

---

### ── TUẦN 8-9: dbt ──

```
Tên: Tuần 8-9 – dbt: Data Build Tool
File: "Week08_dbt.html"

=== CÁC MODULE ===
W8.01 – dbt là gì & ELT vs ETL
W8.02 – Project Structure & Configuration
W8.03 – Models: view / table / incremental / ephemeral
W8.04 – ref() và source(): Dependency Management
W8.05 – Built-in Tests & Custom Tests
W8.06 – Documentation với schema.yml
W8.07 – Snapshots: SCD2 bằng dbt
W8.08 – Macros & DRY Principle
W8.09 – dbt Commands Cheat Sheet
W8.10 – Artifact: dbt_project/ hoàn chỉnh
W8.11 – Mini Test Tổng Kết

Nguồn: https://learn.getdbt.com + dbt docs chính thức
```

---

### ── TUẦN 10-11: Apache Airflow ──

```
Tên: Tuần 10-11 – Apache Airflow: Orchestration
File: "Week10_Airflow.html"

=== CÁC MODULE ===
W10.01 – Airflow Architecture (Scheduler/Executor/Webserver)
W10.02 – DAG: Định Nghĩa & Schedule
W10.03 – Core Operators (Python/Bash/SQL)
W10.04 – Task Dependencies & XCom
W10.05 – Variables, Connections & Secrets
W10.06 – Sensors & ExternalTaskSensor
W10.07 – Dynamic DAGs từ Config
W10.08 – Tích Hợp dbt + Airflow
W10.09 – Retry, Timeout & SLA Miss
W10.10 – Artifact: airflow_dags/ hoàn chỉnh
W10.11 – Mini Test Tổng Kết
```

---

## 📌 QUY TẮC CHUNG CHO MỌI TUẦN

Khi dùng prompt bất kỳ tuần nào, Claude phải:

1. **KHÔNG dùng placeholder** như "// thêm nội dung tương tự" hay "..."
   → Viết đầy đủ mọi section, mọi quiz, mọi code block

2. **Mỗi code block phải chạy được thực tế**
   → Test mentally trước khi viết — SQL phải valid PostgreSQL, Oraclesql, Python phải valid syntax

3. **Mỗi quiz phải có đúng 4 đáp án với giải thích riêng cho từng đáp án**
   → Kể cả đáp án sai cũng phải giải thích tại sao sai

4. **Code syntax highlight dùng đúng class**
   → `<span class="prompt">$</span>` cho prompt
   → `<span class="comment">-- comment</span>` cho SQL comments
   → `<span class="output">output text</span>` cho output

5. **Mỗi section 5 (Tổng Kết) phải có đúng 6 ô summary-grid**
   → Tóm tắt 6 điểm cốt lõi nhất của module

6. **File cuối cùng phải < 500KB**
   → Nếu nội dung quá dài, chia thành Part A và Part B

7. **Không có lỗi JavaScript**
   → gradeFinalTest() phải reference đúng id="final-test"
   → Số module trong JS phải khớp với số module HTML

## SQL Comparison UI (MANDATORY)

Whenever a lesson compares PostgreSQL and Oracle SQL:

DO NOT write:

-- PostgreSQL
SELECT ...

-- Oracle SQL
SELECT ...

INSTEAD render interactive tabs:

[PostgreSQL] [Oracle SQL]

Behavior:
- Default active: PostgreSQL
- Clicking tab shows matching code block
- Hide inactive block
- Reusable component
- Multiple SQL tab groups can exist in one page

Required HTML pattern:

<div class="sql-tabs">
  <button class="sql-tab active">PostgreSQL</button>
  <button class="sql-tab">Oracle SQL</button>
</div>

<div class="sql-panel active">...</div>
<div class="sql-panel">...</div>   

---

## 🗂️ DANH SÁCH ĐẦY ĐỦ CÁC FILE CẦN BUILD

| File | Tuần | Giai đoạn | Ưu tiên |
|------|------|-----------|---------|
| Week00_Setup.html | 0 | 0 | ⭐⭐⭐ Làm trước |
| Week01_SQL_Advanced.html | 1 | 1 | ⭐⭐⭐ |
| Week02_Python_DE.html | 2 | 1 | ⭐⭐⭐ |
| Week03_Data_Cleaning.html | 3 | 1 | ⭐⭐ |
| Week04_Pipeline_Design.html | 4 | 1 | ⭐⭐ |
| Week05_Dimensional_Modeling.html | 5-6 | 2 | ⭐⭐⭐ |
| Week07_Fact_Modeling.html | 7 | 2 | ⭐⭐⭐ |
| Week08_dbt.html | 8-9 | 2 | ⭐⭐⭐ |
| Week10_Airflow.html | 10-11 | 2 | ⭐⭐⭐ |
| Week12_Data_Quality.html | 12 | 2 | ⭐⭐ |
| Week13_Cloud_AWS.html | 13 | 3 | ⭐⭐⭐ |
| Week14_Data_Warehouse.html | 14 | 3 | ⭐⭐⭐ |
| Week15_Data_Integration.html | 15 | 3 | ⭐⭐ |
| Week16_Spark.html | 16-17 | 3 | ⭐⭐⭐ |
| Week18_Flink_Kafka.html | 18-19 | 4 | ⭐⭐ |
| Week20_Modern_OLAP.html | 20 | 4 | ⭐⭐ |
| Week21_Analytical_Patterns.html | 21 | 4 | ⭐⭐⭐ |
| Week22_KPI_Dashboard.html | 22 | 4 | ⭐⭐ |
| Week23_Maintenance.html | 23 | 5 | ⭐⭐ |
| Week24_Capstone.html | 24-27 | 6 | ⭐⭐⭐ |

**Thứ tự build đề xuất:** 00 → 01 → 02 → 05 → 08 → 10 → 16 → còn lại

---

## 💡 MẸO SỬ DỤNG PROMPT HIỆU QUẢ

**Nếu file quá dài (> 500KB):**
```
Xây dựng Week01_SQL_Advanced_Part1.html với các module W1.01 đến W1.04.
(Áp dụng toàn bộ format chuẩn phía trên)
```

**Nếu muốn bổ sung nội dung vào file có sẵn:**
```
Trong file Week01_SQL_Advanced.html, hãy bổ sung module W1.09 về
Recursive CTE với nội dung sau: [mô tả nội dung]
Giữ nguyên tất cả modules khác, chỉ thêm vào nav sidebar và cuối danh sách modules.
```

**Nếu muốn thêm quiz vào module có sẵn:**
```
Thêm 3 quiz items vào Section 4 của module W1.02 trong file Week01.html.
Chủ đề: frame specification (ROWS BETWEEN vs RANGE BETWEEN).
Format quiz đúng chuẩn answerQuiz() với 4 đáp án và explanation đầy đủ.
```
