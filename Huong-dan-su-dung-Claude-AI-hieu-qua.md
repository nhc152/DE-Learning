# HƯỚNG DẪN SỬ DỤNG CLAUDE AI HIỆU QUẢ

Dành cho CEO, Manager, Marketer và người làm Business

*Không cần biết code. Chỉ cần biết cách hỏi đúng.*

**Bùi Tấn Việt**
CEO SePay.Vn | 123HOST.Vn
Tháng 2, 2026

---

## MỤC LỤC

- Phần 1: Tư duy đúng trước khi dùng AI
- Phần 2: Thiết lập Claude cho công việc của bạn
- Phần 3: Hiểu cách AI hoạt động: Bộ nhớ, Ngữ cảnh và Giới hạn
- Phần 4: Cách viết câu lệnh hiệu quả - Công thức 4C
- Phần 5: Kỹ thuật Brainstorm: Dẫn dắt AI từng bước
- Phần 6: 7 bài toán Business mà Claude giải tốt nhất
- Phần 7: Skills - Dạy Claude làm việc theo cách của bạn
- Phần 8: Kỹ thuật nâng cao: Lặp lại, Phản biện, Rút bài học
- Phần 9: Những sai lầm phổ biến và cách tránh
- Phần 10: Ví dụ thực tế: Cách CEO SePay dùng Claude hằng ngày
- Phần 11: Một ngày làm việc minh họa với Claude
- Phụ lục A: Bộ câu lệnh mẫu cho từng phòng ban
- Phụ lục B: Từ điển thuật ngữ AI cho người không chuyên

---

## PHẦN 1: TƯ DUY ĐÚNG TRƯỚC KHI DÙNG AI

Trước khi học cách dùng Claude, bạn cần hiểu một điều quan trọng: AI khuếch đại năng lực sẵn có của bạn, không thay thế năng lực.

Người có kiến thức marketing dùng AI sẽ ra kết quả chất lượng cao gấp 3-5 lần. Người không có kiến thức nền dùng AI vẫn ra kết quả, nhưng không biết nó đúng hay sai - và đây là điều nguy hiểm hơn cả việc không dùng AI.

### 3 nguyên tắc cốt lõi

**1. AI là cộng sự, không phải nút bấm thần kỳ**

Đừng nghĩ AI sẽ làm hết mọi thứ cho bạn. Hãy nghĩ AI là một đồng nghiệp cực kỳ giỏi nhưng mới vào công ty - cần bạn giao việc rõ ràng thì mới làm đúng.

**2. Kết quả đầu tiên luôn là bản nháp**

Không bao giờ lấy câu trả lời đầu tiên của AI rồi dùng luôn. Luôn đọc lại, chỉnh sửa, yêu cầu viết lại. Người dùng AI giỏi lặp lại ít nhất 2-3 lần.

**3. Bạn là người ra quyết định cuối cùng**

AI có thể sai. AI có thể tự tin nói điều không đúng. Luôn dùng kinh nghiệm và kiến thức của bạn để đánh giá kết quả. Nếu có gì không đúng, hỏi lại ngay.

> **MẸO:** Cách đơn giản nhất để kiểm tra: Nếu bạn đọc kết quả mà không hiểu nó đang nói gì, hoặc không thể giải thích cho đồng nghiệp - thì chưa nên dùng kết quả đó.

---

## PHẦN 2: THIẾT LẬP CLAUDE CHO CÔNG VIỆC CỦA BẠN

### Bắt đầu: Tạo tài khoản và làm quen

**Bước 1: Truy cập và đăng ký**

- Vào claude.ai trên trình duyệt (máy tính hoặc điện thoại)
- Nhấn Sign Up (Đăng ký) - có thể đăng ký bằng email hoặc tài khoản Google
- Sau khi đăng ký xong, bạn sẽ thấy một ô trò chuyện trắng - đó là nơi bạn gõ câu lệnh cho Claude

**Bước 2: Chọn gói sử dụng**

| Gói | Giá | Phù hợp với |
|-----|-----|-------------|
| Miễn phí (Free) | 0 đồng | Dùng thử, số lượng tin nhắn giới hạn. Hết lượt phải chờ vài giờ |
| Pro | $20/tháng (~500,000đ) | Dùng hằng ngày cho công việc. Nhiều tin nhắn hơn gấp 5 lần, được dùng phiên bản AI thông minh nhất, tạo file, tìm kiếm web |
| Max | $100-$200/tháng | Cho người dùng rất nhiều mỗi ngày. Gấp 5-20 lần gói Pro |
| Team | Từ $25/người/tháng | Cho nhóm từ 5 người trở lên. Chia sẻ Dự án giữa các thành viên, quản lý tập trung |

> **MẸO:** Gói miễn phí chỉ dùng được phiên bản Sonnet - đủ để trải nghiệm cách tương tác với AI. Nhưng nếu muốn dùng Opus (phiên bản thông minh nhất, cho kết quả tốt nhất), bạn cần nâng lên gói Pro. Toàn bộ ví dụ trong tài liệu này đều được thực hiện với Opus trên gói Pro.

### Quan trọng: Chọn phiên bản AI (Model)

Claude có nhiều phiên bản AI với mức độ thông minh khác nhau. Khi dùng gói Pro trở lên, bạn sẽ thấy thanh chọn phiên bản ở đầu mỗi cuộc trò chuyện. Hãy chọn đúng phiên bản:

| Phiên bản | Đặc điểm | Nên dùng khi |
|-----------|----------|--------------|
| Opus (khuyên dùng) | Thông minh nhất. Phân tích sâu, hiểu ngữ cảnh phức tạp, cho kết quả chất lượng cao nhất | Viết chiến lược, phân tích kinh doanh, viết nội dung quan trọng, brainstorm ý tưởng |
| Sonnet | Nhanh hơn Opus, khá thông minh nhưng kém hơn ở các bài toán phức tạp | Việc đơn giản: tóm tắt email, dịch thuật, trả lời nhanh |
| Haiku | Nhanh nhất, nhưng đơn giản nhất. Phù hợp việc không cần suy nghĩ sâu | Sửa lỗi chính tả, format lại văn bản, câu hỏi đơn giản |

> **MẸO:** Lời khuyên: Nếu dùng cho công việc kinh doanh, luôn chọn Opus. Sự khác biệt rất rõ ràng - Opus phân tích sâu hơn, viết hay hơn, và ít mắc lỗi hơn so với Sonnet.

**Bước 3: Thử ngay câu đầu tiên**

Đừng đọc hết tài liệu này rồi mới bắt đầu. Hãy mở claude.ai ngay bây giờ và gõ thử một câu đơn giản:

> **THỬ NGAY:**
> Tôi là [tên bạn], [chức vụ] tại [công ty]. Giúp tôi viết một email ngắn chúc mừng đối tác nhân dịp hợp tác thành công.

Chỉ cần gõ câu đó, nhấn Enter, và xem Claude trả lời. Bạn sẽ thấy ngay cảm giác tương tác với AI ra sao. Sau đó tiếp tục đọc tài liệu này để học cách dùng hiệu quả hơn.

### Thiết lập để Claude hiểu bạn tốt hơn

Sau khi đã thử vài câu và quen với giao diện, hãy dành 10 phút thiết lập. Việc này giúp mọi cuộc trò chuyện sau đó đều tốt hơn, không cần lặp lại thông tin.

**Bước 1: Cài đặt Tùy chỉnh cá nhân (User Preferences)**

Mục đích: Đây giống như một tấm thẻ nhân viên mà bạn đưa cho Claude. Thay vì mỗi lần mở cuộc trò chuyện mới phải giới thiệu lại 'Tôi là ai, làm gì, cần gì', bạn chỉ cần cài đặt một lần. Sau đó Claude sẽ tự nhớ và điều chỉnh câu trả lời phù hợp với bạn trong mọi cuộc trò chuyện.

