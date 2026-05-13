import json
import re

html_path = r'D:\TaiLieu\Data Engineer\DE Roadmap\DE-Learning\interview-prep-html\DE_Interview_Handbook.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<script id="handbook-data" type="application/json">(.*?)</script>', content, re.DOTALL)
if not match:
    print("Could not find JSON")
    exit(1)

data = json.loads(match.group(1))
questions = data.get('questions', [])

# Replacements dictionary
replacements = {
    r'\bduoc\b': 'được',
    r'\bkhong\b': 'không',
    r'\bnao\b': 'nào',
    r'\bgi\b': 'gì',
    r'\bvao\b': 'vào',
    r'\bluu\b': 'lưu',
    r'\btruoc\b': 'trước',
    r'\bthe nao\b': 'thế nào',
    r'\bkhac\b': 'khác',
    r'\bcap nhat\b': 'cập nhật',
    r'\bcong ty\b': 'công ty',
    r'\bton\b': 'tốn',
    r'\bthoi diem\b': 'thời điểm',
    r'\bxu ly\b': 'xử lý',
    r'\btich hop\b': 'tích hợp',
    r'\bphan biet\b': 'phân biệt',
    r'\bhieu qua\b': 'hiệu quả',
    r'\bde hieu\b': 'dễ hiểu',
    r'\bde\b': 'để',
    r'\blap trinh\b': 'lập trình',
    r'\bnhieu\b': 'nhiều',
    r'\btang\b': 'tăng',
    r'\bcham\b': 'chậm',
    r'\bgiai quyet\b': 'giải quyết',
    r'\bgiam\b': 'giảm',
    r'\bchuan hoa\b': 'chuẩn hóa',
    r'\bthong nhat\b': 'thống nhất',
    r'\bhieu\b': 'hiểu',
    r'\bdung\b': 'dùng',  # correct context mostly
    r'\bvoi\b': 'với',
    r'\bban\b': 'bạn',
    r'\bdo\b': 'đo',
    r'\bnay\b': 'này',
    r'\btinh\b': 'tính',
    r'\bthanh\b': 'thành',
    r'\bphinh\b': 'phình',
    r'\bchot\b': 'chốt',
    r'\bmot\b': 'một',
    r'\bnhay thang\b': 'nhảy thẳng',
    r'\bcan\b': 'cần',
    r'\bbao ve\b': 'bảo vệ',
    r'\bbien doi\b': 'biến đổi',
    r'\bthu tu\b': 'thứ tự',
    r'\bthuc te\b': 'thực tế',
    r'\blam\b': 'làm',
    r'\bphuc tap\b': 'phức tạp',
    r'\bdam bao\b': 'đảm bảo',
    r'\btoi uu\b': 'tối ưu',
    r'\bnho\b': 'nhỏ',
    r'\blon\b': 'lớn',
    r'\bgom\b': 'gồm',
    r'\btach\b': 'tách',
    r'\bcach\b': 'cách',
    r'\blien tuc\b': 'liên tục',
    r'\bsang\b': 'sang',
    r'\bnhat quan\b': 'nhất quán',
    r'\bthuong\b': 'thường',
    r'\bthay doi\b': 'thay đổi',
    r'\bphat hien\b': 'phát hiện',
    r'\bbien\b': 'biến',
    r'\bdap ung\b': 'đáp ứng',
    r'\btruy xuat\b': 'truy xuất',
    r'\bdac biet\b': 'đặc biệt',
    r'\bcung cap\b': 'cung cấp',
    r'\byeu cau\b': 'yêu cầu',
    r'\bbo qua\b': 'bỏ qua',
    r'\btu dong\b': 'tự động',
    r'\bmuon\b': 'muộn',
    r'\brut ra\b': 'rút ra',
    r'\bloai bo\b': 'loại bỏ',
    r'\bquy tac\b': 'quy tắc',
    r'\blua chon\b': 'lựa chọn',
    r'\bsao chep\b': 'sao chép',
    r'\bo on\b': 'ổn'
}

