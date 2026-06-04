# Bối cảnh Cuộc trò chuyện: Lộ trình học Data Engineering & Khởi tạo dự án

**Ngày cập nhật:** 2026-06-04 (Theo giờ local)
**Mục tiêu:** Lưu trữ context cuộc trò chuyện để đồng bộ và tiếp tục học tập/thảo luận trên thiết bị khác (ví dụ: máy tính ở công ty).

---

## 1. TỔNG QUAN VỀ DỰ ÁN DE-LEARNING

Thư mục `DE-Learning` là thư viện tài nguyên gốc, đóng vai trò làm cẩm nang hướng dẫn học tập:
- **Interactive HTML Handbooks:** Các file bài học theo tuần `Week00` đến `Week24` chứa lý thuyết, code walkthrough, lỗi thường gặp, quiz và bài tập.
- **DE Mastery Dashboard (`DE_Mastery_Dashboard.html`):** Dashboard quản lý tiến độ, checklist công việc hàng ngày, đo lường kỹ năng (Notion-style).
- **Phần chuẩn bị phỏng vấn (`interview-prep/`):** Chứa cẩm nang phỏng vấn thiết kế riêng cho Data Architect/Database Specialist/Data Engineer và bộ 100 câu hỏi tuyển dụng.

---

## 2. CÁC LỘ TRÌNH HỌC TẬP ĐỀ XUẤT

Tùy vào thời gian và mục tiêu, có 3 lộ trình chính được rút ra từ các tài liệu có sẵn trong repo:
1.  **Lộ trình Expert (24-28 tuần ~ 6-9 tháng):** Lộ trình toàn diện dựa trên file `DE_Roadmap_Expert_NHC.md` cho người đi làm (12-15h/tuần).
2.  **Lộ trình Deep Study (32 tuần ~ 8 tháng):** Đi sâu chi tiết từng công cụ dựa trên `Senior_DE_2026_Weekly_Checklist.csv`.
3.  **Lộ trình Cấp tốc Phỏng vấn (16 tuần ~ 4 tháng):** Rút gọn, tập trung vào lý thuyết trọng tâm và luyện câu hỏi phỏng vấn dựa trên `DE_Interview_Prep_16Weeks_Checklist.csv`.

---

## 3. CƠ CẤU WORKSPACE VÀ PROJECT THỰC HÀNH MỚI

Để tiện quản lý và đồng bộ (chỉ cần dùng một repository Git duy nhất), thư mục làm bài tập đã được chuyển vào nằm trong repository tài liệu gốc `DE-Learning`:
- **Đường dẫn local:** `d:\TaiLieu\Data Engineer\DE Roadmap\DE-Learning\de-roadmap-artifacts`
- **Trạng thái:** Đã tích hợp trực tiếp vào Git của `DE-Learning`, cấu hình `.gitignore` chuẩn, tạo tệp `README.md` giới thiệu chung và cấu trúc sẵn các thư mục con:
  - `week01_sql_advanced/`
  - `week02_python_etl/`
  - `week03_data_cleaning/`
  - `week04_pipeline_design/`
  - `week05_dimensional_modeling/`
  - `week07_fact_modeling/`
  - `dbt_project/`
  - `airflow_dags/`
  - `capstone_project/`

---

## 🔄 4. QUY TRÌNH HỌC TẬP HÀNG TUẦN (WORKFLOW)

Khi bắt đầu học bất kỳ tuần (Week) nào, thực hiện theo 6 bước:
1.  **Đọc tài liệu:** Kéo thả file `WeekXX_*.html` từ thư mục `DE-Learning` vào trình duyệt để học lý thuyết.
2.  **Xem đề bài:** Cuộn xuống cuối file HTML để xem phần bài tập thực hành (Practice Task).
3.  **Viết code:** Truy cập vào thư mục `de-roadmap-artifacts` bên trong `DE-Learning`, viết code giải bài tập trong folder tuần tương ứng.
4.  **Tối ưu bằng AI:** Copy đề bài và code của bạn gửi cho Claude AI để nhờ review/tối ưu hóa theo tiêu chuẩn Senior DE.
5.  **Push GitHub:** `git add`, `git commit` và `git push` để lưu trữ bài tập lên GitHub (chung repository `DE-Learning`).
6.  **Đánh dấu tiến độ:** Tích hoàn thành các công việc trên `DE_Mastery_Dashboard.html` để cập nhật tiến trình học tập.

---

## 🚀 5. HÀNG ĐỘNG TIẾP THEO (KHI SANG MÁY KHÁC)

Khi chuyển sang máy tính khác (ở công ty), bạn hãy thực hiện các bước sau để đồng bộ:
1.  **Đồng bộ toàn bộ:** `git pull` tại thư mục `DE-Learning` trên máy tính ở công ty. Bạn sẽ nhận được cả tài liệu học tập mới, file bối cảnh này và toàn bộ code bài tập đã làm.
2.  **Bắt đầu học:** Mở file [Week00_Setup.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week00_Setup.html) hoặc [Week01_SQL_Advanced.html](file:///d:/TaiLieu/Data%20Engineer/DE%20Roadmap/DE-Learning/Week01_SQL_Advanced.html) để thực hành.