Vào Settings > Profile > User Preferences trên claude.ai. Hãy điền càng chi tiết càng tốt - đây là nền tảng để Claude hiểu bạn. Dưới đây là mẫu tham khảo:

```
## Thông tin về tôi
- Tên: [Họ tên]
- Chức vụ: [Ví dụ: Giám đốc điều hành, Trưởng phòng Marketing...]
- Giới tính: [Nam/Nữ]
- Công cụ thường dùng: [Ví dụ: Google Docs, Google Sheets, Canva, Excel...]

## Trình độ của tôi
- Về kinh doanh: [Ví dụ: Có 10 năm kinh nghiệm quản lý. Hiểu về chiến lược, marketing, tài chính, nhân sự]
- Về kỹ thuật: [Ví dụ: Không biết lập trình. Biết dùng Excel cơ bản. Hoặc: Thông thạo Excel nâng cao]

## Công việc hằng ngày
- [Ví dụ: Điều hành công ty, họp với các phòng ban]
- [Ví dụ: Lập kế hoạch chiến lược, theo dõi doanh thu]
- [Ví dụ: Viết nội dung Facebook, soạn email đối tác]
- [Ví dụ: Làm slide thuyết trình, làm báo cáo Excel]

## Công ty của tôi
- Tên công ty: [Tên]. Website: [URL]
- Lĩnh vực: [Ví dụ: Cung cấp dịch vụ API thanh toán cho doanh nghiệp]
- Quy mô: [Ví dụ: 200 nhân viên, doanh thu 150 tỷ/năm]
- Tình hình: [Ví dụ: Đang tăng trưởng cao, lợi nhuận tốt. Hoặc: Đang giai đoạn tái cấu trúc]

## Ngôn ngữ
- Luôn trả lời bằng tiếng Việt trừ khi tôi hỏi bằng tiếng Anh
- Thuật ngữ chuyên ngành có thể giữ nguyên tiếng Anh nhưng hãy hạn chế

## Giọng văn và cách trình bày
- Trình bày đủ sâu như một chuyên gia, đừng nói chung chung
- Thẳng thắn chỉ ra vấn đề, không cần né tránh
- Khi không chắc chắn thì nói rõ là không chắc, đừng đoán mò
- Không thêm những câu lưu ý không cần thiết
```

**Tại sao cần chi tiết đến vậy?**

Mỗi thông tin bạn cung cấp giúp Claude điều chỉnh cách trả lời. Ví dụ:
- Ghi 'CEO công ty fintech' → Claude phân tích ở góc nhìn CEO, không phải góc sinh viên
- Ghi 'Không biết lập trình' → Claude sẽ không dùng thuật ngữ kỹ thuật khi giải thích
- Ghi 'Thẳng thắn, không né tránh' → Claude sẽ chỉ ra vấn đề thay vì chỉ khen
- Ghi 'Công ty đang tăng trưởng cao' → Claude sẽ tập trung vào chiến lược mở rộng thay vì cắt giảm

> **MẸO:** Bạn không cần viết hoàn hảo ngay. Bắt đầu với thông tin cơ bản, rồi bổ sung dần khi thấy Claude trả lời chưa sát với bạn. Mỗi lần bổ sung, mọi cuộc trò chuyện sau đó đều được cải thiện.

**Bước 2: Bật Bộ nhớ (Memory) - Để Claude nhớ bạn qua các cuộc trò chuyện**

Mặc định, mỗi cuộc trò chuyện mới là một trang giấy trắng - Claude không nhớ gì từ cuộc trước. Nhưng nếu bạn bật tính năng Bộ nhớ, Claude sẽ tự động học và nhớ thông tin quan trọng về bạn qua thời gian.

Vào Settings > Capabilities, kéo xuống phần Memory và bật cả 2 tùy chọn:
- **Search and reference chats:** Cho phép Claude tìm lại nội dung từ các cuộc trò chuyện cũ. Ví dụ bạn hỏi "hôm qua mình bàn gì nhỉ?" - Claude sẽ tìm lại được.
- **Generate memory from chat history:** Cho phép Claude tự động ghi nhớ thông tin quan trọng (tên bạn, công ty, cách làm việc...) để dùng trong các cuộc trò chuyện sau. Đây là cách Claude "học" về bạn qua thời gian.

> **MẸO:** Bật 2 tùy chọn này ngay. Đây là bước mà 90% người dùng bỏ qua, dẫn đến phải nhắc lại thông tin mỗi cuộc trò chuyện. Kết hợp Tùy chỉnh cá nhân (Bước 1) + Bộ nhớ (Bước 2) = Claude hiểu bạn ngày càng tốt hơn mà không cần bạn làm gì thêm.

**Bước 3: Tải lên tài liệu quan trọng**

Khi trò chuyện với Claude, bạn có thể tải lên các tài liệu để Claude đọc và phân tích. Claude đọc được file PDF, Word, Excel, PowerPoint, và hình ảnh.

> **MẸO:** Đừng tải lên quá nhiều tài liệu một lúc. 2-3 file liên quan nhất là đủ. Quá nhiều sẽ khiến Claude bị loãng sự tập trung. Chất lượng thông tin quan trọng hơn số lượng.

### Nâng cao: Khi nào nên dùng Dự án (Project)?

Claude có tính năng Dự án (Project) nằm ở thanh menu bên trái trên claude.ai. Tuy nhiên, phần lớn người dùng chỉ cần Tùy chỉnh cá nhân + Bộ nhớ là đủ cho công việc hằng ngày. Bạn cứ mở cuộc trò chuyện mới và hỏi thẳng - không cần suy nghĩ 'cái này nên vào dự án nào'.

Dự án chỉ thực sự hữu ích khi bạn có một mảng công việc cần Claude nhớ nhiều tài liệu tham khảo cố định. Ví dụ:
- Dự án Marketing: chứa sẵn bộ nhận diện thương hiệu, chân dung khách hàng, giọng văn chuẩn
- Dự án Chiến lược: chứa sẵn kế hoạch kinh doanh, phân tích SWOT, báo cáo tài chính

Khi mở cuộc trò chuyện trong Dự án, Claude đã biết sẵn tất cả tài liệu đó - không cần tải lên lại mỗi lần.

---

## PHẦN 3: HIỂU CÁCH AI HOẠT ĐỘNG: BỘ NHỚ, NGỮ CẢNH VÀ GIỚI HẠN

Để dùng AI hiệu quả, bạn cần hiểu 3 khái niệm quan trọng về cách AI xử lý thông tin. Không cần hiểu kỹ thuật sâu - chỉ cần hiểu đủ để biết tại sao AI đôi khi 'quên' hoặc trả lời lung tung.

### Cửa sổ ngữ cảnh (Context Window) - Tại sao AI đôi khi 'quên'?

Hãy tưởng tượng Claude là một người đang đọc tài liệu trên một chiếc bàn. Chiếc bàn chỉ rộng có hạn - nếu bạn chất quá nhiều giấy tờ lên, những tờ cũ sẽ rơi xuống đất và không còn nhìn thấy nữa.

Đó chính là cửa sổ ngữ cảnh - lượng thông tin tối đa mà Claude có thể 'nhìn thấy' cùng lúc trong một cuộc trò chuyện. Claude hiện hỗ trợ khoảng 200,000 token (tương đương khoảng 500 trang sách).

**Vấn đề thường gặp:** Khi bạn trò chuyện quá dài, hoặc tải lên quá nhiều tài liệu cùng lúc, Claude bắt đầu mất tập trung - trả lời không chính xác, bỏ sót thông tin, hoặc lặp lại ý cũ.

**Cách xử lý:**
- Nếu cuộc trò chuyện quá dài, hãy mở cuộc trò chuyện mới và tóm tắt lại những gì đã thống nhất
- Đừng tải lên 10 file cùng lúc. Tải lên 2-3 file liên quan nhất
- Chia công việc lớn thành nhiều cuộc trò chuyện nhỏ, mỗi cuộc tập trung vào 1 phần