def fix_spelling(text):
    if not text:
        return text
    for pattern, repl in replacements.items():
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    # Fix uppercase replacements preserving case
    text = text.replace('Đe', 'Để').replace('Ban', 'Bạn').replace('Khi nao', 'Khi nào').replace('Khong', 'Không').replace('Neu', 'Nếu').replace('Vay', 'Vậy')
    # some specific fixes
    text = text.replace('đúng', 'dùng') # heuristic fix for DB terms
    text = text.replace('dùng đúng', 'sử dụng')
    text = text.replace('tạo nên tăng', 'tạo nền tảng')
    return text

def split_tradeoffs_mistakes(raw_text):
    # raw_text often contains "Trade-off" or "Trade off"
    if 'Trade-off' in raw_text:
        parts = raw_text.split('Trade-off')
        return parts[0].strip(), 'Trade-off' + parts[1].strip()
    elif 'trade-off' in raw_text.lower():
        idx = raw_text.lower().find('trade-off')
        return raw_text[:idx].strip(), raw_text[idx:].strip()
    else:
        # split by first sentence
        sentences = raw_text.split('. ')
        if len(sentences) > 1:
            return sentences[0] + '.', '. '.join(sentences[1:])
        return raw_text, "Cần cân bằng giữa chi phí, tốc độ và độ phức tạp."

for q in questions:
    q['question'] = fix_spelling(q['question'])
    q['short'] = fix_spelling(q['short'])
    q['deep'] = fix_spelling(q['deep'])
    q['production'] = fix_spelling(q['production'])
    q['followups'] = fix_spelling(q['followups'])
    
    # Process tradeoffs/mistakes
    original_tradeoffs = q.get('tradeoffs', '')
    mistakes, tradeoffs = split_tradeoffs_mistakes(original_tradeoffs)
    q['mistakes'] = fix_spelling(mistakes)
    q['tradeoffs'] = fix_spelling(tradeoffs)

