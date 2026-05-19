# -*- coding: utf-8 -*-
import argparse
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


DEFAULT_OUT_PATH = Path(
    r"d:\TaiLieu\Data Engineer\DE Roadmap\DE-Learning\interview-prep-html\Data_Architect_Corporate_Banking_Interview_Guide_VN.docx"
)


CONTENT = [
    "TÀI LIỆU ÔN PHỎNG VẤN DATA ARCHITECT - DỰ ÁN MIGRATE CORPORATE BANKING",
    "Phiên bản: 19/05/2026",
    "",
    "MỤC TIÊU TÀI LIỆU",
    "- Chuẩn bị phỏng vấn vị trí Data Architect theo mindset Framework, Methodology và Risk Control.",
    "- Ôn SQL, database concepts, ERD, data migration architecture, reconciliation, cutover và rollback.",
    "- Cung cấp ví dụ thực hành rõ ràng để trả lời câu hỏi tình huống trong phỏng vấn.",
    "",
    "1. HIỂU ĐÚNG VAI TRÒ DATA ARCHITECT TRONG MIGRATION",
    "Data Architect không phải người chỉ viết script ETL, mà là người chịu trách nhiệm thiết kế phương pháp, kiến trúc, tiêu chuẩn kiểm soát và điều phối go-live an toàn.",
    "",
    "Deliverables cốt lõi:",
    "- Data Architecture Blueprint: kiến trúc as-is, to-be, luồng dữ liệu và ranh giới hệ thống.",
    "- Data Model và Mapping Specification: ánh xạ source-to-target, business rules, data type rules.",
    "- Metadata-driven migration framework.",
    "- Reconciliation framework 3 lớp và cơ chế xử lý sai lệch.",
    "- Cutover runbook theo phút và rollback decision matrix.",
    "- Governance artifacts: data quality, lineage, security masking, audit trail.",
    "",
    "2. GIẢI NGHĨA YÊU CẦU JD VÀ CÁCH TRẢ LỜI",
    "- 10+ năm enterprise architecture: thể hiện năng lực chiến lược, tiêu chuẩn và governance.",
    "- Oracle, Exadata, PostgreSQL: nói được tuning, partitioning, CDC, performance ở quy mô lớn.",
    "- Metadata-driven accelerator: cho thấy khả năng scale từ 100 lên 1000 bảng mà không tăng effort tuyến tính.",
    "- Reconciliation framework: đưa ra bằng chứng kiểm soát dữ liệu độc lập với trạng thái ETL.",
    "",
    "3. ERD MẪU CORE BANKING",
    "- CUSTOMER 1-N ACCOUNT 1-N TXN",
    "- ACCOUNT 1-N ACCOUNT_BALANCE_DAILY",
    "- CUSTOMER 1-N KYC_PROFILE",
    "- PRODUCT 1-N ACCOUNT, BRANCH 1-N ACCOUNT",
    "",
    "4. SQL THỰC HÀNH NHANH",
    "SELECT COUNT(*) FROM src.txn WHERE value_date = :biz_date;",
    "SELECT COUNT(*) FROM tgt.txn WHERE value_date = :biz_date;",
    "SELECT SUM(amount) FROM src.txn WHERE value_date = :biz_date;",
    "SELECT SUM(amount) FROM tgt.txn WHERE value_date = :biz_date;",
    "",
    "5. CUTOVER RUNBOOK",
    "- Freeze giao dịch ghi mới trên legacy.",
    "- CDC catch-up vòng cuối.",
    "- Final reconciliation.",
    "- Go/No-Go meeting.",
    "- Switch traffic sang hệ mới.",
    "- Smoke test nghiệp vụ quan trọng.",
    "",
    "6. CÂU TRẢ LỜI MẪU",
    "Migration thành công không phải ETL success, mà là data parity, business sign-off và SLA ổn định sau go-live.",
    "",
    "Ghi chú: file này đã được sinh lại với nội dung UTF-8 chuẩn để hiển thị tiếng Việt đúng trong Word.",
]


def make_paragraph(text: str) -> str:
    if not text:
        return "<w:p/>"
    return (
        "<w:p><w:r><w:rPr>"
        '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>'
        '<w:lang w:val="vi-VN" w:eastAsia="vi-VN" w:bidi="vi-VN"/>'
        '<w:sz w:val="24"/><w:szCs w:val="24"/>'
        "</w:rPr><w:t xml:space=\"preserve\">"
        + escape(text)
        + "</w:t></w:r></w:p>"
    )


document_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 wp14">
  <w:body>
    {paras}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
      <w:cols w:space="708"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
</w:document>
"""


styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>
        <w:lang w:val="vi-VN" w:eastAsia="vi-VN" w:bidi="vi-VN"/>
        <w:sz w:val="24"/>
        <w:szCs w:val="24"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault><w:pPr/></w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
    <w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>
      <w:lang w:val="vi-VN" w:eastAsia="vi-VN" w:bidi="vi-VN"/>
      <w:sz w:val="24"/>
      <w:szCs w:val="24"/>
    </w:rPr>
  </w:style>
</w:styles>
"""


content_types_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>
"""


root_rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""


doc_rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(DEFAULT_OUT_PATH))
    args = parser.parse_args()
    out_path = Path(args.output)

    paras = "".join(make_paragraph(line) for line in CONTENT)
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types_xml)
        zf.writestr("_rels/.rels", root_rels_xml)
        zf.writestr("word/document.xml", document_xml.format(paras=paras))
        zf.writestr("word/styles.xml", styles_xml)
        zf.writestr("word/_rels/document.xml.rels", doc_rels_xml)

    print(out_path)


if __name__ == "__main__":
    main()