### Bộ nhớ (Memory) - Claude nhớ gì về bạn qua các cuộc trò chuyện?

Ở Phần 2, bạn đã bật tính năng Bộ nhớ. Dưới đây là cách sử dụng hiệu quả hơn.

**Bộ nhớ hoạt động như thế nào:**
- Claude tự động rút ra thông tin quan trọng từ các cuộc trò chuyện trước (tên bạn, công ty, sở thích, cách làm việc...)
- Bạn cũng có thể chủ động ra lệnh cho Claude ghi nhớ điều gì đó
- Bộ nhớ được cập nhật dần, nên cuộc trò chuyện gần nhất có thể chưa được ghi nhớ ngay

**Cách ra lệnh Claude ghi nhớ:**

```
"Hãy nhớ rằng công ty tôi dùng HubSpot làm CRM."
"Ghi nhớ: khi viết bài Facebook cho tôi, luôn dùng giọng văn chuyên gia chia sẻ kinh nghiệm."
"Nhớ rằng tôi thích phân tích dạng bảng so sánh hơn là viết dài."
```

**Cách xem và quản lý bộ nhớ:** Vào Settings > Profile > Memory trên claude.ai. Tại đây bạn có thể xem Claude đang nhớ những gì, xóa thông tin sai, hoặc tắt tính năng bộ nhớ nếu muốn.

> **MẸO:** Kết hợp Tùy chỉnh cá nhân (thông tin cố định về bạn) + Bộ nhớ (thông tin Claude tự học qua thời gian) + Dự án (thông tin chuyên sâu cho từng mảng công việc) = Claude hiểu bạn ngày càng tốt hơn.

---

## PHẦN 4: CÁCH VIẾT CÂU LỆNH HIỆU QUẢ - CÔNG THỨC 4C

Câu lệnh là câu bạn gõ cho Claude. Câu lệnh tốt cho kết quả tốt. Câu lệnh mơ hồ cho kết quả vô dụng. Đây là công thức đơn giản nhất:

### C - BỐI CẢNH (Context)

Cho Claude biết bạn đang ở đâu, làm gì, và tình hình hiện tại ra sao. Hãy tưởng tượng bạn đang giao việc cho nhân viên mới - họ cần biết bối cảnh để làm đúng.

> **VÍ DỤ:**
> Tôi là trưởng phòng Marketing công ty bất động sản tầm trung tại TP.HCM. Tháng tới chúng tôi ra mắt dự án căn hộ giá 2-3 tỷ, nhắm đến vợ chồng trẻ 28-35 tuổi.

### C - YÊU CẦU CỤ THỂ (Command)

Nói rõ bạn muốn Claude làm gì. Càng cụ thể càng tốt. Thay vì 'viết bài quảng cáo', hãy nói rõ: bao nhiêu ý tưởng, mỗi ý tưởng gồm những gì, tập trung vào thông điệp nào.

> **VÍ DỤ:**
> Hãy viết 5 ý tưởng quảng cáo Facebook, mỗi ý tưởng gồm: tiêu đề, mô tả ngắn 2 dòng, và gợi ý hình ảnh đi kèm. Tập trung vào nỗi đau 'thuê nhà mãi không có tài sản tích lũy'.

### C - GIỚI HẠN (Constraints)

Cho Claude biết những gì KHÔNG được làm, và các ràng buộc cần tuân thủ.

> **VÍ DỤ:**
> Không dùng giọng văn kích thích mua hàng. Giọng chân thực, gần gũi. Mỗi tiêu đề không quá 10 từ. Không nhắc đến giá cụ thể.

### C - TIÊU CHUẨN (Criteria)

Cho Claude biết kết quả tốt trông như thế nào. Điều này giúp Claude hiểu đích đến.

> **VÍ DỤ:**
> Kết quả tốt là khi đọc xong, người đọc cảm thấy 'đây đúng là vấn đề của mình' chứ không phải 'lại quảng cáo'. Ý tưởng phải gây tò mò để người ta nhấn vào xem tiếp.

### Ví dụ hoàn chỉnh: Ghép 4C lại

❌ **ĐỪNG:** Câu lệnh kém:
> "Viết cho tôi lý do tăng ngân sách marketing."

✅ **NÊN:** Câu lệnh tốt (có 4C):
> "Tôi là Giám đốc Marketing công ty SaaS B2B, khách hàng là doanh nghiệp vừa và nhỏ tại Việt Nam. Tuần tới tôi cần trình bày cho CEO về việc tăng ngân sách marketing quý 2 thêm 30%. Hãy giúp tôi soạn 5 luận điểm chính, mỗi luận điểm có tiêu đề, giải thích 2-3 câu, và số liệu minh họa. Giọng chuyên nghiệp nhưng thuyết phục. Kết quả tốt là khi CEO đọc xong sẽ nói: dữ liệu thuyết phục, đáng để đầu tư."

> **MẸO:** Bạn không cần nhớ 4C mỗi lần gõ. Chỉ cần nhớ: cho Claude đủ thông tin để nó hiểu bạn muốn gì, như cách bạn giao việc cho một nhân viên mới.

---

## PHẦN 5: KỸ THUẬT BRAINSTORM: DẪN DẮT AI TỪNG BƯỚC

Nhiều người nghĩ phải suy nghĩ thật kỹ, viết một câu lệnh dài và hoàn chỉnh ngay từ đầu. Không cần. Cách hiệu quả nhất là trò chuyện tự nhiên với Claude, cung cấp thông tin dần dần, để Claude tự hiểu bạn cần gì.

Hãy tưởng tượng bạn đang ngồi uống cà phê với một chuyên gia tư vấn. Bạn không cần chuẩn bị bài thuyết trình 10 trang - bạn chỉ cần nói ra vấn đề, rồi hai người cùng trao đổi qua lại.

### Ví dụ thực tế: Lên chiến lược marketing cho sản phẩm mới

> **BẠN:** Tôi đang chuẩn bị ra mắt dịch vụ loa thanh toán - loa tự đọc khi có người chuyển khoản. Giúp tôi nghĩ xem nên tiếp cận nhóm khách hàng nào trước?

> **CLAUDE:** (Claude phân tích và đề xuất 3-4 nhóm khách hàng tiềm năng, kèm lý do cho từng nhóm)

> **BẠN:** Nhóm tiểu thương và quán ăn nghe hợp lý. Vấn đề lớn nhất của họ là bán hàng đông, không kịp kiểm tra chuyển khoản. Giúp tôi nghĩ thông điệp marketing nhắm vào vấn đề này.

> **CLAUDE:** (Claude đề xuất các góc thông điệp tập trung vào: bán hàng không lo sót đơn, nghe tiếng 'ting' là biết tiền về)

> **BẠN:** Ý số 2 hay đấy. Bây giờ viết cho tôi bài Facebook theo hướng đó. Đối tượng đọc là chủ quán ăn, tiểu thương chợ, tuổi 30-50.

### Tại sao cách này hiệu quả hơn?

- Bạn không cần suy nghĩ hết mọi thứ trước khi bắt đầu
- Mỗi câu trả lời của Claude giúp bạn nghĩ rõ hơn bước tiếp theo
- Claude hiểu dần dần thay vì phải đoán ý bạn từ một câu lệnh dài
- Kết quả cuối cùng chính xác hơn vì được xây dựng qua nhiều bước xác nhận

> **MẸO:** Quy tắc vàng: Nếu bạn không biết bắt đầu từ đâu, hãy mô tả vấn đề bạn đang gặp. Claude sẽ hỏi lại hoặc đề xuất hướng đi. Từ đó bạn chọn hướng phù hợp và đi sâu dần.

---

## PHẦN 6: 7 BÀI TOÁN BUSINESS MÀ CLAUDE GIẢI TỐT NHẤT