new_questions = [
    {
        "id": "080",
        "question": "How do you handle consumer lag in Kafka?",
        "category": "Kafka / Streaming",
        "moduleId": "m05",
        "difficulty": "Senior",
        "tags": "Kafka, lag, consumer",
        "raw": "",
        "short": "Consumer lag xảy ra khi producer gửi dữ liệu nhanh hơn mức consumer có thể xử lý. Cách xử lý bao gồm tăng số partition, tối ưu hóa logic của consumer, hoặc điều chỉnh cấu hình batching.",
        "deep": "Việc theo dõi lag là rất quan trọng để đảm bảo tính thời gian thực (real-time). Nếu lag tăng đột biến, hệ thống có thể bị mất dữ liệu do retention policy. Chúng ta cần đánh giá xem bottleneck nằm ở I/O hay CPU của consumer để scale up/out phù hợp.",
        "production": "Trong pipeline thanh toán, lag quá 5 phút sẽ gây ra alert P1. Chúng tôi xử lý bằng cách tự động scale thêm consumer instance dựa trên metric lag từ Prometheus.",
        "tradeoffs": "Tăng partition giúp tăng mức độ song song nhưng tốn thêm resource và chi phí ZooKeeper/KRaft. Tối ưu consumer có thể phức tạp hơn.",
        "mistakes": "Bỏ qua việc theo dõi lag và chỉ nhận ra vấn đề khi dữ liệu bị mất do hết hạn retention.",
        "followups": "Bạn sử dụng công cụ gì để monitor Kafka lag? Làm sao để xử lý poison pill message?",
        "codeBlocks": []
    },
    {
        "id": "081",
        "question": "Explain Exactly-Once semantics in stream processing.",
        "category": "Kafka / Streaming",
        "moduleId": "m05",
        "difficulty": "Senior",
        "tags": "exactly-once, Flink",
        "raw": "",
        "short": "Exactly-Once đảm bảo mỗi sự kiện được xử lý và có tác động đến trạng thái (state) đúng một lần, ngay cả khi có sự cố hệ thống.",
        "deep": "Trong Kafka, nó đạt được qua Idempotent Producer và Transactional API. Trong Flink, nó dùng cơ chế checkpointing dựa trên thuật toán Chandy-Lamport để lưu state nhất quán.",
        "production": "Khi tính phí giao dịch tài chính, việc tính đúp (at-least-once) là không thể chấp nhận. Chúng tôi dùng Kafka transactions kết hợp với Flink exactly-once sink vào Postgres.",
        "tradeoffs": "Exactly-once gây ra độ trễ (latency) cao hơn và tốn hiệu năng do overhead của transaction/checkpoint. Đôi khi at-least-once kết hợp với idempotent sink là đủ.",
        "mistakes": "Cố gắng sử dụng exactly-once cho mọi workload, kể cả khi hệ thống chỉ cần đếm lượt view (chấp nhận sai số nhỏ).",
        "followups": "Idempotent sink là gì? 2PC (Two-Phase Commit) hoạt động thế nào trong Flink?",
        "codeBlocks": []
    },
    {
        "id": "082",
        "question": "What is Schema Registry and why is it needed in Kafka?",
        "category": "Kafka / Streaming",
        "moduleId": "m05",
        "difficulty": "Intermediate",
        "tags": "schema, evolution",
        "raw": "",
        "short": "Schema Registry là trung tâm quản lý lược đồ dữ liệu (ví dụ Avro/Protobuf) cho Kafka, giúp đảm bảo producer và consumer luôn hiểu cùng một định dạng.",
        "deep": "Nó cung cấp khả năng kiểm tra tính tương thích (backward/forward compatibility) khi schema thay đổi, ngăn chặn producer gửi dữ liệu sai định dạng làm sập consumer (poison pill).",
        "production": "Team Backend thêm cột `age` vào user_event. Schema Registry từ chối schema mới nếu nó phá vỡ tính backward compatibility, bảo vệ pipeline Data Warehouse đang đọc topic đó.",
        "tradeoffs": "Tạo thêm một điểm phụ thuộc (SPOF) trong hệ thống nếu không được HA. Đổi lại, dữ liệu được validate ngay từ nguồn và tiết kiệm băng thông do data serialization.",
        "mistakes": "Sử dụng JSON plain text trong Kafka, dẫn đến lỗi schema drift âm thầm phá hỏng downstream pipelines.",
        "followups": "Backward compatibility trong Avro nghĩa là gì? Nếu Schema Registry sập thì Kafka có hoạt động không?",
        "codeBlocks": []
    },
    {
        "id": "083",
        "question": "Describe different windowing strategies in stream processing.",
        "category": "Kafka / Streaming",
        "moduleId": "m05",
        "difficulty": "Intermediate",
        "tags": "window, Flink",
        "raw": "",
        "short": "Có 3 loại chính: Tumbling (cửa sổ cố định, không chồng lấp), Hopping/Sliding (cửa sổ trượt, có chồng lấp), và Session (cửa sổ dựa trên thời gian không hoạt động).",
        "deep": "Việc chọn cửa sổ phụ thuộc vào business logic. Tumbling tốt cho báo cáo định kỳ (vd: doanh thu theo giờ). Sliding tốt cho alert (vd: đếm lỗi trong 5 phút qua, cập nhật mỗi phút). Session tốt cho phân tích hành vi người dùng.",
        "production": "Để tính thời gian trung bình của một phiên người dùng trên app, chúng tôi dùng Session window với khoảng gap là 30 phút.",
        "tradeoffs": "Sliding window tiêu tốn nhiều RAM/State hơn vì một event có thể thuộc nhiều cửa sổ cùng lúc. Session window phức tạp trong việc xử lý late data.",
        "mistakes": "Sử dụng processing time thay vì event time cho windowing, dẫn đến kết quả sai lệch khi hệ thống có độ trễ.",
        "followups": "Event time và Processing time khác nhau thế nào? Làm sao xử lý dữ liệu đến muộn (late data)?",
        "codeBlocks": []
    },
    {
        "id": "084",
        "question": "How do you handle late-arriving data in streaming?",
        "category": "Kafka / Streaming",
        "moduleId": "m05",
        "difficulty": "Senior",
        "tags": "late data, watermark",
        "raw": "",
        "short": "Xử lý dữ liệu đến muộn (late data) thường sử dụng cơ chế Watermarks để hệ thống biết khi nào có thể đóng cửa sổ (window), kết hợp với Allowed Lateness để chấp nhận update sau đó.",
        "deep": "Watermark là một timestamp khai báo rằng 'sẽ không có event nào cũ hơn thời gian này tới nữa'. Allowed Lateness cho phép lưu lại state của cửa sổ một thời gian sau khi watermark đi qua để gộp thêm late events.",
        "production": "App di động gửi event offline khi có mạng lại. Flink pipeline dùng watermark trễ 5 phút, và allowed lateness 24 giờ để cập nhật lại kết quả vào bảng thay vì bỏ qua event.",
        "tradeoffs": "Allowed Lateness càng lớn thì tốn càng nhiều bộ nhớ để giữ state của các cửa sổ cũ. Nếu watermark quá chặt, sẽ rớt nhiều dữ liệu.",
        "mistakes": "Đóng cửa sổ ngay lập tức dựa trên processing time, làm mất hoàn toàn dữ liệu từ các thiết bị có kết nối mạng kém.",
        "followups": "Điều gì xảy ra nếu một event đến sau cả Allowed Lateness? Side output là gì?",
        "codeBlocks": []
    },
    {
        "id": "085",
        "question": "What are Kafka retention policies and compacted topics?",
        "category": "Kafka / Streaming",
        "moduleId": "m05",
        "difficulty": "Intermediate",
        "tags": "retention, compaction",
        "raw": "",
        "short": "Retention policy quyết định Kafka giữ dữ liệu trong bao lâu (theo thời gian hoặc dung lượng). Compacted topics là chế độ chỉ giữ lại giá trị (value) mới nhất cho mỗi khóa (key).",
        "deep": "Compaction rất hữu ích để giữ state hiện tại (vd: số dư tài khoản mới nhất của user) thay vì lưu toàn bộ lịch sử thay đổi từ lúc tạo hệ thống. Quá trình compaction diễn ra ở background.",
        "production": "Bảng `dim_users` được đồng bộ từ MySQL qua Debezium vào một compacted topic trong Kafka. Khi một dịch vụ mới bật lên, nó chỉ cần đọc topic này để lấy được state hiện hành nhanh nhất.",
        "tradeoffs": "Compaction tiêu tốn CPU/Disk I/O của broker. Nó không phù hợp nếu bạn cần phân tích hành vi lịch sử (time-series).",
        "mistakes": "Dùng topic thường cho bảng cấu hình (config), khiến topic phình to vô hạn hoặc dữ liệu config bị xóa do hết hạn time-based retention.",
        "followups": "Tombstone message trong compacted topic dùng để làm gì? Cấu hình retention mặc định là bao lâu?",
        "codeBlocks": []
    },
    {
        "id": "086",
        "question": "How do you evaluate Build vs. Buy for a Data Platform?",
        "category": "Senior Architecture Mindset",
        "moduleId": "m09",
        "difficulty": "Senior",
        "tags": "build vs buy, architecture",
        "raw": "",
        "short": "Quyết định Build vs Buy phụ thuộc vào việc tính năng đó có phải là lợi thế cạnh tranh cốt lõi (core competency) của công ty hay không, ngân sách, và năng lực của team.",
        "deep": "Buy (ví dụ Snowflake, Fivetran) giúp time-to-market nhanh, ít cần kỹ sư hạ tầng. Build (ví dụ tự dựng Spark/Airflow trên K8s) tiết kiệm opex khi scale cực lớn, cho phép tùy chỉnh sâu nhưng tốn công vận hành (TCO).",
        "production": "Một startup chọn Buy Fivetran để lấy data từ CRM vào BigQuery trong 2 tuần. Một công ty công nghệ lớn (Uber) tự Build hệ thống Hudi lakehouse để tiết kiệm hàng triệu đô compute.",
        "tradeoffs": "Buy dễ gặp vendor lock-in và chi phí tăng phi mã (sticker shock) khi scale. Build dễ bị technical debt và chi phí nhân sự duy trì hệ thống.",
        "mistakes": "Tự Build các tool ingestion cơ bản trong khi team chỉ có 2 Data Engineer, dẫn đến việc dùng toàn bộ thời gian fix bug thay vì tạo giá trị business.",
        "followups": "TCO (Total Cost of Ownership) bao gồm những gì? Làm sao để giảm thiểu vendor lock-in?",
        "codeBlocks": []
    },
    {
        "id": "087",
        "question": "What are key strategies for cloud cost optimization in Data Engineering?",
        "category": "Senior Architecture Mindset",
        "moduleId": "m09",
        "difficulty": "Senior",
        "tags": "cost, optimization",
        "raw": "",
        "short": "Tối ưu chi phí tập trung vào việc giám sát chặt chẽ, sử dụng đúng dịch vụ (spot instances, storage tiers), tối ưu hóa câu truy vấn và thiết lập giới hạn (guardrails).",
        "deep": "Các bước thường gặp: Phân tích dashboard chi phí (FinOps), tìm các query quét toàn bộ bảng (full scan), áp dụng partitioning/clustering, chuyển dữ liệu cũ sang cold storage, và tắt cluster khi không dùng.",
        "production": "Hóa đơn BigQuery tăng gấp đôi do một bảng unpartitioned được query mỗi 5 phút. Giải pháp: Thêm partition theo ngày và thiết lập quota giới hạn số TB được scan mỗi ngày cho mỗi team.",
        "tradeoffs": "Tối ưu quá sớm (premature optimization) làm chậm tiến độ dự án. Chuyển sang cold storage tiết kiệm tiền nhưng làm chậm truy vấn lịch sử.",
        "mistakes": "Không gán thẻ (resource tagging) cho các job/table, dẫn đến khi hóa đơn tăng cao không biết team hay pipeline nào là thủ phạm.",
        "followups": "FinOps là gì? Bạn xử lý thế nào khi một Data Scientist chạy một câu query tốn $500?",
        "codeBlocks": []
    },
    {
        "id": "088",
        "question": "Compare Data Mesh and Data Fabric concepts.",
        "category": "Senior Architecture Mindset",
        "moduleId": "m09",
        "difficulty": "Senior",
        "tags": "data mesh, data fabric",
        "raw": "",
        "short": "Data Mesh là khái niệm tổ chức (organizational) phân quyền sở hữu dữ liệu cho từng domain. Data Fabric là cách tiếp cận công nghệ (technological) dùng AI/Metadata để tự động hóa tích hợp dữ liệu.",
        "deep": "Mesh giải quyết vấn đề thắt cổ chai ở team Data trung tâm bằng cách coi Data as a Product. Các team tự chịu trách nhiệm về data của họ. Fabric tập trung vào việc tạo ra một lớp truy cập dữ liệu liền mạch từ nhiều hệ thống vật lý khác nhau.",
        "production": "Công ty áp dụng Data Mesh: Team Marketing tự build và quản lý `dim_campaigns`, team Finance tự quản lý `fact_revenue`. Trung tâm chỉ cung cấp hạ tầng dbt/Airflow và governance rules.",
        "tradeoffs": "Data Mesh yêu cầu mức độ trưởng thành văn hóa cao; nếu áp dụng sai sẽ tạo ra các silo dữ liệu độc lập không thể join với nhau. Fabric phụ thuộc vào tool đắt tiền.",
        "mistakes": "Mua một tool mới và tuyên bố 'Chúng ta đã có Data Mesh', trong khi mô hình tổ chức vẫn là một team data gánh toàn bộ yêu cầu.",
        "followups": "Các nguyên tắc cốt lõi của Data Mesh là gì? Federated Governance hoạt động thế nào?",
        "codeBlocks": []
    },
    {
        "id": "089",
        "question": "How do you mitigate vendor lock-in in modern data stacks?",
        "category": "Senior Architecture Mindset",
        "moduleId": "m09",
        "difficulty": "Senior",
        "tags": "vendor lock-in, architecture",
        "raw": "",
        "short": "Giảm thiểu vendor lock-in bằng cách sử dụng các chuẩn mở (open standards), tách biệt tính toán và lưu trữ, và dùng các công cụ mã nguồn mở ở lớp điều phối và biến đổi (như Airflow, dbt).",
        "deep": "Thay vì dùng các hàm đặc thù của Snowflake, hãy viết logic trong dbt (chỉ dùng ANSI SQL). Thay vì lưu format độc quyền, hãy lưu dữ liệu dưới dạng Iceberg/Delta trên S3. Khi cần thiết, bạn có thể chuyển engine tính toán sang Trino hoặc Databricks.",
        "production": "Kiến trúc Lakehouse của chúng tôi lưu mọi thứ ở format Apache Iceberg trên AWS S3. Dù đang dùng Athena để query, nếu Athena tăng giá, chúng tôi có thể dễ dàng trỏ StarRocks vào cùng bucket S3 đó.",
        "tradeoffs": "Việc tránh lock-in thường đồng nghĩa với việc không tận dụng được các tính năng ưu việt, tối ưu nhất của nền tảng đó. Đôi khi chấp nhận lock-in một phần lại hiệu quả hơn về time-to-market.",
        "mistakes": "Bao bọc (wrap) mọi service bằng các lớp abstraction phức tạp tự viết chỉ vì 'sợ lock-in', làm tăng chi phí bảo trì hơn cả chi phí đổi vendor.",
        "followups": "Open Table Format (Delta/Iceberg/Hudi) giúp ích gì cho vấn đề lock-in? Bạn có bao giờ cố ý chọn vendor lock-in không?",
        "codeBlocks": []
    },
    {
        "id": "090",
        "question": "How do you design for High Availability (HA) and Disaster Recovery (DR)?",
        "category": "Senior Architecture Mindset",
        "moduleId": "m09",
        "difficulty": "Senior",
        "tags": "HA, DR, RPO, RTO",
        "raw": "",
        "short": "HA đảm bảo hệ thống luôn chạy (multi-AZ, load balancers). DR là kế hoạch khôi phục khi toàn bộ vùng (region) sập, tập trung vào RTO (thời gian khôi phục) và RPO (lượng dữ liệu chấp nhận mất).",
        "deep": "Hệ thống Data cần phân loại tier. Dữ liệu thô (raw) phải replicate cross-region để RPO = 0. Cluster tính toán (compute) có thể cấu hình infrastructure-as-code (Terraform) để dựng lại nhanh chóng, giảm RTO.",
        "production": "Khi AWS us-east-1 sập, Terraform tự động spin up Airflow ở us-west-2, trỏ vào S3 cross-region replica. Pipeline khôi phục sau 30 phút (RTO = 30m).",
        "tradeoffs": "Active-Active DR cực kỳ đắt đỏ và phức tạp trong việc giải quyết xung đột (conflict resolution). Active-Passive rẻ hơn nhưng thời gian RTO lâu hơn.",
        "mistakes": "Không bao giờ diễn tập (game day) kế hoạch DR. Bản sao lưu (backup) có tồn tại nhưng không thể restore thành công do thiếu quyền KMS key.",
        "followups": "RPO và RTO là gì? Sự khác nhau giữa Multi-AZ và Multi-Region?",
        "codeBlocks": []
    },
    {
        "id": "091",
        "question": "How to choose between Managed Services vs. Self-hosted?",
        "category": "Senior Architecture Mindset",
        "moduleId": "m09",
        "difficulty": "Senior",
        "tags": "managed, self-hosted",
        "raw": "",
        "short": "Managed services (ví dụ MWAA, Confluent) tiết kiệm công vận hành nhưng đắt hơn và kém linh hoạt. Self-hosted (chạy trên EC2/K8s) rẻ hơn về compute, dễ tùy chỉnh nhưng đòi hỏi team kỹ sư giỏi.",
        "deep": "Lựa chọn phụ thuộc vào quy mô (scale) và bảo mật (security/compliance). Nếu team Data không có DevOps/SRE hỗ trợ, Managed là lựa chọn duy nhất an toàn. Tuy nhiên, ở scale cực lớn, Self-hosted giúp tiết kiệm hàng triệu đô.",
        "production": "Ban đầu dùng Confluent Cloud để chạy Kafka. Khi lưu lượng đạt hàng trăm GB/s, chi phí mạng (egress/ingress) quá cao, team chuyển sang tự host Kafka trên EKS bằng Strimzi operator.",
        "tradeoffs": "Managed tốn Opex (tiền thuê) nhưng giảm lương nhân sự. Self-hosted tiết kiệm Opex nhưng tốn thời gian on-call, nâng cấp phiên bản và vá lỗi bảo mật.",
        "mistakes": "Tự host công cụ cốt lõi (như database) trong khi team không ai có kinh nghiệm backup, tuning hệ điều hành, dẫn đến mất dữ liệu nghiêm trọng.",
        "followups": "Bạn sẽ khuyên một startup series-A nên chọn hướng nào? TCO được tính như thế nào trong trường hợp này?",
        "codeBlocks": []
    }
]

questions.extend(new_questions)
data['questions'] = questions

# Update HTML content
new_json = json.dumps(data, ensure_ascii=False)
new_content = content[:match.start(1)] + new_json + content[match.end(1):]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Appended {len(new_questions)} new questions. Fixed spelling and split tradeoffs/mistakes.")
