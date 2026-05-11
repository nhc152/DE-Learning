# Cấu Trúc Chi Tiết Đầy Đủ — Data Engineer Handbook

## 1) Mục tiêu thư mục
Thư mục `data-engineer-handbook` được tổ chức theo lộ trình học Data Engineering từ cơ bản đến nâng cao, kết hợp:
- kiến thức nền tảng,
- bootcamp thực hành,
- tài nguyên tham khảo,
- dự án portfolio.

---

## 2) Cấu trúc tổng thể đề xuất

```text
data-engineer-handbook/
├── README.md
├── README.html
├── .gitignore
├── books.md
├── communities.md
├── newsletters.md
├── interviews.md
├── projects.md
├── data_cleaning.md
├── read_this_for_application_fundamentals_for_python
│
├── beginner-bootcamp/
│   ├── README.md
│   ├── Week01_*.html
│   ├── Week02_*.html
│   ├── Week03_*.html
│   ├── Week04_*.html
│   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── datasets/
│   └── exercises/
│       ├── week01/
│       ├── week02/
│       ├── week03/
│       └── week04/
│
├── intermediate-bootcamp/
│   ├── README.md
│   ├── Week05_*.html
│   ├── Week06_*.html
│   ├── Week07_*.html
│   ├── Week08_*.html
│   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── datasets/
│   └── labs/
│       ├── week05/
│       ├── week06/
│       ├── week07/
│       └── week08/
│
├── advanced-bootcamp/
│   ├── README.md
│   ├── Week09_*.html
│   ├── Week10_*.html
│   ├── Week11_*.html
│   ├── Week12_*.html
│   ├── capstone/
│   │   ├── requirements.md
│   │   ├── architecture.md
│   │   ├── implementation.md
│   │   └── evaluation.md
│   └── assets/
│       ├── css/
│       ├── js/
│       ├── images/
│       └── datasets/
│
├── templates/
│   ├── week_template.html
│   ├── module_template.md
│   ├── quiz_template.json
│   └── project_template.md
│
├── references/
│   ├── glossary.md
│   ├── cheat_sheets/
│   │   ├── python.md
│   │   ├── sql.md
│   │   ├── pandas.md
│   │   └── airflow.md
│   └── architecture_patterns.md
│
├── datasets/
│   ├── raw/
│   ├── cleaned/
│   ├── sample/
│   └── README.md
│
└── portfolio-projects/
    ├── README.md
    ├── project-01-ingestion-pipeline/
    ├── project-02-batch-warehouse/
    ├── project-03-streaming-analytics/
    └── project-04-end-to-end-platform/
```

---

## 3) Ý nghĩa từng nhóm thư mục/tệp chính

### Root files
- `README.md`, `README.html`: trang vào chính, mô tả lộ trình học và cách sử dụng handbook.
- `books.md`, `communities.md`, `newsletters.md`: tài nguyên cập nhật dài hạn.
- `interviews.md`: bộ câu hỏi ôn tập/chuẩn bị phỏng vấn.
- `projects.md`: danh sách dự án theo cấp độ.
- `data_cleaning.md`: chuẩn làm sạch dữ liệu thực chiến.

### Bootcamp levels
- `beginner-bootcamp/`: cho người mới, tập trung nền tảng Python/SQL/ETL cơ bản.
- `intermediate-bootcamp/`: tăng độ khó với workflow, orchestration, data quality.
- `advanced-bootcamp/`: kiến trúc hệ thống, tối ưu hiệu năng, capstone hoàn chỉnh.

### Shared resources
- `templates/`: chuẩn hóa layout, quiz, project brief để giữ UX nhất quán.
- `references/`: glossary, cheat sheet, pattern kiến trúc.
- `datasets/`: dữ liệu dùng chung cho toàn bộ bài học.
- `portfolio-projects/`: dự án tích lũy để showcase năng lực.

---

## 4) Chuẩn đặt tên khuyến nghị

### File tuần học
- `Week01_Foundations.html`
- `Week02_Python_for_Data_Engineering.html`
- `Week03_SQL_and_Data_Modeling.html`

Quy tắc:
1. Luôn bắt đầu bằng `WeekXX_` (2 chữ số).
2. Dùng `_` thay khoảng trắng.
3. Tên phần sau ngắn gọn, phản ánh đúng chủ đề.

### Tài nguyên phụ trợ
- Datasets: `sales_2026_q1.csv`, `users_dim.parquet`
- Labs: `lab_week05_incremental_load.md`
- Assets ảnh: `week03_pipeline_diagram.png`

---

## 5) Khung nội dung chuẩn cho mỗi file WeekXX_*.html
Mỗi bài học nên có tối thiểu các phần:
1. Learning Objectives
2. Concept đơn giản trước, chuyên sâu sau
3. Demo dữ liệu thực tế
4. Code walkthrough từng bước
5. Common mistakes
6. Mini quiz
7. Practice task
8. Tóm tắt + hướng học tiếp

---

## 6) Lộ trình phát triển nội dung (gợi ý)
- Giai đoạn 1: Hoàn chỉnh Beginner (Week01–Week04).
- Giai đoạn 2: Hoàn chỉnh Intermediate (Week05–Week08).
- Giai đoạn 3: Xây Advanced + Capstone (Week09–Week12).
- Giai đoạn 4: Chuẩn hóa template + bổ sung portfolio projects.
- Giai đoạn 5: Tối ưu trải nghiệm học (quiz, feedback, scoring nhất quán).

---

## 7) Checklist chất lượng trước khi thêm bài mới
- [ ] Đúng chuẩn tên `WeekXX_*.html`
- [ ] Nội dung theo thứ tự từ dễ đến khó
- [ ] Có ví dụ thực tế Data Engineering
- [ ] Có quiz + bài tập thực hành
- [ ] UI/UX đồng bộ với các tuần khác
- [ ] Không trùng lặp nội dung đã có
- [ ] Có tài nguyên tham khảo cuối bài

---

## 8) Trạng thái hiện tại (theo thư mục đang có)
Đang có:
- `beginner-bootcamp/`
- `intermediate-bootcamp/`
- bộ tài nguyên nền (`books.md`, `communities.md`, `newsletters.md`, `projects.md`, `interviews.md`...)

Nên bổ sung tiếp theo:
- `advanced-bootcamp/`
- `templates/`
- `references/`
- `datasets/`
- `portfolio-projects/`

---

## 9) Ghi chú vận hành
- Ưu tiên chất lượng từng tuần hơn mở rộng số lượng nhanh.
- Tái sử dụng template để giữ “same tutorial family feeling”.
- Mỗi tuần nên có “sản phẩm nhỏ” để học viên thấy tiến bộ rõ ràng.