### 1. Viết nội dung và soạn thảo văn bản

**Bài toán:** Bài viết Facebook, email, đề xuất hợp tác, báo cáo, thông báo nội bộ

**Cách dùng:** Cho Claude biết: ai sẽ đọc, mục đích bài viết, giọng văn muốn dùng, và độ dài mong muốn. Tải lên bài viết cũ để Claude học phong cách.

> **CÂU LỆNH MẪU:**
> "Tôi cần viết email gửi đối tác Nhật Bản để đề xuất tích hợp API thanh toán SePay. Đối tác là công ty logistics lớn. Giọng lịch sự, chuyên nghiệp, ngắn gọn. Email bằng tiếng Anh, không quá 200 từ."

### 2. Phân tích chiến lược và ra quyết định

**Bài toán:** Đánh giá đối thủ, phân tích thị trường, SWOT, lập kế hoạch kinh doanh

**Cách dùng:** Cung cấp dữ liệu thực tế. Đừng hỏi chung chung kiểu 'phân tích thị trường X'. Hãy cho Claude số liệu cụ thể rồi yêu cầu phân tích.

> **CÂU LỆNH MẪU:**
> "Công ty tôi đang cân nhắc mở thêm dịch vụ mới bên cạnh sản phẩm chính. Thị trường hiện tại có 3 đối thủ lớn. Vốn đầu tư ban đầu khoảng 500 triệu. Phân tích giúp tôi: cơ hội - rủi ro, thời điểm có nên làm không, và chiến lược ra mắt nên như thế nào."

### 3. Nghiên cứu và tổng hợp thông tin

**Bài toán:** Tìm hiểu về ngành, xu hướng, công nghệ mới, đối thủ

**Cách dùng:** Claude có thể tìm kiếm thông tin trên web ngay trong cuộc trò chuyện. Hãy yêu cầu tìm kiếm và tổng hợp, sau đó nói rõ muốn kết quả dạng nào.

> **CÂU LỆNH MẪU:**
> "Tìm hiểu về xu hướng Open Banking tại Đông Nam Á năm 2026. Tập trung vào: quy định mới, các công ty nổi bật, và cơ hội cho doanh nghiệp cung cấp API ngân hàng. Tổng hợp thành bản tóm tắt 1 trang với 5 điểm chính."

### 4. Tạo file chuyên nghiệp

**Bài toán:** Slide thuyết trình, bảng tính phân tích, báo cáo Word, tài liệu PDF

**Cách dùng:** Claude có thể tạo file PowerPoint, Excel, Word, PDF trực tiếp. Bạn chỉ cần mô tả nội dung và cách trình bày, Claude sẽ tạo file để tải về.

> **CÂU LỆNH MẪU:**
> "Tạo file PowerPoint báo cáo quý 1/2026, gồm 8 slide: trang bìa, tổng quan doanh thu, phân tích theo sản phẩm, so sánh với chỉ tiêu, điểm sáng và điểm cần cải thiện, kế hoạch quý 2, hạng mục hành động, trang cảm ơn."

### 5. Tư duy sáng tạo và giải quyết vấn đề

**Bài toán:** Tìm ý tưởng mới, giải quyết vấn đề phức tạp, khám phá góc nhìn khác

**Cách dùng:** Claude mạnh nhất khi bạn đưa ra vấn đề cụ thể và yêu cầu nhiều hướng giải quyết. Sau đó chọn hướng tốt nhất, rồi yêu cầu đào sâu.

> **CÂU LỆNH MẪU:**
> "Tỷ lệ khách hàng rời bỏ dịch vụ API thanh toán SePay đang là 8%/tháng. Khách phàn nàn: tích hợp phức tạp, hỗ trợ chậm, thiếu báo cáo. Cho tôi 10 giải pháp, xếp theo mức tác động từ cao đến thấp."

### 6. Soạn email và tin nhắn quan trọng

**Bài toán:** Email cho đối tác, phản hồi khiếu nại, đàm phán, thông báo nhạy cảm

**Cách dùng:** Cho Claude biết: mối quan hệ với người nhận, lịch sử trao đổi, mục tiêu muốn đạt, và điều gì tuyệt đối không được nói.

> **CÂU LỆNH MẪU:**
> "Tôi cần viết email từ chối tăng lương cho một nhân viên. Nhân viên này làm tốt nhưng mới vào 6 tháng, công ty đang tối ưu chi phí. Muốn từ chối nhưng vẫn giữ được nhân viên. Gợi ý: xem xét lại sau 3 tháng."

### 7. Học hỏi và hiểu vấn đề phức tạp

**Bài toán:** Hiểu khái niệm mới, luật mới, công nghệ mới, mô hình kinh doanh

**Cách dùng:** Claude giải thích rất tốt nếu bạn cho biết trình độ hiện tại. Đừng ngại nói 'tôi chưa biết gì về chủ đề này'.

> **CÂU LỆNH MẪU:**
> "Giải thích cho tôi về Thông tư 64/2024 (quy định Open Banking của Ngân hàng Nhà nước). Tôi là CEO công ty fintech, cần hiểu: ảnh hưởng gì đến doanh nghiệp cung cấp API ngân hàng, nghĩa vụ pháp lý, và lộ trình triển khai."

### Bonus: Đọc ảnh - Tính năng ít người biết nhưng cực kỳ hữu ích

Đây là một trong những tính năng tuyệt vời nhất của Claude mà ít người biết đến. Bạn chỉ cần chụp ảnh màn hình hoặc chụp ảnh bất kỳ thứ gì, gửi cho Claude, và hỏi. Claude đọc và hiểu ảnh rất tốt - từ văn bản, bảng biểu, biểu đồ, cho đến ảnh chụp ngoài đời thực.

**Các tình huống thực tế:**
- **Chụp ảnh báo cáo, bảng biểu:** Chụp màn hình bảng doanh thu từ Excel, dashboard Google Analytics, hoặc báo cáo quảng cáo Facebook → Gửi Claude và hỏi: 'Phân tích số liệu này cho tôi'
- **Chụp ảnh tài liệu giấy:** Chụp hợp đồng, hóa đơn, danh thiếp, hoặc tài liệu in → Claude đọc được chữ trong ảnh và tóm tắt nội dung
- **Chụp ảnh sản phẩm:** Chụp ảnh thuốc để biết tên và công dụng từng loại. Chụp ảnh linh kiện để hỏi thông số. Chụp ảnh cây cối để hỏi tên loại cây
- **Chụp ảnh vé số:** Chụp cả xấp vé số, gửi Claude và nói 'dò kết quả giúp tôi' - Claude đọc được số trên vé và tự tra kết quả
- **Chụp ảnh giao diện phần mềm:** Gặp lỗi trên màn hình? Chụp ảnh gửi Claude và hỏi 'lỗi này là gì, sửa thế nào'
- **Chụp slide bài giảng:** Chụp ảnh slide trong buổi học hoặc hội thảo → Claude tóm tắt ý chính và giải thích thêm

> **MẸO:** Bạn không cần gõ lại nội dung từ ảnh. Cứ chụp và gửi thẳng. Claude đọc được chữ trong ảnh, số liệu trong bảng, và cả nội dung viết tay (nếu rõ ràng). Đây là cách nhanh nhất để đưa thông tin vào Claude mà không cần đánh máy.

---

## PHẦN 7: SKILLS - DẠY CLAUDE LÀM VIỆC THEO CÁCH CỦA BẠN

Bạn có bao giờ gặp tình huống này không: mỗi lần mở cuộc trò chuyện mới, bạn phải nhắc lại 'viết theo cấu trúc này', 'dùng giọng văn này', 'trình bày kiểu này'? Skill (kỹ năng) sinh ra để giải quyết vấn đề đó.

### Skill là gì?

