# Output Standard

## Language

Use Vietnamese for explanations.

Keep English technical terms when standard, such as:

* PostgreSQL
* Oracle SQL
* Python
* Airflow
* Spark
* Kafka
* dbt
* Terraform
* AWS IAM
* API
* ETL / ELT

UI labels should remain Vietnamese.

---

## Writing Style

Tone:

* mentor-like
* clear
* calm
* practical
* confident

Sentence Style:

Prefer:

* clear sentences
* moderate length
* explicit logic
* concrete wording
* practical phrasing

Avoid:

* robotic wording
* vague explanations
* overly long paragraphs
* unnecessary buzzwords
* unnatural translated phrasing

---

## Teaching Style

Prefer:

* explain simply first
* then deepen gradually
* explain why before how when useful
* compare alternatives
* show trade-offs
* include common mistakes
* connect to real-world scenarios

Avoid:

* dry textbook definitions
* theory without application
* jumping between ideas
* overcomplicated language

---

## SQL Policy

Where relevant, include both:

* PostgreSQL
* Oracle SQL

When syntax differs:

* present both versions clearly
* explain the difference briefly in Vietnamese
* do not force Oracle examples where topic is purely Python-only
* include SQL where relevant to Data Engineering workflows

When showing SQL examples with multiple databases:

Always render as tab buttons:

* PostgreSQL
* Oracle SQL

Never output plain text headings like:

* PostgreSQL
* Oracle SQL

---

## HTML Standard

Every Week file should be standalone HTML with inline CSS/JS unless user asks otherwise.

Expected UI:

* Hero banner
* Badge row
* Sidebar navigation
* Main content modules
* Responsive layout
* Dark premium style

---

## Module Standard

Each module should contain these 6 sections in order:

1. Menu Tổng Thể
2. Mục Đích Module
3. Giải Thích Chi Tiết
4. Câu Hỏi Ôn Tập
5. Tổng Kết
6. Bài Tập Thực Hành

---

## Section Expectations

### Menu Tổng Thể

* short orientation
* learning roadmap
* key topics preview

### Mục Đích Module

* clear outcomes
* what learner can do after module

### Giải Thích Chi Tiết

* practical explanation first
* then examples
* then syntax/code
* then notes/tips/warnings

### Câu Hỏi Ôn Tập

* practical questions
* not trivial memory checks
* explanations should teach

### Tổng Kết

* concise recap
* memorable key takeaways

### Bài Tập Thực Hành

* realistic
* achievable
* useful for career growth

---

## Interaction Standard

Preserve or implement when relevant:

* showModule()
* goNext()
* goPrev()
* toggleSection()
* answerQuiz()
* toggleSolution()
* gradeFinalTest()
* resetFinalTest()

---

## Quiz Standard

When quizzes are requested:

* exactly 10 questions per module
* 4 options each
* explanations included
* practical and scenario-based

---

## Final Test Standard

When included:

* scoring works
* reset works
* meaningful questions

---

## UX Writing Standard

Use clear Vietnamese labels such as:

* Xem lời giải
* Module tiếp theo
* Quay lại
* Chấm điểm
* Làm lại
* Ẩn / Hiện nội dung

---

## Consistency Rule

Every Week file should feel like part of the same premium handbook family as Week00_Setup.html.