Skill là một bộ hướng dẫn mà bạn dạy cho Claude một lần, sau đó Claude sẽ tự động áp dụng mỗi khi gặp công việc liên quan. Giống như bạn viết một bộ quy trình cho nhân viên - sau khi đào tạo xong, nhân viên tự biết làm theo mà không cần nhắc lại.

Ví dụ: Bạn thường xuyên viết bài Facebook với cấu trúc nhất định (tiêu đề viết hoa, dùng gạch đầu dòng, kết bài bằng dấu =>, không dùng biểu tượng cảm xúc). Thay vì nhắc lại mỗi lần, bạn tạo một Skill chứa tất cả quy tắc đó. Từ giờ, mỗi khi bạn nói 'viết bài Facebook', Claude tự động làm theo đúng cấu trúc.

### Các loại Skill phổ biến cho công việc kinh doanh

| Loại Skill | Ví dụ | Lợi ích |
|------------|-------|---------|
| Viết nội dung | Skill viết bài Facebook, soạn email, viết báo cáo tuần | Đảm bảo mọi nội dung đúng giọng văn, đúng cấu trúc |
| Phân tích | Skill phân tích đối thủ, đánh giá dự án, đánh giá hiệu quả | Phân tích theo đúng tiêu chí công ty bạn |
| Tạo tài liệu | Skill tạo slide theo mẫu, tạo báo cáo tài chính | File tạo ra đúng chuẩn, không cần chỉnh nhiều |
| Lập kế hoạch | Skill lập kế hoạch kinh doanh, lập kế hoạch marketing | AI làm theo đúng khung tư duy bạn đã định |

### Cách tạo Skill bằng cách trò chuyện với Claude

Bạn không cần biết viết code hay biết Markdown. Cách đơn giản nhất là nhờ Claude tạo Skill cho bạn qua cuộc trò chuyện:

**Bước 1: Mô tả quy trình cho Claude**

> **CÂU LỆNH MẪU:**
> "Tôi muốn tạo một Skill để Claude viết bài Facebook cho tôi. Quy tắc:
> - Tiêu đề viết hoa, gây tò mò, dễ hiểu ngay
> - Dùng gạch đầu dòng bằng dấu '-', không dùng biểu tượng cảm xúc
> - Kết bài bằng dấu '=>' kèm kết luận ngắn gọn
> - Có số liệu cụ thể, không đặt liên kết trong bài
> - Giọng văn: chuyên gia chia sẻ kinh nghiệm
>
> Hãy tạo file Skill hoàn chỉnh cho tôi và xuất ra file nén (.zip) để tôi tải về."

**Bước 2: Tải về file nén và cài đặt vào Claude**
- Claude sẽ tạo file nén (.zip) chứa Skill. Nhấn tải về máy
- Vào claude.ai, mở Settings > Profile > Skills
- Nhấn nút Upload Skill, chọn file nén vừa tải
- Skill sẽ xuất hiện trong danh sách. Bật công tắc để kích hoạt

**Bước 3: Kiểm tra Skill hoạt động đúng chưa**
- Mở cuộc trò chuyện mới, thử gõ: 'Viết bài Facebook về chủ đề XYZ'
- Kiểm tra: Claude có tự động áp dụng đúng cấu trúc không?
- Nếu chưa đúng, quay lại chỉnh sửa Skill và tải lên lại

> **MẸO:** Sau khi làm việc với Claude một thời gian, Claude đã hiểu phong cách và cách làm việc của bạn. Lúc đó bạn có thể nói: 'Dựa trên cách tôi thường yêu cầu viết bài Facebook, hãy tự tổng hợp thành một Skill hoàn chỉnh.' Claude sẽ tự rút ra quy tắc từ lịch sử trò chuyện.

---

## PHẦN 8: KỸ THUẬT NÂNG CAO: LẶP LẠI, PHẢN BIỆN, RÚT BÀI HỌC

Đây là 3 kỹ thuật phân biệt người dùng AI trung bình và người dùng AI giỏi. Không khó, chỉ cần hình thành thói quen.

### Kỹ thuật 1: LẶP LẠI - Chỉnh sửa qua nhiều vòng

Không ai viết bài hay từ bản nháp đầu tiên. Với AI cũng vậy. Sức mạnh thực sự nằm ở việc bạn biết chỉ hướng cho AI điều chỉnh.

- **Vòng 1: Lấy bản nháp:** Yêu cầu Claude viết bản đầu tiên với đầy đủ bối cảnh.
- **Vòng 2: Chỉnh hướng:** "Bỏ phần ABC, thêm phần XYZ. Phần giữa quá dài, rút gọn lại."
- **Vòng 3: Tinh chỉnh:** "Mở bài chưa đủ hấp dẫn. Viết lại mở bài gây tò mò hơn."

> **MẸO:** Phản hồi càng cụ thể, kết quả càng tốt. Thay vì nói 'viết hay hơn', hãy nói 'mở bài cần gây tò mò hơn' hoặc 'thêm số liệu cụ thể ở đoạn 2'.

### Kỹ thuật 2: PHẢN BIỆN - Kiểm tra và đặt câu hỏi ngược

Claude có thể tự tin nói những điều không chính xác. Việc của bạn là kiểm tra và phản biện khi cần.

**Các câu hỏi phản biện hữu ích:**
- "Nguồn thông tin này từ đâu? Có chính xác không?"
- "Có góc nhìn nào ngược lại không?"
- "Phân tích này có bỏ sót rủi ro nào không?"
- "Nếu giả định A sai thì kết luận có thay đổi không?"
- "Đây là câu trả lời tốt nhất hay chỉ là câu trả lời an toàn nhất?"

### Kỹ thuật 3: RÚT BÀI HỌC - Dùng kết quả thực tế để AI cải thiện

Đây là kỹ thuật mạnh nhất nhưng ít người dùng: dùng số liệu thực tế từ công việc để AI học và làm tốt hơn.

> **VÍ DỤ THỰC TẾ TỪ SEPAY:**
> Tôi vừa đăng 2 bài Facebook. Bài A dùng tiêu đề 'QUỐC GIA CỦA CÁC THIÊN TÀI TRONG DATA CENTER' đạt 5,000 lượt xem. Sau khi đổi thành 'AI CÓ THỂ ĐẠT NĂNG LỰC NGHIÊN CỨU NGANG TẦM GIẢI NOBEL' thì lượt xem tăng lên 26,000. Phân tích: tại sao tiêu đề thứ hai hiệu quả hơn? Rút ra nguyên tắc gì cho các bài sau?

> **MẸO:** Mỗi khi bạn có kết quả thực tế (lượt tương tác, doanh số, phản hồi khách hàng), hãy đưa cho Claude phân tích. Qua thời gian, bạn sẽ xây dựng được bộ nguyên tắc riêng cho công việc.

---

## PHẦN 9: NHỮNG SAI LẦM PHỔ BIẾN VÀ CÁCH TRÁNH

### Sai lầm 1: Câu lệnh quá ngắn, thiếu bối cảnh

❌ **ĐỪNG:** "Viết cho tôi kế hoạch marketing."

✅ **NÊN:** "Tôi là trưởng phòng Marketing công ty thực phẩm organic, doanh thu 20 tỷ/năm. Cần kế hoạch marketing quý 2 cho sản phẩm nước ép cold-press, giá 45K/chai, nhắm phụ nữ 25-40 tại TP.HCM. Ngân sách: 500 triệu. Cho tôi: mục tiêu, kênh, lộ trình, và phân bổ ngân sách."

### Sai lầm 2: Lấy nguyên kết quả mà không kiểm tra

❌ **ĐỪNG:** Lấy nguyên văn kết quả của Claude gửi cho sếp hoặc khách hàng.

✅ **NÊN:** Đọc lại, chỉnh sửa cho phù hợp với giọng văn và bối cảnh thực tế. AI cho bạn 80%, 20% còn lại là công việc của bạn.

### Sai lầm 3: Nhồi 5-6 yêu cầu vào một câu lệnh

❌ **ĐỪNG:** "Phân tích đối thủ, viết SWOT, đề xuất chiến lược, soạn KPI, và làm slide luôn."

✅ **NÊN:** Chia thành từng bước riêng. Bước 1: phân tích đối thủ. Bước 2: từ kết quả đó, viết SWOT. Bước 3: đề xuất chiến lược. Mỗi bước Claude sẽ làm tốt hơn nhiều.

### Sai lầm 4: Không nói rõ ai sẽ đọc kết quả

❌ **ĐỪNG:** Viết giống nhau cho mọi đối tượng.

✅ **NÊN:** Luôn nói rõ: kết quả này để trình bày cho CEO, hay để gửi khách hàng, hay để đội ngũ nội bộ đọc. Cùng một thông tin nhưng cách trình bày khác hoàn toàn.

### Sai lầm 5: Bỏ cuộc sau câu trả lời đầu tiên không vừa ý

❌ **ĐỪNG:** "AI không hiểu ý tôi" rồi tắt cuộc trò chuyện.

✅ **NÊN:** Nói cho Claude biết chỗ nào chưa đúng: 'Phần A tốt rồi, nhưng phần B chưa đúng ý. Ý tôi là... Hãy viết lại phần B.' Claude sẽ cải thiện rất nhanh qua phản hồi.

---

## PHẦN 10: VÍ DỤ THỰC TẾ: CÁCH CEO SEPAY DÙNG CLAUDE HẰNG NGÀY

SePay (sepay.vn) là công ty cung cấp hạ tầng Open Banking - API ngân hàng cho doanh nghiệp tại Việt Nam. Dưới đây là 5 cách mà CEO SePay ứng dụng Claude vào công việc và cuộc sống hằng ngày, kèm kết quả thực tế.

### Ví dụ 1: Viết nội dung Facebook đạt hàng trăm nghìn lượt xem

**Bối cảnh:** CEO SePay có niềm đam mê chia sẻ kiến thức về AI và công nghệ trên Facebook cá nhân, thường xuyên viết các bài phân tích chuyên sâu về xu hướng công nghệ mới.

**Cách làm:**
- Bước 1: Chụp ảnh bảng điều khiển Facebook chuyên nghiệp (Meta Business Suite) gửi cho Claude để AI hiểu cấu trúc và số liệu các bài đã đăng
- Bước 2: Claude phân tích: bài nào đạt lượt xem cao, cấu trúc bài lên xu hướng có đặc điểm gì (tiêu đề dạng nào, độ dài bao nhiêu, chủ đề gì thu hút)
- Bước 3: Tạo Skill viết bài Facebook riêng, bao gồm: quy tắc cấu trúc, giọng văn, và danh sách từ cần tránh (để thuật toán Facebook không hạn chế bài đăng)
- Bước 4: Sau khi đăng bài, cung cấp số liệu kết quả (lượt xem, chia sẻ, bình luận) cho Claude rút kinh nghiệm cho bài sau

**Kết quả:** Nhiều bài đạt 100,000-330,000 lượt xem. Bài cao nhất đạt trên 330,000 lượt xem và gần 900 lượt chia sẻ. Trang Facebook cá nhân tăng lên hơn 11,000 người theo dõi trong vài tháng.

> **MẸO:** Bài học: Tiêu đề quyết định 80% thành công. Tiêu đề phải dễ hiểu ngay lập tức, không nên dùng khái niệm trừu tượng dù nghe hay.

### Ví dụ 2: Cùng AI hoàn thiện chiến lược kinh doanh

**Bối cảnh:** CEO cần đánh giá và hoàn thiện chiến lược kinh doanh 2026 một cách nhanh chóng và toàn diện.

**Cách làm:**
- Tải lên toàn bộ file chiến lược (Excel kế hoạch tài chính, PowerPoint kế hoạch kinh doanh, bảng phân tích đối thủ) vào Claude
- Yêu cầu Claude đánh giá độ khả thi: mục tiêu doanh thu có thực tế không, chi phí có thiếu khoản nào, lộ trình có quá tham vọng không
- Cùng Claude phản biện từng giả định: 'Nếu thị trường chỉ tăng 10% thay vì 30% thì kế hoạch này có còn khả thi?'
- Yêu cầu Claude đề xuất kịch bản dự phòng và bổ sung phần còn thiếu

**Kết quả:** Chiến lược được hoàn thiện nhanh gấp 3 lần. Claude phát hiện được một số giả định tài chính chưa hợp lý mà CEO chưa nhận ra.

### Ví dụ 3: Dùng AI đào sâu bài học sau mỗi khóa học

**Bối cảnh:** CEO thường xuyên học hỏi và tham gia các khóa học kinh doanh. Sau mỗi buổi học, cần nghiên cứu thêm và liên hệ kiến thức với thực tế công ty.

**Cách làm:**
- Chụp ảnh hoặc tải lên slide bài giảng vào Claude sau mỗi buổi học
- Yêu cầu Claude: tóm tắt ý chính, giải thích sâu những khái niệm chưa rõ
- Yêu cầu liên hệ kiến thức với bối cảnh SePay: 'Áp dụng bài học này vào công ty tôi thì cụ thể phải làm gì?'

**Kết quả:** Thời gian ôn tập và ghi chú giảm từ 2-3 giờ xuống 30 phút. Kiến thức được liên hệ ngay với thực tế kinh doanh thay vì chỉ là lý thuyết.

### Ví dụ 4: Xây dựng Skill lập kế hoạch kinh doanh theo khung riêng

**Bối cảnh:** Mỗi lần lập kế hoạch kinh doanh phải nhắc lại cấu trúc, các bước phân tích, và tiêu chuẩn đánh giá. Mất thời gian và dễ bỏ sót.

**Cách làm:**
- Tổng hợp bộ khung lập kế hoạch kinh doanh thường dùng (các công cụ phân tích MBA như SWOT, phân tích cạnh tranh, phân khúc thị trường, chiến lược marketing mix...)
- Tải lên toàn bộ khung này vào Claude và tạo Skill chuyên biệt
- Từ giờ, mỗi khi cần lập kế hoạch cho sản phẩm mới hoặc đánh giá thị trường, chỉ cần nói: 'Lập kế hoạch kinh doanh cho dịch vụ X' - Claude tự động phân tích theo đúng khung đã định

**Kết quả:** Quá trình lập kế hoạch giảm từ 1-2 tuần xuống 2-3 ngày. Chất lượng đồng đều vì luôn tuân theo khung chuẩn, không bỏ sót yếu tố quan trọng.

### Ví dụ 5: Chụp ảnh thay vì đánh máy - AI đọc ảnh trong đời sống hằng ngày

**Bối cảnh:** Trong công việc và cuộc sống hằng ngày, có rất nhiều lúc cần AI hỗ trợ nhưng thông tin nằm trên giấy, trên màn hình, hoặc trên đồ vật thực tế - không tiện gõ lại.

**Cách làm:** Chụp ảnh và gửi thẳng cho Claude. Không cần gõ lại bất kỳ thông tin nào.

**Các tình huống đã dùng thực tế:**
- Chụp ảnh bảng điều khiển Facebook (Meta Business Suite) → Claude phân tích bài nào đạt hiệu quả cao và tại sao
- Chụp cả xấp vé số → Claude đọc số trên vé, tự tìm kiếm kết quả xổ số và dò giúp
- Chụp ảnh các hộp thuốc → Claude nhận diện tên thuốc, thành phần, công dụng từng loại
- Chụp slide bài giảng trong các buổi học → Claude tóm tắt ý chính và giải thích thêm

**Kết quả:** Tiết kiệm rất nhiều thời gian gõ lại thông tin. Nhiều việc tưởng nhỏ nhưng làm cuộc sống dễ dàng hơn rất nhiều - dò vé số mất 30 giây thay vì 10 phút, tra thuốc chỉ cần chụp 1 ảnh thay vì gõ từng tên thuốc.

---

## PHẦN 11: MỘT NGÀY LÀM VIỆC MINH HỌA VỚI CLAUDE

Dưới đây là ví dụ minh họa một ngày làm việc kết hợp Claude. Bạn không cần làm y hệt - hãy chọn những phần phù hợp với công việc của mình.

### 8:00 - Bắt đầu ngày

Mở Claude, lên kế hoạch:

> **CÂU LỆNH MẪU:**
> "Hôm nay tôi có 3 việc quan trọng: họp ban lãnh đạo lúc 10h, hạn nộp báo cáo quý 1 lúc 3h chiều, và phỏng vấn ứng viên Marketing lúc 4h. Giúp tôi chuẩn bị nội dung chính cho buổi họp trước."

### 9:00 - Chuẩn bị họp

Sau khi có nội dung, tiếp tục:

> **CÂU LỆNH MẪU:**
> "Từ nội dung trên, tạo file PowerPoint 5 slide: tổng quan, doanh thu so với chỉ tiêu, vấn đề cần quyết định, đề xuất, và bước tiếp theo."

### 13:00 - Soạn báo cáo

Tải lên dữ liệu Excel:

> **CÂU LỆNH MẪU:**
> "Tôi tải lên file doanh thu quý 1. Phân tích: xu hướng theo tháng, sản phẩm nào tăng hoặc giảm mạnh, và viết phần nhận xét cho báo cáo."

### 15:00 - Chuẩn bị phỏng vấn

Cho Claude biết vị trí cần tuyển:

> **CÂU LỆNH MẪU:**
> "Tôi cần phỏng vấn ứng viên Marketing Executive. Yêu cầu: 2-3 năm kinh nghiệm, biết chạy quảng cáo Facebook/Google. Đề xuất 10 câu hỏi: kỹ năng, tình huống, và đánh giá phù hợp văn hóa."

### 17:00 - Viết nội dung

Viết bài Facebook:

> **CÂU LỆNH MẪU:**
> "Công ty vừa đạt mốc 100,000 khách hàng sử dụng API thanh toán SePay. Viết bài chia sẻ cột mốc này. Giọng tự hào nhưng không khoe khoang. Nhấn mạnh hành trình và cảm ơn khách hàng."

---

## PHỤ LỤC A: BỘ CÂU LỆNH MẪU CHO TỪNG PHÒNG BAN

Các câu lệnh mẫu dưới đây là gợi ý để bắt đầu. Thay thế phần trong [ngoặc vuông] bằng thông tin thực tế của công ty bạn.

### MARKETING

**Viết nội dung Facebook**

> **CÂU LỆNH MẪU:**
> Tôi cần viết bài Facebook cho [trang công ty/cá nhân]. Chủ đề: [chủ đề]. Đối tượng đọc: [mô tả]. Giọng văn: [chuyên nghiệp/vui vẻ/gần gũi]. Bài viết cần câu mở đầu hấp dẫn, nội dung dưới 300 từ, và kết thúc bằng câu hỏi hoặc lời kêu gọi hành động.

**Phân tích chiến dịch quảng cáo**

> **CÂU LỆNH MẪU:**
> Chiến dịch [tên] vừa kết thúc. Kết quả: [số liệu cụ thể]. So với chỉ tiêu ban đầu [mục tiêu], kết quả [tốt/kém] hơn [bao nhiêu]%. Phân tích nguyên nhân và đề xuất 3 điều chỉnh.

### KINH DOANH

**Soạn đề xuất hợp tác**

> **CÂU LỆNH MẪU:**
> Soạn đề xuất gửi [tên khách hàng], ngành [ngành]. Họ đang gặp vấn đề [mô tả]. Giải pháp: [sản phẩm/dịch vụ]. Gồm: tổng quan, vấn đề, giải pháp, lợi ích, lộ trình, bước tiếp theo. Không quá 5 trang.

**Xử lý phản đối**

> **CÂU LỆNH MẪU:**
> Khách hàng phản đối: '[câu phản đối]'. Sản phẩm: [mô tả]. Đối thủ chào giá thấp hơn [bao nhiêu]%. Cho 3 cách trả lời, tập trung vào giá trị.

### KẾ TOÁN - TÀI CHÍNH

**Phân tích chi phí**

> **CÂU LỆNH MẪU:**
> Tôi tải lên file chi phí 6 tháng. Phân tích: khoản nào tăng bất thường, khoản nào cắt được, so sánh tỷ lệ chi phí/doanh thu với chuẩn ngành. Kết quả dạng bảng, đánh dấu khoản cần chú ý.

**Giải thích quy định mới**

> **CÂU LỆNH MẪU:**
> Giải thích [thông tư/nghị định] ảnh hưởng gì đến công ty tôi. Ngành [ngành], doanh thu [khoảng], [số] nhân viên. Tập trung: nghĩa vụ mới, thời hạn, mức xử phạt. Giải thích đơn giản.

### NHÂN SỰ

**Viết mô tả tuyển dụng**

> **CÂU LỆNH MẪU:**
> Viết mô tả công việc cho [vị trí]. Cấp bậc: [mới/có kinh nghiệm/quản lý]. Yêu cầu bắt buộc: [liệt kê]. Quyền lợi: [liệt kê]. Giọng trẻ trung, thu hút.

**Viết đánh giá nhân viên**

> **CÂU LỆNH MẪU:**
> Viết đánh giá cho nhân viên [vị trí], làm [thời gian]. Điểm mạnh: [liệt kê]. Cần cải thiện: [liệt kê]. Giọng công bằng, xây dựng, có đề xuất phát triển 6 tháng tới.

---

## PHỤ LỤC B: TỪ ĐIỂN THUẬT NGỮ AI CHO NGƯỜI KHÔNG CHUYÊN

Khi đọc về AI hoặc dùng các công cụ AI, bạn sẽ gặp một số thuật ngữ tiếng Anh. Dưới đây là giải thích đơn giản:

**AI (Artificial Intelligence)**
Nghĩa đơn giản: Trí tuệ nhân tạo
Phần mềm có khả năng xử lý ngôn ngữ, phân tích dữ liệu và đưa ra câu trả lời giống như con người suy nghĩ. Claude, ChatGPT, Gemini đều là các sản phẩm AI.

**Model (Mô hình AI)**
Nghĩa đơn giản: Bộ não của AI
Mỗi sản phẩm AI có nhiều phiên bản mạnh yếu khác nhau. Ví dụ Claude có: Opus (thông minh nhất), Sonnet (cân bằng), Haiku (nhanh nhất). Chọn phiên bản giống như chọn cấp độ chuyên gia cho từng loại công việc.

**Prompt (Câu lệnh)**
Nghĩa đơn giản: Câu bạn gõ cho AI
Bất kỳ câu nào bạn gõ vào ô trò chuyện để hỏi hoặc yêu cầu AI làm gì đó đều gọi là câu lệnh. Câu lệnh tốt = kết quả tốt.

**Token**
Nghĩa đơn giản: Đơn vị đo lường văn bản của AI
AI chia văn bản thành các mảnh nhỏ gọi là token. Trung bình 1 token khoảng bằng 3/4 từ tiếng Anh. Với tiếng Việt, 1 từ thường chiếm 2-3 token. Token quyết định giới hạn bao nhiêu thông tin AI xử lý được cùng lúc.

**Cửa sổ ngữ cảnh (Context Window)**
Nghĩa đơn giản: Bộ nhớ tạm trong một cuộc trò chuyện
Lượng thông tin tối đa AI 'nhìn thấy' cùng lúc. Claude hỗ trợ khoảng 200,000 token (tầm 500 trang sách). Khi cuộc trò chuyện quá dài, AI bắt đầu 'quên' phần đầu. Xem thêm Phần 3.

**Bộ nhớ (Memory)**
Nghĩa đơn giản: Thông tin Claude nhớ qua các cuộc trò chuyện
Claude có thể ghi nhớ thông tin quan trọng về bạn (tên, công ty, sở thích) để áp dụng trong các cuộc trò chuyện sau. Bạn có thể chủ động ra lệnh ghi nhớ. Xem thêm Phần 3.

**Chế độ suy nghĩ (Thinking Mode)**
Nghĩa đơn giản: Để AI suy nghĩ kỹ trước khi trả lời
Khi bật, Claude dành thời gian phân tích và lập luận trước khi đưa câu trả lời, thay vì trả lời ngay. Hữu ích cho câu hỏi phức tạp.

**Agent (Tác tử AI)**
Nghĩa đơn giản: AI tự thực hiện nhiều bước
Thay vì chỉ trả lời câu hỏi, Agent tự tìm kiếm thông tin, đọc file, tạo tài liệu. Giống như giao việc cho trợ lý biết tự tìm hiểu và hoàn thành.

**Markdown**
Nghĩa đơn giản: Ngôn ngữ viết văn bản có cấu trúc
Cách viết văn bản có tiêu đề, in đậm, danh sách bằng các ký hiệu đơn giản. Bạn không cần học, nhưng biết thì dùng AI hiệu quả hơn.

**Skill (Kỹ năng)**
Nghĩa đơn giản: Bộ hướng dẫn dạy AI làm việc theo cách của bạn
File hướng dẫn tạo một lần, AI tự động áp dụng mỗi khi gặp công việc phù hợp. Xem chi tiết tại Phần 7.

**Project (Dự án)**
Nghĩa đơn giản: Thư mục riêng trong Claude cho một mảng công việc
Nơi lưu thông tin nền, tài liệu, và Skill cho một chủ đề cụ thể. Claude nhớ tất cả thông tin trong Dự án mỗi khi bạn mở cuộc trò chuyện trong đó.

**Ảo giác AI (Hallucination)**
Nghĩa đơn giản: Khi AI tự tin nói sai
Đôi khi AI 'bịa' thông tin nhưng trình bày rất tự tin. Đây là lý do bạn luôn cần kiểm tra kết quả quan trọng.

**Artifact (Sản phẩm trực quan)**
Nghĩa đơn giản: Kết quả Claude hiển thị riêng bên cạnh cuộc trò chuyện
Khi Claude tạo biểu đồ, trang web mẫu, hoặc tài liệu dài, nó hiển thị trong một khung riêng bên phải màn hình để bạn xem trực tiếp.

---

## Tài liệu tham khảo

Các nguồn tài liệu chính thức từ Anthropic (công ty phát triển Claude):
- Hướng dẫn sử dụng Claude: docs.claude.com
- Hướng dẫn viết câu lệnh hiệu quả: docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
- Hướng dẫn tạo và sử dụng Skills: docs.claude.com/en/docs/claude-ai/skills
- Bảng giá Claude: claude.com/pricing
- Trung tâm hỗ trợ: support.claude.com

---

## SEPAY.VN

**Hạ tầng Open Banking cho doanh nghiệp Việt Nam**

### SePay là gì?

SePay cung cấp API ngân hàng giúp doanh nghiệp tự động hóa việc xác nhận thanh toán và quản lý dòng tiền. Thay vì phải mở internet banking ra kiểm tra từng giao dịch, hệ thống của bạn sẽ tự động xác nhận thanh toán ngay khi khách hàng chuyển khoản.

### SePay giải quyết vấn đề gì?

| Vấn đề | Không có SePay | Có SePay |
|--------|---------------|----------|
| Xác nhận thanh toán | Nhân viên phải mở internet banking, kiểm tra từng giao dịch, đối soát thủ công | Hệ thống tự động nhận biết khách đã chuyển khoản, xác nhận trong vài giây |
| Đối soát cuối ngày | Kế toán dành 1-2 giờ mỗi ngày để đối soát giao dịch với đơn hàng | Tự động khớp giao dịch với đơn hàng, kế toán chỉ cần kiểm tra báo cáo |
| Quản lý nhiều tài khoản ngân hàng | Đăng nhập từng ngân hàng riêng, theo dõi rời rạc | Một bảng điều khiển duy nhất cho tất cả tài khoản ngân hàng |
| Sai sót | Nhầm số tiền, bỏ sót giao dịch, khách phàn nàn chậm xác nhận | Tự động 100%, không sai sót, khách hàng được phục vụ nhanh hơn |

### Sản phẩm và dịch vụ

**Dành cho doanh nghiệp:**
- **Cổng thanh toán:** Thanh toán qua VietQR (Open Banking), NAPAS (VietQRPay), và thẻ quốc tế (Visa, Mastercard, JCB). Tích hợp sẵn WooCommerce, Haravan, HostBill
- **Chia sẻ biến động số dư:** Nhận thông báo giao dịch qua Telegram, Lark, Mobile App - không cần đăng nhập internet banking
- **Loa thanh toán:** Thông báo bằng giọng nói khi có giao dịch, phù hợp cho cửa hàng bán lẻ
- **SePay eShop:** Phần mềm bán hàng tích hợp thanh toán và xuất hóa đơn điện tử
- **SePay eInvoice:** Xuất hóa đơn điện tử tự động

**Dành cho lập trình viên:**
- **API và Webhook ngân hàng:** Nhận thông báo giao dịch theo thời gian thực qua API
- **API hóa đơn điện tử:** Tự động xuất hóa đơn từ hệ thống của bạn
- **API loa thanh toán:** Tích hợp thông báo giọng nói vào ứng dụng
- **SePay Bank Hub:** API ngân hàng dành cho công ty phần mềm (CRM, ERP, SaaS, POS)
- **Tài liệu kỹ thuật đầy đủ:** developer.sepay.vn

### Ai nên dùng SePay?

- **Doanh nghiệp bán hàng online:** Tự động xác nhận đơn hàng khi khách chuyển khoản
- **Nền tảng thương mại điện tử:** Tích hợp API thanh toán vào hệ thống
- **Doanh nghiệp có nhiều giao dịch mỗi ngày:** Giảm tải công việc cho kế toán
- **Startup và công ty công nghệ:** API dễ tích hợp, tài liệu kỹ thuật đầy đủ

### SePay trong con số

- Hơn 10 ngân hàng đã kết nối API
- Hàng nghìn doanh nghiệp đang sử dụng
- Xử lý hàng triệu giao dịch mỗi tháng

### Bắt đầu dùng SePay miễn phí

- Truy cập: sepay.vn
- Tài liệu kỹ thuật: developer.sepay.vn
- Liên hệ tư vấn: fb.com/buitanviet (Bùi Tấn Việt - CEO)

---

## LỜI KẾT

AI không phải phép màu. AI là công cụ khuếch đại.

Người giỏi marketing dùng AI sẽ làm marketing giỏi gấp 3 lần. Người giỏi chiến lược dùng AI sẽ phân tích sâu gấp 5 lần. Nhưng AI không thể thay bạn ra quyết định, không thể thay bạn hiểu khách hàng, và không thể thay bạn chịu trách nhiệm.

Bắt đầu từ việc nhỏ: ngày mai, thay vì tự viết email đầu tiên trong ngày, hãy thử nhờ Claude viết nháp trước. Rồi bạn chỉnh sửa. Chỉ cần 1 tuần làm vậy, bạn sẽ thấy sự khác biệt.

**Bùi Tấn Việt - CEO SePay.Vn**

SePay (sepay.vn) - Hạ tầng Open Banking cho doanh nghiệp Việt Nam
123HOST (123host.vn) - Dịch vụ Hosting và Tên miền từ 2012
Facebook: fb.com/buitanviet | Điện thoại: 0903 252 427

*Tài liệu này được viết dựa trên kinh nghiệm dùng Claude thực tế của tôi tại SePay.*
*Phiên bản: Tháng 2/2026*
