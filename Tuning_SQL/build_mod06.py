# -*- coding: utf-8 -*-
html = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Module 06 — Database Operations & Monitoring</title>
<meta name="description" content="Hướng dẫn vận hành và giám sát Database: Golden Signals, Top SQL, Object Health, Cache/Memory tuning, Backup & Recovery, và Replication Lag trên PostgreSQL, MySQL và Oracle.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:#0d1117;--surface:#161b22;--surface2:#21262d;--border:#30363d;
    --accent:#58a6ff;--accent2:#3fb950;--accent3:#f78166;--accent4:#d2a8ff;--accent5:#ffa657;
    --text:#e6edf3;--text-muted:#8b949e;--code-bg:#0d1117;--highlight:#388bfd26;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Inter','Segoe UI',-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.7}
  .hero{background:linear-gradient(135deg,#0d1117 0%,#161b22 40%,#1a2a1e 100%);border-bottom:2px solid var(--accent4);padding:40px 24px 30px;text-align:center;position:relative;overflow:hidden}
  .hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,#6e40c922,transparent 70%);pointer-events:none}
  .hero h1{font-size:2rem;font-weight:800;color:var(--accent4);letter-spacing:-0.5px}
  .hero p{color:var(--text-muted);margin-top:8px;font-size:.95rem}
  .badge-row{display:flex;gap:8px;justify-content:center;margin-top:14px;flex-wrap:wrap}
  .badge{padding:4px 12px;border-radius:20px;font-size:.75rem;font-weight:600;border:1px solid}
  .badge-blue{color:var(--accent);border-color:var(--accent);background:#1f6feb1a}
  .badge-green{color:var(--accent2);border-color:var(--accent2);background:#2ea04326}
  .badge-orange{color:var(--accent5);border-color:var(--accent5);background:#d2940026}
  .badge-purple{color:var(--accent4);border-color:var(--accent4);background:#6e40c926}
  .container{display:flex;min-height:calc(100vh - 160px)}
  .sidebar{width:290px;min-width:290px;background:var(--surface);border-right:1px solid var(--border);padding:20px 0;position:sticky;top:0;height:100vh;overflow-y:auto}
  .sidebar-title{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--text-muted);padding:0 16px 12px}
  .level-label{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;padding:8px 16px 4px;color:var(--accent4)}
  .nav-item{display:block;padding:7px 16px;cursor:pointer;font-size:.82rem;color:var(--text-muted);border-left:3px solid transparent;transition:all .15s}
  .nav-item:hover{color:var(--text);background:var(--surface2)}
  .nav-item.active{color:var(--accent4);border-left-color:var(--accent4);background:#6e40c915;font-weight:600}
  .nav-number{display:inline-block;width:44px;font-size:.7rem;color:var(--text-muted);font-family:'JetBrains Mono',monospace}
  .main{flex:1;padding:32px 40px;max-width:980px}
  .module{display:none}.module.active{display:block}
  .module-header{border:1px solid var(--border);border-radius:12px;padding:24px 28px;background:var(--surface);margin-bottom:24px;position:relative;overflow:hidden}
  .module-header::before{content:'';position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--accent4)}
  .module-tag{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--accent4);margin-bottom:8px}
  .module-title{font-size:1.6rem;font-weight:800;margin-bottom:8px}
  .module-subtitle{color:var(--text-muted);font-size:.9rem}
  .section{margin-bottom:28px;border:1px solid var(--border);border-radius:10px;overflow:hidden}
  .section-header{padding:14px 20px;font-weight:700;font-size:.9rem;display:flex;align-items:center;gap:10px;cursor:pointer;background:var(--surface2);border-bottom:1px solid var(--border);user-select:none}
  .section-icon{width:28px;height:28px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
  .icon-purpose{background:#1f6feb33}.icon-detail{background:#2ea04326}.icon-quiz{background:#d2940026}.icon-summary{background:#6e40c926}.icon-practice{background:#f7816626}
  .section-content{padding:20px;background:var(--surface)}
  .section-toggle{margin-left:auto;color:var(--text-muted);font-size:12px}
  h3{font-size:1rem;font-weight:700;color:var(--accent4);margin:18px 0 10px}
  h3:first-child{margin-top:0} h3.blue{color:var(--accent)} h3.green{color:var(--accent2)} h3.orange{color:var(--accent5)} h3.red{color:var(--accent3)}
  p{margin-bottom:12px;color:var(--text);font-size:.88rem}
  ul,ol{padding-left:20px;margin-bottom:12px} li{font-size:.88rem;margin-bottom:5px}
  strong{color:var(--text)}
  .cmd-block{background:var(--code-bg);border:1px solid var(--border);border-radius:8px;margin:12px 0;overflow:hidden}
  .cmd-header{display:flex;align-items:center;justify-content:space-between;padding:8px 14px;background:var(--surface2);border-bottom:1px solid var(--border);font-size:.72rem;color:var(--text-muted);font-family:'JetBrains Mono',monospace}
  .cmd-body{padding:14px}
  pre{font-family:'JetBrains Mono','Courier New','Consolas',monospace;font-size:.82rem;line-height:1.6;white-space:pre;overflow-x:auto;color:var(--text)}
  .kw{color:#ff7b72}.kw2{color:var(--accent)}.str{color:var(--accent5)}.fn{color:var(--accent4)}.num{color:#79c0ff}.comment{color:var(--text-muted)}
  .db-tag{display:inline-block;padding:2px 8px;border-radius:4px;font-size:.68rem;font-weight:700;letter-spacing:.5px;margin-bottom:6px;margin-right:4px}
  .db-pg{background:#4169e122;color:#4d9de0;border:1px solid #4169e155}.db-my{background:#f0931322;color:#f09313;border:1px solid #f0931355}.db-oracle{background:#cc000022;color:#f97316;border:1px solid #cc000055}
  code{font-family:'JetBrains Mono',monospace;background:var(--surface2);border:1px solid var(--border);padding:1px 6px;border-radius:4px;font-size:.82rem;color:var(--accent4)}
  
  .tab-group{display:flex;gap:4px;margin:14px 0 0;border-bottom:2px solid var(--border)}
  .tab{padding:7px 16px;border-radius:6px 6px 0 0;cursor:pointer;font-size:.78rem;font-weight:600;color:var(--text-muted);transition:all .15s;border:1px solid transparent;border-bottom:none;margin-bottom:-2px}
  .tab:hover{color:var(--text);background:var(--surface2)}
  .tab.active{color:var(--accent4);background:var(--surface);border-color:var(--border);border-bottom-color:var(--surface)}
  .tab-content{display:none;padding-top:4px}
  .tab-content.active{display:block}

  .quiz-item{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:16px;margin-bottom:12px}
  .quiz-q{font-weight:600;font-size:.88rem;margin-bottom:10px}
  .quiz-q::before{content:'Q';display:inline-block;width:22px;height:22px;background:var(--accent4);color:#000;border-radius:50%;font-size:.7rem;font-weight:800;text-align:center;line-height:22px;margin-right:8px}
  .quiz-options{display:flex;flex-direction:column;gap:6px;margin-bottom:10px}
  .quiz-opt{padding:8px 12px;border:1px solid var(--border);border-radius:6px;cursor:pointer;font-size:.84rem;transition:all .15s;background:var(--bg)}
  .quiz-opt:hover{border-color:var(--accent4);color:var(--accent4)}
  .quiz-opt.correct{border-color:var(--accent2);color:var(--accent2);background:#2ea04310}
  .quiz-opt.wrong{border-color:var(--accent3);color:var(--accent3);background:#f7816610}
  .quiz-explain{font-size:.82rem;color:var(--text-muted);border-top:1px solid var(--border);padding-top:10px;margin-top:8px;display:none}
  .quiz-explain.show{display:block}

  .summary-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
  .summary-item{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:12px;font-size:.82rem}
  .summary-item strong{color:var(--accent4);display:block;margin-bottom:4px}
  
  .practice-task{background:var(--surface2);border:1px solid var(--border);border-radius:8px;margin-bottom:16px;overflow:hidden}
  .practice-task-header{padding:12px 16px;background:#6e40c915;border-bottom:1px solid var(--border);font-weight:700;font-size:.85rem;color:var(--accent4)}
  .practice-task-body{padding:16px}
  
  .solution-toggle{display:inline-flex;align-items:center;gap:6px;background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:6px 14px;font-size:.8rem;cursor:pointer;color:var(--accent2);margin-top:10px;transition:all .15s}
  .solution-toggle:hover{background:var(--surface2)}
  .solution-box{margin-top:10px;display:none;border-top:1px solid var(--border);padding-top:12px}
  .solution-box.show{display:block}
  
  .info-box{border-radius:8px;padding:14px 16px;margin:12px 0;font-size:.84rem;border:1px solid;display:flex;gap:10px}
  .info-box.tip{border-color:var(--accent2);background:#2ea04310;color:var(--accent2)}
  .info-box.warn{border-color:var(--accent5);background:#d2940015;color:var(--accent5)}
  .info-box.note{border-color:var(--accent4);background:#6e40c915;color:var(--accent4)}
  .info-box.danger{border-color:var(--accent3);background:#f7816610;color:var(--accent3)}
  .info-box span{color:var(--text)}
  
  .progress-bar{background:var(--surface2);border-radius:4px;height:4px;margin:16px 0;overflow:hidden}
  .progress-fill{height:100%;background:linear-gradient(90deg,var(--accent4),var(--accent2));border-radius:4px;width:0;transition:width .2s}
  .nav-buttons{display:flex;gap:12px;margin-top:32px;justify-content:space-between}
  .nav-btn{padding:10px 20px;border-radius:8px;border:1px solid var(--border);background:var(--surface2);color:var(--text);cursor:pointer;font-size:.85rem;font-weight:600;transition:all .15s;display:flex;align-items:center;gap:6px}
  .nav-btn:hover{border-color:var(--accent4);color:var(--accent4)}
  .nav-btn.primary{background:var(--accent4);color:#000;border-color:var(--accent4)}
  .nav-btn.primary:hover{background:#e2c0ff}
  
  table{width:100%;border-collapse:collapse;margin:12px 0;font-size:.83rem}
  th{background:var(--surface2);padding:8px 12px;text-align:left;border:1px solid var(--border);color:var(--accent4)}
  td{padding:8px 12px;border:1px solid var(--border)}
  tr:nth-child(even) td{background:#ffffff05}
  
  .mental-model{border-left:4px solid var(--accent);background:#1f6feb1a;padding:12px 14px;border-radius:6px;margin:12px 0;font-size:.88rem}
  .checklist-row{display:flex;align-items:flex-start;gap:10px;margin-bottom:8px}
  .check-box{width:16px;height:16px;border:1px solid var(--border);border-radius:3px;flex-shrink:0;margin-top:.25rem;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center}
  .check-box.checked{background:var(--accent2);border-color:var(--accent2)}
  .check-box.checked::after{content:'\u2713';font-size:10px;color:#000;font-weight:600}
  .progress-text{font-size:.8rem;color:var(--text-muted);margin-bottom:8px}
  @media(max-width:768px){.sidebar{display:none}.main{padding:16px}.summary-grid{grid-template-columns:1fr}}
</style>
</head>
<body>

<div class="hero">
  <h1>Module 06 — Database Operations & Monitoring</h1>
  <p>Vận hành database thực chiến: Giám sát chủ động, bảo trì sức khỏe bảng/index, chẩn đoán tài nguyên, chiến lược backup an toàn và quản lý hạ tầng Replication.</p>
  <div class="badge-row">
    <span class="badge badge-purple">DBA Operations</span>
    <span class="badge badge-green">~5–7 ngày</span>
    <span class="badge badge-blue">Production Observability</span>
    <span class="badge badge-orange">PostgreSQL · MySQL · Oracle</span>
  </div>
</div>

<div class="container">
  <nav class="sidebar">
    <div class="sidebar-title">Module Navigation</div>
    <div class="level-label">MODULE 06 · OPERATIONS</div>
    <div class="nav-item active" onclick="showModule(0,this)"><span class="nav-number">S0</span>Tổng quan & Mục tiêu</div>
    <div class="nav-item" onclick="showModule(1,this)"><span class="nav-number">S1</span>Monitoring nền tảng</div>
    <div class="nav-item" onclick="showModule(2,this)"><span class="nav-number">S2</span>Slow Query & SQL Stats</div>
    <div class="nav-item" onclick="showModule(3,this)"><span class="nav-number">S3</span>Table/Index Health</div>
    <div class="nav-item" onclick="showModule(4,this)"><span class="nav-number">S4</span>Cache, Memory & I/O</div>
    <div class="nav-item" onclick="showModule(5,this)"><span class="nav-number">S5</span>Backup & Restore Drill</div>
    <div class="nav-item" onclick="showModule(6,this)"><span class="nav-number">S6</span>Replication & Capacity</div>
    <div class="nav-item" onclick="showModule(7,this)"><span class="nav-number">S7</span>Interview Prep</div>
    <div class="nav-item" onclick="showModule(8,this)"><span class="nav-number">S8</span>Checklist & Tổng kết</div>
  </nav>

  <main class="main">

    <!-- S0: Orientation -->
    <div class="module active" id="s0">
      <div class="module-header">
        <div class="module-tag">S0 · Orientation</div>
        <div class="module-title">Tổng quan & Mục tiêu Module 06</div>
        <div class="module-subtitle">Tuning từng query giúp chữa cháy tức thì. Thiết lập quy trình Operations & Monitoring giúp hệ thống hoạt động ổn định 24/7/365.</div>
      </div>
      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-summary">M</span>Roadmap 9 sections của module<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <table>
            <thead><tr><th>Section</th><th>Tên section</th><th>Trọng tâm</th></tr></thead>
            <tbody>
              <tr><td>S0</td><td>Tổng quan & Mục tiêu</td><td>Triết lý vận hành chủ động vs Phản ứng bị động</td></tr>
              <tr><td>S1</td><td>Monitoring nền tảng</td><td>5 Golden signals, dashboard, thiết lập Alert không gây nhiễu</td></tr>
              <tr><td>S2</td><td>Slow Query & SQL Stats</td><td>Top SQL theo Total Impact, cấu hình Slow Query Log & Session Trace</td></tr>
              <tr><td>S3</td><td>Table/Index Health</td><td>Xử lý Bloat, dọn dẹp Index thừa (overlapping), Invisible Index & Thu thập Stats</td></tr>
              <tr><td>S4</td><td>Cache, Memory & I/O</td><td>Tính toán Cache Hit, cấu hình work_mem, sort_buffer_size và Temp spill</td></tr>
              <tr><td>S5</td><td>Backup & Restore Drill</td><td>SLA về RTO/RPO, lệnh sao lưu vật lý/logic và quy trình Restore Drill bắt buộc</td></tr>
              <tr><td>S6</td><td>Replication & Capacity</td><td>Chẩn đoán lag replication, xử lý lag read-after-write và capacity planning</td></tr>
              <tr><td>S7</td><td>Interview Prep</td><td>Bộ câu hỏi Quick Quiz + Senior Triage Scenarios thực chiến</td></tr>
              <tr><td>S8</td><td>Checklist & Tổng kết</td><td>Definition of Done đánh giá năng lực Junior DBA / Senior Developer</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      
      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-purpose">O</span>Operations giải quyết vấn đề gì?<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <h3 class="blue">Tuning là phản ứng lâm sàng, Operations là theo dõi nhịp tim sinh học</h3>
          <p>Query tuning xử lý sự cố cụ thể khi người dùng than phiền. Operations & Monitoring giúp DBA quan sát toàn cục, nhận biết xu hướng suy giảm hiệu năng từ sớm để can thiệp trước khi hệ thống sụp đổ.</p>
          <div class="mental-model"><strong>Mental model:</strong> Database production là một thực thể sống. Nếu không đo lường các Golden Signals, bạn sẽ chỉ phát hiện ra tim nó ngừng đập khi đã quá muộn để hồi sức cấp cứu.</div>
          
          <h3 class="orange">Hậu quả nghiêm trọng khi thiếu Operations</h3>
          <ul>
            <li><strong>Mất kiểm soát tài nguyên:</strong> Không biết query nào chiếm 80% I/O và CPU của cả hệ thống tuần qua.</li>
            <li><strong>Chủ quan về an toàn dữ liệu:</strong> Script backup báo thành công hàng ngày nhưng khi restore bị crash do database corruption hoặc thiếu WAL/Redo log.</li>
            <li><strong>Sự cố gián đoạn bất ngờ:</strong> Ổ đĩa đầy trong vòng 10 phút vì table/index bloat hoặc log ghi đè dữ liệu.</li>
            <li><strong>Nghiệp vụ bị sai lệch:</strong> Read replica bị lag nghiêm trọng dẫn đến app đọc dữ liệu cũ mà không hề hay biết để định tuyến lại.</li>
          </ul>
        </div>
      </div>
      
      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">🔁</span>Incidents Triage & Resolution Process Flow<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <div class="cmd-block">
            <div class="cmd-header"><span>● ● ●</span><span>incident-lifecycle-flow.txt</span></div>
            <div class="cmd-body">
<pre><span class="kw2">[1. Alert Triggered]</span> ──► <span class="str">Sự cố phát sinh (p99 Latency > 2s hoặc Disk Free < 15%)</span>
       │
       ▼
<span class="kw2">[2. Golden Signals Check]</span> ──► <span class="str">Xác định bottleneck: CPU bão hòa, I/O wait tăng hay Connection Storm?</span>
       │
       ▼
<span class="kw2">[3. SQL Stats Triage]</span> ──► <span class="str">Tìm thủ phạm: Chạy Top SQL query có total execution time đột biến</span>
       │
       ▼
<span class="kw2">[4. Object/Memory Fix]</span> ──► <span class="str">Hành động: Dọn dẹp index thừa, Analyze stats stale, tăng sort memory tạm thời</span>
       │
       ▼
<span class="kw2">[5. Verify & Document]</span> ──► <span class="str">Kiểm chứng metrics hạ nhiệt, viết Post-mortem, bổ sung Runbook</span></pre>
            </div>
          </div>
        </div>
      </div>
      
      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-practice">✅</span>Exit criteria: "Bạn đã nắm vững module này khi..."<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <ul>
            <li>Thiết lập được Dashboard giám sát tối thiểu cho production dựa trên 5 Golden Signals.</li>
            <li>Tự tay truy vấn danh sách <strong>Top SQL</strong> ngốn tài nguyên nhất trên cả PostgreSQL, MySQL và Oracle.</li>
            <li>Xác định và dọn dẹp các <strong>Index không sử dụng (unused index)</strong>, kiểm soát an toàn qua <strong>Invisible Index</strong> theo đúng tài liệu chuẩn.</li>
            <li>Đọc hiểu dấu hiệu quá tải bộ nhớ và temp spill để điều chỉnh `work_mem` và `sort_buffer_size`.</li>
            <li>Hiểu sâu về backup SLA, tự viết quy trình <strong>Restore Drill</strong> để chứng minh tính sẵn sàng của dữ liệu.</li>
            <li>Đo lường và tính toán chính xác <strong>Replication Lag</strong> trên môi trường Master-Slave.</li>
          </ul>
        </div>
      </div>

      <div class="nav-buttons"><button class="nav-btn" disabled>← Trước</button><button class="nav-btn primary" onclick="nextModule()">Bắt đầu →</button></div>
    </div>

    <!-- S1: Monitoring Foundations -->
    <div class="module" id="s1">
      <div class="module-header">
        <div class="module-tag">S1 · Monitoring Foundations</div>
        <div class="module-title">Thiết lập Monitoring nền tảng cho DBA</div>
        <div class="module-subtitle">Giám sát hiệu quả bằng cách bắt đầu với nhóm chỉ số quan trọng, thiết lập Alert thông minh có Runbook đi kèm.</div>
      </div>
      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">G</span>5 Golden Signals của Database<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Không nên thu thập tràn lan hàng trăm chỉ số gây loãng. Một DBA Senior luôn tập trung vào 5 nhóm tín hiệu vàng sau:</p>
          <table>
            <thead><tr><th>Signal</th><th>Metric cụ thể cần đo</th><th>Mục đích giám sát</th></tr></thead>
            <tbody>
              <tr><td><strong>Latency (Trễ)</strong></td><td>p95, p99 duration của query và transaction</td><td>Người dùng có đang bị nghẽn và chậm trễ không?</td></tr>
              <tr><td><strong>Traffic (Lưu lượng)</strong></td><td>QPS (Queries/s), TPS (Transactions/s), Active Sessions</td><td>Hệ thống đang phải gánh tải bao nhiêu?</td></tr>
              <tr><td><strong>Errors (Lỗi)</strong></td><td>Tần suất Deadlocks, Connection Timeouts, ORA errors, Replication Errors</td><td>Có bất thường về mặt logic hoặc hạ tầng vật lý không?</td></tr>
              <tr><td><strong>Saturation (Bão hòa)</strong></td><td>CPU %, Disk I/O wait, Mem Swap %, PGA/Temp tablespace usage</td><td>Tài nguyên nào đang chạm ngưỡng giới hạn vật lý?</td></tr>
              <tr><td><strong>Growth (Tăng trưởng)</strong></td><td>Table/Index Size growth per day, WAL/Redo generation rate</td><td>Khi nào đĩa sẽ đầy? Lập kế hoạch Capacity Planning.</td></tr>
            </tbody>
          </table>
          <div class="info-box tip">✅ <span><strong>Best Practice:</strong> Setup dashboard tối giản hiển thị 5 nhóm tín hiệu trên tại màn hình trung tâm NOC. Chỉ số Latency p99 phản ánh trải nghiệm thực tế tốt nhất của người dùng cuối.</span></div>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">A</span>Xây dựng Alert không gây nhiễu (Alert Fatigue)<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Sai lầm của Junior là đặt alert vào mọi CPU spike 10 giây. Điều này gây nhiễu (alert fatigue), làm đội vận hành phớt lờ cảnh báo thật.</p>
          <h3 class="blue">Quy tắc vàng khi cấu hình Alert</h3>
          <ul>
            <li><strong>Ngưỡng thời gian (Duration Threshold):</strong> Không alert vì CPU chạm 95% trong 10 giây. Hãy alert khi CPU duy trì trên 85% trong liên tục 3-5 phút.</li>
            <li><strong>Alert theo triệu chứng của người dùng (Symptom-based Alert):</strong> Alert khi tỉ lệ query bị lỗi > 1% hoặc p99 latency vượt quá 1000ms. Cảnh báo bão hòa tài nguyên (CPU, Memory) chỉ nên là phụ trợ.</li>
            <li><strong>Bắt buộc có Runbook:</strong> Mỗi cảnh báo được gửi đi (Slack/Telegram/PagerDuty) phải chứa đường link trỏ tới tài liệu Runbook tương ứng, hướng dẫn cụ thể cách kiểm tra và lệnh khắc phục.</li>
          </ul>
        </div>
      </div>
      <div class="nav-buttons"><button class="nav-btn" onclick="prevModule()">← Trước</button><button class="nav-btn primary" onclick="nextModule()">Tiếp →</button></div>
    </div>

    <!-- S2: Slow Query & SQL Stats -->
    <div class="module" id="s2">
      <div class="module-header">
        <div class="module-tag">S2 · SQL Observability</div>
        <div class="module-title">Slow Query & SQL Statistics</div>
        <div class="module-subtitle">Thủ phạm nguy hiểm nhất không phải lúc nào cũng là query chạy lâu nhất. Một query tốn 20ms nhưng gọi 10 triệu lần/ngày có thể nuốt trọn băng thông CPU/I/O của server.</div>
      </div>
      
      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">S</span>Truy tìm Top SQL ngốn tài nguyên nhất<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>DBA Senior sắp xếp mức độ ưu tiên tối ưu dựa trên <strong>Total Impact</strong> (Tổng thời gian = Số lần gọi x Thời gian trung bình) và lượng I/O đọc từ đĩa.</p>
          
          <div class="tab-group" id="tabs-topsql">
            <div class="tab active" onclick="switchTab('tabs-topsql','topsql-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-topsql','topsql-my')">MySQL</div>
            <div class="tab" onclick="switchTab('tabs-topsql','topsql-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="topsql-pg">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>top-sql-postgres.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Yêu cầu bật extension pg_stat_statements trong postgresql.conf</span>
<span class="kw">SELECT</span> 
  queryid,
  calls,
  <span class="fn">round</span>(total_exec_time::numeric / <span class="num">1000</span>, <span class="num">2</span>) <span class="kw">AS</span> total_sec,
  <span class="fn">round</span>(mean_exec_time::numeric, <span class="num">2</span>) <span class="kw">AS</span> mean_ms,
  shared_blks_read + shared_blks_written <span class="kw">AS</span> total_io_blocks,
  query
<span class="kw">FROM</span> pg_stat_statements
<span class="kw">ORDER BY</span> total_exec_time <span class="kw">DESC</span>
<span class="kw">LIMIT</span> <span class="num">15</span>;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="topsql-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>top-sql-mysql.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Sử dụng Performance Schema thu thập thống kê SQL</span>
<span class="kw">SELECT</span> 
  digest_text <span class="kw">AS</span> query,
  count_star <span class="kw">AS</span> calls,
  <span class="fn">round</span>(sum_timer_wait / <span class="num">1000000000000</span>, <span class="num">2</span>) <span class="kw">AS</span> total_sec,
  <span class="fn">round</span>(avg_timer_wait / <span class="num">1000000000</span>, <span class="num">2</span>) <span class="kw">AS</span> avg_ms,
  sum_select_full_join,
  sum_no_index_used
<span class="kw">FROM</span> performance_schema.events_statements_summary_by_digest
<span class="kw">ORDER BY</span> sum_timer_wait <span class="kw">DESC</span>
<span class="kw">LIMIT</span> <span class="num">15</span>;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="topsql-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>top-sql-oracle.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Truy vấn từ V$SQL hiển thị chi tiết tài nguyên tiêu thụ</span>
<span class="kw">SELECT</span> 
  sql_id,
  executions <span class="kw">AS</span> calls,
  <span class="fn">round</span>(elapsed_time / <span class="num">1000000</span>, <span class="num">2</span>) <span class="kw">AS</span> total_elapsed_sec,
  <span class="fn">round</span>(cpu_time / <span class="num">1000000</span>, <span class="num">2</span>) <span class="kw">AS</span> total_cpu_sec,
  buffer_gets <span class="kw">AS</span> logical_reads,
  disk_reads <span class="kw">AS</span> physical_reads,
  sql_text
<span class="kw">FROM</span> v$sql
<span class="kw">WHERE</span> executions &gt; <span class="num">0</span>
<span class="kw">ORDER BY</span> elapsed_time <span class="kw">DESC</span>
<span class="kw">FETCH FIRST</span> <span class="num">15</span> <span class="kw">ROWS ONLY</span>;</pre>
              </div>
            </div>
          </div>
          <div class="info-box note">📌 <span><strong>Phân tích chuyên sâu:</strong> Khi review Top SQL, nếu <code>sum_no_index_used</code> (MySQL) cao hoặc <code>physical_reads</code> (Oracle) chiếm tỉ lệ lớn, chứng tỏ query đó đang quét toàn bộ dữ liệu trên ổ cứng do thiếu Index thích hợp.</span></div>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">L</span>Cấu hình Slow Query Log & Session Trace<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Kích hoạt Slow Query Log là bắt buộc để phát hiện sớm các query bị suy thoái hiệu năng trong production.</p>
          
          <div class="tab-group" id="tabs-slowlog">
            <div class="tab active" onclick="switchTab('tabs-slowlog','slowlog-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-slowlog','slowlog-my')">MySQL</div>
            <div class="tab" onclick="switchTab('tabs-slowlog','slowlog-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="slowlog-pg">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>postgresql.conf</span></div>
              <div class="cmd-body">
<pre><span class="comment"># Cấu hình log các query chạy quá 500ms</span>
log_min_duration_statement = <span class="num">500</span>  <span class="comment"># đơn vị: millisecond</span>

<span class="comment"># Log thêm thông tin về khóa hàng đợi và deadlock</span>
log_lock_waits = <span class="kw">on</span>
deadlock_timeout = <span class="num">1000</span>  <span class="comment"># 1 giây</span></pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="slowlog-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>slow-query.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Bật log slow query và cấu hình ngưỡng 0.5 giây</span>
<span class="kw">SET GLOBAL</span> slow_query_log = <span class="str">'ON'</span>;
<span class="kw">SET GLOBAL</span> long_query_time = <span class="num">0.5</span>;
<span class="comment">-- Log cả các query không dùng index để dọn dẹp</span>
<span class="kw">SET GLOBAL</span> log_queries_not_using_indexes = <span class="str">'ON'</span>;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="slowlog-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>session-trace.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Oracle sử dụng cơ chế DBMS_MONITOR để kích hoạt SQL Trace</span>
<span class="comment">-- 1. Bật trace cho session hiện tại:</span>
<span class="kw">EXEC</span> <span class="fn">DBMS_MONITOR.SESSION_TRACE_ENABLE</span>(waits =&gt; <span class="kw">TRUE</span>, binds =&gt; <span class="kw">TRUE</span>);

<span class="comment">-- 2. Bật trace cho session cụ thể trên hệ thống (dựa vào SID, SERIAL#):</span>
<span class="kw">EXEC</span> <span class="fn">DBMS_MONITOR.SESSION_TRACE_ENABLE</span>(session_id =&gt; <span class="num">142</span>, serial_num =&gt; <span class="num">9584</span>, waits =&gt; <span class="kw">TRUE</span>);</pre>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-buttons"><button class="nav-btn" onclick="prevModule()">← Trước</button><button class="nav-btn primary" onclick="nextModule()">Tiếp →</button></div>
    </div>

    <!-- S3: Table/Index Health -->
    <div class="module" id="s3">
      <div class="module-header">
        <div class="module-tag">S3 · Object Health</div>
        <div class="module-title">Table, Index Health & Statistics Freshness</div>
        <div class="module-subtitle">Cấu trúc dữ liệu bị lão hóa theo thời gian: phình to (bloat), phân mảnh (fragmentation), và statistics bị lỗi thời khiến Optimizer đưa ra những plan thảm họa.</div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">I</span>Truy quét Index không sử dụng (Unused Index)<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Mỗi index thừa đều tiêu hao tài nguyên ổ đĩa và làm chậm các câu lệnh ghi (DML) nghiêm trọng. Dưới đây là các câu lệnh dò tìm index dư thừa chuẩn từ PDF và Oracle SQL:</p>
          
          <div class="tab-group" id="tabs-unusedidx">
            <div class="tab active" onclick="switchTab('tabs-unusedidx','unusedidx-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-unusedidx','unusedidx-my')">MySQL</div>
            <div class="tab" onclick="switchTab('tabs-unusedidx','unusedidx-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="unusedidx-pg">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>find-unused-postgres.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Truy vấn chuẩn từ trang 65-66 của PDF: tìm các index chưa từng quét</span>
<span class="kw">SELECT</span>
  schemaname <span class="kw">AS</span> schema,
  tablename <span class="kw">AS</span> bang_du_lieu,
  indexrelname <span class="kw">AS</span> ten_index,
  idx_scan <span class="kw">AS</span> so_lan_quet,
  idx_tup_read <span class="kw">AS</span> so_dong_doc
<span class="kw">FROM</span> pg_stat_all_indexes
<span class="kw">WHERE</span> schemaname <span class="kw">NOT IN</span> (<span class="str">'pg_catalog'</span>, <span class="str">'information_schema'</span>)
  <span class="kw">AND</span> idx_scan = <span class="num">0</span>
<span class="kw">ORDER BY</span> idx_scan <span class="kw">ASC</span>;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="unusedidx-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>find-unused-mysql.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Sử dụng Performance Schema tìm index không dùng (Trang 65 PDF)</span>
<span class="kw">SELECT</span>
  object_schema <span class="kw">AS</span> 'database',
  object_name <span class="kw">AS</span> 'bang_du_lieu',
  index_name <span class="kw">AS</span> 'ten_index',
  count_star <span class="kw">AS</span> 'so_lan_su_dung'
<span class="kw">FROM</span> performance_schema.table_io_waits_summary_by_index_usage
<span class="kw">WHERE</span> object_schema <span class="kw">NOT IN</span> (<span class="str">'mysql'</span>, <span class="str">'performance_schema'</span>)
  <span class="kw">AND</span> index_name <span class="kw">IS NOT NULL</span>
  <span class="kw">AND</span> index_name &lt;&gt; <span class="str">'PRIMARY'</span>
  <span class="kw">AND</span> count_star = <span class="num">0</span>
<span class="kw">ORDER BY</span> count_star <span class="kw">ASC</span>;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="unusedidx-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>find-unused-oracle.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- 1. Sử dụng tính năng giám sát thủ công (Monitoring Usage)</span>
<span class="kw">ALTER INDEX</span> idx_orders_customer_id <span class="kw">MONITORING USAGE</span>;
<span class="kw">SELECT</span> index_name, table_name, monitoring, used <span class="kw">FROM</span> v$object_usage;
<span class="kw">ALTER INDEX</span> idx_orders_customer_id <span class="kw">NOMONITORING USAGE</span>;

<span class="comment">-- 2. Oracle 12.2+: Tận dụng bảng thống kê tự động DBA_INDEX_USAGE</span>
<span class="kw">SELECT</span> owner, index_name, table_name, total_access_count, total_exec_count, last_used
<span class="kw">FROM</span> dba_index_usage
<span class="kw">WHERE</span> owner = <span class="str">'APP'</span> <span class="kw">AND</span> total_access_count = <span class="num">0</span>;</pre>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">V</span>Ẩn Index an toàn (Invisible Index) để loại trừ rủi ro<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Xóa ngay một index có nguy cơ gây plan regression nặng nề. Do đó, DBA Senior luôn ẩn index trước khi xóa thật để kiểm chứng (theo nguyên lý an toàn trang 66 PDF):</p>
          
          <div class="tab-group" id="tabs-invisible">
            <div class="tab active" onclick="switchTab('tabs-invisible','invisible-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-invisible','invisible-my')">MySQL</div>
            <div class="tab" onclick="switchTab('tabs-invisible','invisible-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="invisible-pg">
            <p>PostgreSQL hiện <strong>chưa hỗ trợ</strong> tính năng Invisible Index trực tiếp. Tuy nhiên, ta có hai giải pháp an toàn tương đương:</p>
            <ul>
              <li><strong>Giải pháp 1:</strong> Đổi tên index sang định dạng backup rồi chạy <code>REINDEX</code> trước khi DROP.</li>
              <li><strong>Giải pháp 2:</strong> Tạo một bản backup Schema. Chạy câu lệnh <code>DROP INDEX CONCURRENTLY</code> trong giờ thấp tải để tránh block lock ghi.</li>
            </ul>
          </div>

          <div class="tab-content" id="invisible-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>invisible-index-mysql.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- 1. Chuyển index sang trạng thái Invisible (Trang 66 PDF)</span>
<span class="kw">ALTER TABLE</span> users <span class="kw">ALTER INDEX</span> idx_user_status <span class="kw">INVISIBLE</span>;
<span class="comment">-- Optimizer sẽ bỏ qua index này, nhưng DML vẫn cập nhật dữ liệu bình thường.</span>

<span class="comment">-- 2. Theo dõi 1-2 tuần. Nếu không có query nào bị chậm đi, xóa vĩnh viễn:</span>
<span class="kw">DROP INDEX</span> idx_user_status <span class="kw">ON</span> users;

<span class="comment">-- 3. Nếu xảy ra lỗi regression lập tức hiển thị lại chỉ trong 1 giây:</span>
<span class="kw">ALTER TABLE</span> users <span class="kw">ALTER INDEX</span> idx_user_status <span class="kw">VISIBLE</span>;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="invisible-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>invisible-index-oracle.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Oracle hỗ trợ native tính năng Invisible Index rất mạnh mẽ</span>
<span class="comment">-- 1. Chuyển trạng thái index thành INVISIBLE</span>
<span class="kw">ALTER INDEX</span> idx_orders_status <span class="kw">INVISIBLE</span>;

<span class="comment">-- 2. Bạn có thể cho phép riêng session của DBA dùng thử index này để kiểm chứng:</span>
<span class="kw">ALTER SESSION SET</span> optimizer_use_invisible_indexes = <span class="kw">TRUE</span>;

<span class="comment">-- 3. Phục hồi ngay lập tức nếu hệ thống gặp lỗi:</span>
<span class="kw">ALTER INDEX</span> idx_orders_status <span class="kw">VISIBLE</span>;</pre>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">B</span>Bloat & Thu hoạch Statistics Freshness<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <div class="info-box warn">⚠️ <span><strong>Quy tắc thực tế (PDF trang 42):</strong> Luôn chạy <code>ANALYZE</code> sau khi hoàn thành các thay đổi dữ liệu lớn (bulk changes/batch load) để cung cấp phân phối mới nhất cho Optimizer.</span></div>
          
          <div class="tab-group" id="tabs-freshness">
            <div class="tab active" onclick="switchTab('tabs-freshness','freshness-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-freshness','freshness-my')">MySQL</div>
            <div class="tab" onclick="switchTab('freshness-my','freshness-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="freshness-pg">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>bloat-pg.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Xem tỉ lệ dead tuple (bloat) trong PostgreSQL</span>
<span class="kw">SELECT</span> relname, n_live_tup, n_dead_tup,
       <span class="fn">round</span>(n_dead_tup * <span class="num">100</span> / <span class="fn">nullif</span>(n_live_tup + n_dead_tup, <span class="num">0</span>), <span class="num">2</span>) <span class="kw">AS</span> bloat_pct,
       last_vacuum, last_autovacuum
<span class="kw">FROM</span> pg_stat_user_tables
<span class="kw">ORDER BY</span> n_dead_tup <span class="kw">DESC</span>;

<span class="comment">-- Chạy phân tích thu thập stats thủ công (SKIP_LOCKED tránh block query) (PDF trang 42)</span>
<span class="kw">ANALYZE</span> users;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="freshness-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>analyze-mysql.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Cập nhật lại phân phối dữ liệu cho bảng của MySQL (PDF trang 42)</span>
<span class="kw">ANALYZE TABLE</span> users;

<span class="comment">-- Thu dọn phân mảnh ổ đĩa và lấy lại khoảng trống từ bảng InnoDB (Duyệt lại block)</span>
<span class="kw">OPTIMIZE TABLE</span> users;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="freshness-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>stats-oracle.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Thu thập stats cho bảng lớn của Oracle</span>
<span class="kw">BEGIN</span>
  <span class="fn">DBMS_STATS.GATHER_TABLE_STATS</span>(
    ownname =&gt; <span class="str">'APP'</span>,
    tabname =&gt; <span class="str">'ORDERS'</span>,
    cascade =&gt; <span class="kw">TRUE</span>,
    estimate_percent =&gt; <span class="fn">DBMS_STATS.AUTO_SAMPLE_SIZE</span>
  );
<span class="kw">END</span>;
/

<span class="comment">-- Dò tìm các bảng đang có statistics bị cũ (stale)</span>
<span class="kw">SELECT</span> owner, table_name, stale_stats, last_analyzed
<span class="kw">FROM</span> dba_tab_statistics
<span class="kw">WHERE</span> owner = <span class="str">'APP'</span> <span class="kw">AND</span> stale_stats = <span class="str">'YES'</span>;</pre>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-buttons"><button class="nav-btn" onclick="prevModule()">← Trước</button><button class="nav-btn primary" onclick="nextModule()">Tiếp →</button></div>
    </div>

    <!-- S4: Cache, Memory & I/O -->
    <div class="module" id="s4">
      <div class="module-header">
        <div class="module-tag">S4 · Resource Health</div>
        <div class="module-title">Cache, Memory & I/O Observability</div>
        <div class="module-subtitle">Nghẽn cổ chai tài nguyên phần cứng làm tê liệt hiệu năng: Cache miss kéo tụt tốc độ, trong khi Temp Spill gây quá tải I/O ổ đĩa trầm trọng.</div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">C</span>Chẩn đoán Buffer Cache Hit Ratio<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Buffer Cache lưu trữ các block dữ liệu được truy cập thường xuyên trên RAM. Tỉ lệ hit ratio > 98% cho thấy database của bạn đang vận hành ổn định trong bộ nhớ vật lý.</p>
          
          <div class="tab-group" id="tabs-cachehit">
            <div class="tab active" onclick="switchTab('tabs-cachehit','cachehit-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-cachehit','cachehit-my')">MySQL</div>
            <div class="tab" onclick="switchTab('tabs-cachehit','cachehit-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="cachehit-pg">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>cache-ratio-pg.sql</span></div>
              <div class="cmd-body">
<pre><span class="kw">SELECT</span> datname,
       blks_hit,
       blks_read,
       <span class="fn">round</span>(blks_hit * <span class="num">100.0</span> / <span class="fn">nullif</span>(blks_hit + blks_read, <span class="num">0</span>), <span class="num">2</span>) <span class="kw">AS</span> cache_hit_pct
<span class="kw">FROM</span> pg_stat_database
<span class="kw">WHERE</span> datname = <span class="str">'appdb'</span>;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="cachehit-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>cache-ratio-mysql.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Xem tỉ lệ hit ratio của InnoDB Buffer Pool</span>
<span class="kw">SHOW GLOBAL STATUS LIKE</span> <span class="str">'Innodb_buffer_pool_read%'</span>;
<span class="comment">-- Thức tính: Hit Ratio = (Innodb_buffer_pool_read_requests - Innodb_buffer_pool_reads) / Innodb_buffer_pool_read_requests</span></pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="cachehit-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>cache-ratio-oracle.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Tính toán Buffer Cache Hit Ratio chi tiết từ V$SYSSTAT</span>
<span class="kw">SELECT</span> <span class="fn">round</span>((<span class="num">1</span> - (phy.value / (cons.value + dbg.value))) * <span class="num">100</span>, <span class="num">2</span>) <span class="kw">AS</span> buffer_cache_hit_pct
<span class="kw">FROM</span> v$sysstat phy, v$sysstat cons, v$sysstat dbg
<span class="kw">WHERE</span> phy.name = <span class="str">'physical reads'</span>
  <span class="kw">AND</span> cons.name = <span class="str">'consistent gets'</span>
  <span class="kw">AND</span> dbg.name = <span class="str">'db block gets'</span>;</pre>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">T</span>Temp Spill & Bão hòa bộ nhớ sắp xếp<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Khi các thao tác <code>ORDER BY</code>, <code>GROUP BY</code>, hoặc <code>HASH JOIN</code> có kích thước lớn hơn vùng nhớ đệm sắp xếp, database buộc phải ghi dữ liệu tạm ra ổ đĩa (Temp Spill). SSD nhanh đến đâu vẫn chậm gấp 10-100 lần so với RAM.</p>
          <div class="info-box note">📌 <span><strong>Điều chỉnh tham số quan trọng từ PDF (Trang 28, 41):</strong>
          <br>• <strong>PostgreSQL:</strong> Tăng <code>work_mem</code> (Từ mặc định 4MB lên 32-64MB) và cấu hình <code>random_page_cost = 1.1</code> tối ưu cho SSD.
          <br>• <strong>MySQL:</strong> Tăng <code>sort_buffer_size</code> (Từ mặc định 256KB lên 4-8MB) để tránh disk-based sort.
          <br>• <strong>Oracle:</strong> Cấu hình <code>PGA_AGGREGATE_TARGET</code> tự động phân bổ vùng nhớ làm việc cho session.
          </span></div>
          
          <div class="tab-group" id="tabs-tempspill">
            <div class="tab active" onclick="switchTab('tabs-tempspill','tempspill-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-tempspill','tempspill-my')">MySQL</div>
            <div class="tab" onclick="switchTab('tabs-tempspill','tempspill-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="tempspill-pg">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>temp-spill-pg.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Theo dõi khối lượng dữ liệu tạm ghi ra disk</span>
<span class="kw">SELECT</span> datname, temp_files, temp_bytes
<span class="kw">FROM</span> pg_stat_database;

<span class="comment">-- Điều chỉnh tham số tối ưu (PDF trang 28, 41)</span>
<span class="kw">SET</span> work_mem = <span class="str">'64MB'</span>;
<span class="kw">SET</span> random_page_cost = <span class="num">1.1</span>;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="tempspill-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>temp-spill-mysql.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Theo dõi số lượng bảng tạm được ghi xuống ổ đĩa</span>
<span class="kw">SHOW GLOBAL STATUS LIKE</span> <span class="str">'Created_tmp_disk_tables'</span>;

<span class="comment">-- Nâng sort_buffer_size cho session sắp xếp (PDF trang 28)</span>
<span class="kw">SET SESSION</span> sort_buffer_size = <span class="num">8</span> * <span class="num">1024</span> * <span class="num">1024</span>; <span class="comment"># 8MB</span></pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="tempspill-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>temp-spill-oracle.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Truy vấn các session đang chiếm dụng Temp Tablespace</span>
<span class="kw">SELECT</span> s.sid, s.username, u.tablespace, u.contents,
       <span class="fn">round</span>(u.blocks * <span class="num">8</span> / <span class="num">1024</span>, <span class="num">2</span>) <span class="kw">AS</span> temp_mb,
       q.sql_text
<span class="kw">FROM</span> v$session s
<span class="kw">JOIN</span> v$sort_usage u <span class="kw">ON</span> s.saddr = u.session_addr
<span class="kw">LEFT JOIN</span> v$sql q <span class="kw">ON</span> q.sql_id = s.sql_id;

<span class="comment">-- Cấu hình tự động quản lý vùng nhớ PGA để tối ưu</span>
<span class="kw">ALTER SYSTEM SET</span> pga_aggregate_target = <span class="num">2</span>G <span class="kw">SCOPE</span>=BOTH;
<span class="kw">ALTER SYSTEM SET</span> workarea_size_policy = AUTO <span class="kw">SCOPE</span>=BOTH;</pre>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-buttons"><button class="nav-btn" onclick="prevModule()">← Trước</button><button class="nav-btn primary" onclick="nextModule()">Tiếp →</button></div>
    </div>

    <!-- S5: Backup & Restore Drill -->
    <div class="module" id="s5">
      <div class="module-header">
        <div class="module-tag">S5 · Backup & Recovery</div>
        <div class="module-title">Chiến lược Backup & Quy trình Restore Drill</div>
        <div class="module-subtitle">Dữ liệu sao lưu hoàn toàn vô giá trị cho đến khi bạn chứng minh được khả năng phục hồi dữ liệu thành công trong thời gian RTO cam kết.</div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">B</span>Hiểu đúng về RPO và RTO<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Mọi chính sách sao lưu đều bắt đầu bằng thỏa thuận mức độ dịch vụ (SLA) nghiệp vụ:</p>
          <ul>
            <li><strong>RPO (Recovery Point Objective):</strong> Mốc thời gian tối đa chấp nhận mất mát dữ liệu. RPO = 5 phút nghĩa là nếu hệ thống sập lúc 12:00, khi khôi phục lại dữ liệu phải mới tối thiểu đến 11:55 (sử dụng PITR/Archivelog).</li>
            <li><strong>RTO (Recovery Time Objective):</strong> Thời gian tối đa cho phép để phục hồi hệ thống online trở lại. RTO = 15 phút nghĩa là từ khi database sập đến khi hoạt động bình thường app kết nối được chỉ được gói gọn trong 15 phút.</li>
          </ul>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">S</span>Các lệnh sao lưu Database chuẩn<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <div class="tab-group" id="tabs-backup">
            <div class="tab active" onclick="switchTab('tabs-backup','backup-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-backup','backup-my')">MySQL</div>
            <div class="tab" onclick="switchTab('tabs-backup','backup-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="backup-pg">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>pg-backup.sh</span></div>
              <div class="cmd-body">
<pre><span class="comment"># 1. Backup vật lý toàn bộ database (Base Backup) thích hợp cho PITR</span>
pg_basebackup -h primary_ip -D /var/lib/postgresql/backup/base_backup -Fp -Xs -P

<span class="comment"># 2. Backup logic một database đơn lẻ</span>
pg_dump -h localhost -U appuser -d appdb -Fd -j <span class="num">4</span> -f /var/lib/postgresql/backup/logical_backup</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="backup-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>mysql-backup.sh</span></div>
              <div class="cmd-body">
                <pre><span class="comment"># Sao lưu logic an toàn tránh khóa bảng InnoDB (single-transaction)</span>
mysqldump --host=localhost --user=root --password \
          --single-transaction \
          --routines --triggers \
          --databases appdb &gt; /backup/mysql_appdb.sql</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="backup-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>rman-backup.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Sử dụng Recovery Manager (RMAN) sao lưu vật lý toàn bộ db kèm Archive Redo Log</span>
RMAN&gt; BACKUP DATABASE PLUS ARCHIVELOG;

<span class="comment">-- Quy trình phục hồi khi mất dữ liệu:</span>
RMAN&gt; STARTUP MOUNT;
RMAN&gt; RESTORE DATABASE;
RMAN&gt; RECOVER DATABASE;
RMAN&gt; ALTER DATABASE OPEN;</pre>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-practice">P</span>Quy trình diễn tập khôi phục (Restore Drill) định kỳ<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Mỗi tháng/quý, một DBA bắt buộc phải thực thi kế hoạch <strong>Restore Drill</strong> trên môi trường cô lập:</p>
          <ol>
            <li>Tải bản backup mới nhất từ hệ thống lưu trữ ngoài (S3/Cloud storage).</li>
            <li>Restore bản backup lên một server test hoàn toàn độc lập với production.</li>
            <li>Khôi phục PITR tới thời điểm sát nhất để kiểm thử tính nguyên vẹn của log.</li>
            <li>Thực hiện các truy vấn đếm dòng, checksum và so khớp số dư nghiệp vụ.</li>
            <li>Đo đạc thời gian khôi phục thực tế xem có đạt chuẩn SLA RTO quy định hay không.</li>
            <li>Viết báo cáo Restore Drill để làm căn cứ kỹ thuật an toàn.</li>
          </ol>
          <div class="info-box danger">🚨 <span><strong>Production Rule:</strong> Backup mà không có lịch trình diễn tập khôi phục (Restore Drill) thì chỉ là giả định, không phải bằng chứng an toàn dữ liệu.</span></div>
        </div>
      </div>
      <div class="nav-buttons"><button class="nav-btn" onclick="prevModule()">← Trước</button><button class="nav-btn primary" onclick="nextModule()">Tiếp →</button></div>
    </div>

    <!-- S6: Replication & Capacity -->
    <div class="module" id="s6">
      <div class="module-header">
        <div class="module-tag">S6 · Infrastructure</div>
        <div class="module-title">Replication Lag & Capacity Planning</div>
        <div class="module-subtitle">Hạ tầng phân tán giải tải đọc nhưng mang lại thách thức lớn về tính đồng nhất của dữ liệu (Consistency).</div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">R</span>Đo lường độ trễ đồng bộ (Replication Lag)<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Lag replication cao làm ảnh hưởng trực tiếp đến nghiệp vụ đọc của người dùng trên Read Replica. DBA cần liên tục theo dõi các chỉ số trễ:</p>
          
          <div class="tab-group" id="tabs-repl">
            <div class="tab active" onclick="switchTab('tabs-repl','repl-pg')">PostgreSQL</div>
            <div class="tab" onclick="switchTab('tabs-repl','repl-my')">MySQL</div>
            <div class="tab" onclick="switchTab('tabs-repl','repl-ora')">Oracle</div>
          </div>

          <div class="tab-content active" id="repl-pg">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>repl-lag-pg.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Đo lượng byte chênh lệch giữa Primary và Replica</span>
<span class="kw">SELECT</span> 
  application_name,
  client_addr,
  state,
  pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) <span class="kw">AS</span> lag_bytes
<span class="kw">FROM</span> pg_stat_replication;</pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="repl-my">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>repl-lag-mysql.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Xem chi tiết trạng thái luồng replication</span>
<span class="kw">SHOW REPLICA STATUS</span>\G
<span class="comment">-- Chú ý quan trọng vào biến: Seconds_Behind_Source</span>
<span class="comment">-- Nó thể hiện thời gian lag tính bằng giây của Slave so với Master</span></pre>
              </div>
            </div>
          </div>

          <div class="tab-content" id="repl-ora">
            <div class="cmd-block">
              <div class="cmd-header"><span>● ● ●</span><span>repl-lag-oracle.sql</span></div>
              <div class="cmd-body">
<pre><span class="comment">-- Truy vấn trên Standby Database (Oracle Data Guard)</span>
<span class="kw">SELECT</span> name, value, unit, time_computed
<span class="kw">FROM</span> v$dataguard_stats
<span class="kw">WHERE</span> name <span class="kw">IN</span> (<span class="str">'transport lag'</span>, <span class="str">'apply lag'</span>);

<span class="comment">-- Kiểm tra trạng thái hoạt động của các tiến trình Data Guard:</span>
<span class="kw">SELECT</span> process, status, thread#, sequence#, block#
<span class="kw">FROM</span> v$managed_standby;</pre>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">C</span>Xử lý bài toán Read-After-Write Consistency<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p>Khi người dùng tạo một order mới ở Master, app chuyển ngay họ sang trang xem chi tiết order (đọc từ Replica). Nếu replication bị lag 1 giây, người dùng sẽ hoang mang vì không thấy order đâu.</p>
          <h3 class="blue">3 Giải pháp kiến trúc kinh điển</h3>
          <ol>
            <li><strong>Session Routing:</strong> Sau khi thực hiện ghi dữ liệu, ghi nhận vào Session của user và tiếp tục route tất cả truy vấn đọc của user đó về thẳng Master trong vòng 3-5 giây.</li>
            <li><strong>Critical Path Routing:</strong> Route các flow nghiệp vụ nhạy cảm (như thanh toán, sửa thông tin thẻ) 100% về Master. Replica chỉ phục vụ báo cáo, phân tích và xem danh mục.</li>
            <li><strong>Lag-aware Query:</strong> Đo đếm độ lag trước khi đọc. Nếu lag vượt ngưỡng nghiệp vụ (ví dụ > 500ms), tự động hạ cấp nghiệp vụ hoặc chờ dữ liệu từ master.</li>
          </ol>
        </div>
      </div>
      <div class="nav-buttons"><button class="nav-btn" onclick="prevModule()">← Trước</button><button class="nav-btn primary" onclick="nextModule()">Tiếp →</button></div>
    </div>

    <!-- S7: Interview Prep -->
    <div class="module" id="s7">
      <div class="module-header">
        <div class="module-tag">S7 · Interview Prep</div>
        <div class="module-title">Interview Prep — Vận hành & Giám sát Database</div>
        <div class="module-subtitle">Nơi kiểm thử tư duy vận hành thực tế dưới áp lực của Senior DBA / Senior Software Engineer.</div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-quiz">Q</span>Quick Quiz — Trắc nghiệm nhanh<span class="section-toggle">▼</span></div>
        <div class="section-content">
          
          <div class="quiz-item">
            <div class="quiz-q">Theo tài liệu Indexing Ebook, tại sao việc xóa ngay một index thừa có thể gây nguy hiểm và cách xử lý an toàn nhất là gì?</div>
            <div class="quiz-options">
              <div class="quiz-opt" onclick="answerQuiz(this,false,'Xóa ngay lập tức luôn tiềm ẩn rủi ro plan regression bất ngờ.')">A. DROP ngay lập tức vào giờ cao tải</div>
              <div class="quiz-opt" onclick="answerQuiz(this,true,'Đúng! Chuyển index thành INVISIBLE (MySQL/Oracle) giúp kiểm chứng an toàn trước khi xóa hoàn toàn.')">B. Chuyển index sang trạng thái INVISIBLE trong 1-2 tuần trước khi DROP hẳn</div>
              <div class="quiz-opt" onclick="answerQuiz(this,false,'REINDEX chỉ làm mới dữ liệu index, không giúp kiểm chứng rủi ro.')">C. Chạy lệnh REINDEX trước khi DROP</div>
            </div>
            <div class="quiz-explain"></div>
          </div>

          <div class="quiz-item">
            <div class="quiz-q">Khi phát hiện temp bytes của Postgres hoặc Created_tmp_disk_tables của MySQL tăng đột biến, hướng xử lý nào từ PDF là tối ưu nhất?</div>
            <div class="quiz-options">
              <div class="quiz-opt" onclick="answerQuiz(this,false,'Thêm RAM vật lý cần thời gian downtime lâu và tốn kém.')">A. Khởi động lại server và bổ sung RAM vật lý</div>
              <div class="quiz-opt" onclick="answerQuiz(this,true,'Chính xác! Tăng work_mem (Postgres) hoặc sort_buffer_size (MySQL) giúp các truy vấn sắp xếp diễn ra hoàn toàn trên RAM.')">B. Tăng work_mem (Postgres) hoặc sort_buffer_size (MySQL) lên mức 32MB-64MB</div>
              <div class="quiz-opt" onclick="answerQuiz(this,false,'GATHER_STATS không giải quyết vấn đề thiếu bộ nhớ tạm sắp xếp.')">C. Chạy GATHER_TABLE_STATS lập tức</div>
            </div>
            <div class="quiz-explain"></div>
          </div>

        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-practice">T</span>Senior Triage Scenario — Xử lý tình huống sản xuất<span class="section-toggle">▼</span></div>
        <div class="section-content">
          
          <div class="practice-task">
            <div class="practice-task-header">Tình huống: Đĩa cứng của hệ thống PostgreSQL Production bất ngờ bị đầy 95% và liên tục báo động đỏ. Bạn sẽ làm gì?</div>
            <div class="practice-task-body">
              <p><strong>Gợi ý hướng xử lý của Senior DBA:</strong></p>
              <ul>
                <li>Kiểm tra xem hệ thống có đang có Long-running Transaction nào bị treo không. Vì long transaction sẽ chặn Autovacuum giải phóng không gian tuple cũ, gây phình đĩa (Bloat) thảm họa.</li>
                <li>Dò tìm và liệt kê các index không sử dụng (Unused Index) theo câu lệnh ở Section S3 để tiến hành ẩn/xóa an toàn.</li>
                <li>Kiểm tra dung lượng của thư mục WAL / Archivelog xem có bị ứ đọng do tiến trình truyền gửi sang Replica bị nghẽn không.</li>
              </ul>
              <div onclick="toggleSolution(this)" class="solution-toggle">💡 Xem mẫu trả lời Senior</div>
              <div class="solution-box">
                <p><strong>Mẫu trả lời chuẩn phỏng vấn:</strong> "Đầu tiên, tôi sẽ kiểm tra các phiên kết nối đang mở thông qua <code>pg_stat_activity</code> để tìm và tắt (terminate) các transaction chạy quá lâu bằng <code>pg_terminate_backend()</code> nhằm cho phép Autovacuum hoạt động giải phóng không gian trống. Tiếp theo, tôi sẽ truy vấn <code>pg_stat_all_indexes</code> để tìm các index thừa lớn hơn 5GB mà chưa từng được quét (idx_scan = 0) và lên kế hoạch xóa concurrently. Cuối cùng, tôi sẽ kiểm tra xem replication slot có bị treo làm tồn đọng các tệp WAL trên Primary không."</p>
              </div>
            </div>
          </div>

        </div>
      </div>
      <div class="nav-buttons"><button class="nav-btn" onclick="prevModule()">← Trước</button><button class="nav-btn primary" onclick="nextModule()">Tiếp →</button></div>
    </div>

    <!-- S8: Checklist & Summary -->
    <div class="module" id="s8">
      <div class="module-header">
        <div class="module-tag">S8 · Summary</div>
        <div class="module-title">Checklist & Tổng kết Module 06</div>
        <div class="module-subtitle">Hoàn thành checklist thực tế này chứng minh bạn đã sẵn sàng gánh vác trách nhiệm vận hành database mức độ Senior Developer / Junior DBA.</div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-summary">S</span>Summary — 6 Điểm cốt lõi cần nhớ<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <div class="summary-grid">
            <div class="summary-item"><strong>Giám sát Golden Signals</strong>Tập trung vào Latency p99, Traffic, Errors, Saturation và Growth.</div>
            <div class="summary-item"><strong>Top SQL theo Total Impact</strong>Luôn đánh giá tổng chi phí hệ thống thay vì chỉ nhìn vào thời gian chạy đơn lẻ.</div>
            <div class="summary-item"><strong>Sức khỏe Bảng & Index</strong>Luôn ẩn index (Invisible Index) trước khi xóa thật để loại trừ regression.</div>
            <div class="summary-item"><strong>Tuning Cache & Memory</strong>Cân đối RAM sắp xếp qua work_mem, sort_buffer_size tránh temp spill ra đĩa.</div>
            <div class="summary-item"><strong>Khôi phục thực tế (Restore Drill)</strong>Sao lưu chỉ là lý thuyết cho tới khi phục hồi thành công trong khung RTO.</div>
            <div class="summary-item"><strong>Consistency của Replica</strong>Quản lý trễ Replication Lag và định tuyến Session Routing thông minh.</div>
          </div>
        </div>
      </div>

      <div class="section">
        <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-practice">D</span>Definition of Done — Đo lường năng lực học tập<span class="section-toggle">▼</span></div>
        <div class="section-content">
          <p class="progress-text" id="checklist-progress-text">0/8 mục hoàn thành (0%)</p>
          <div class="progress-bar"><div class="progress-fill" id="checklist-progress-fill"></div></div>
          
          <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Hiểu sâu 5 Golden Signals và cách cấu hình Alert không gây nhiễu.</span></div>
          <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Thành thạo câu lệnh tìm kiếm Top SQL trên cả PostgreSQL, MySQL và Oracle.</span></div>
          <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Truy vết và dọn dẹp an toàn các index dư thừa bằng Invisible Index.</span></div>
          <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Cập nhật fresh statistics bằng cách chạy <code>ANALYZE</code> ngay sau bulk load.</span></div>
          <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Định cấu hình <code>random_page_cost</code> và vùng nhớ sắp xếp tránh temp spill.</span></div>
          <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Tự lập quy trình Restore Drill chứng minh tính sẵn sàng của dữ liệu sao lưu.</span></div>
          <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Đo lường Replication Lag LSN bytes trên Postgres, seconds trên MySQL và apply lag trên Oracle.</span></div>
          <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Trả lời lưu loát các câu hỏi tình huống sự cố sản xuất của Senior.</span></div>
        </div>
      </div>
      <div class="nav-buttons"><button class="nav-btn" onclick="prevModule()">← Trước</button><button class="nav-btn" disabled>Hoàn thành</button></div>
    </div>

  </main>
</div>

<script>
const navItems = document.querySelectorAll('.nav-item');
let currentModule = 0;
const totalModules = 9;

function showModule(index, navEl) {
  document.querySelectorAll('.module').forEach(m => m.classList.remove('active'));
  const target = document.getElementById('s' + index);
  if (target) { target.classList.add('active'); currentModule = index; window.scrollTo({top: 0, behavior: 'smooth'}); }
  navItems.forEach(n => n.classList.remove('active'));
  if (navEl) { navEl.classList.add('active'); }
  else { if (navItems[index]) navItems[index].classList.add('active'); }
}

function nextModule() { if (currentModule < totalModules - 1) showModule(currentModule + 1); }
function prevModule() { if (currentModule > 0) showModule(currentModule - 1); }

function toggleSection(header) {
  const content = header.nextElementSibling;
  const toggle = header.querySelector('.section-toggle');
  const isHidden = content.style.display === 'none';
  content.style.display = isHidden ? 'block' : 'none';
  toggle.textContent = isHidden ? '▼' : '▶';
}

function answerQuiz(el, isCorrect, msg) {
  const item = el.closest('.quiz-item');
  const opts = item.querySelectorAll('.quiz-opt');
  const explain = item.querySelector('.quiz-explain');
  opts.forEach(opt => (opt.style.pointerEvents = 'none'));
  el.classList.add(isCorrect ? 'correct' : 'wrong');
  if (!isCorrect) { opts.forEach(opt => { const o = opt.getAttribute('onclick'); if (o && o.includes('true')) opt.classList.add('correct'); }); }
  explain.textContent = (isCorrect ? '✓ Chính xác! ' : '✗ Sai rồi. ') + msg;
  explain.classList.add('show');
}

function toggleSolution(btn) {
  const box = btn.nextElementSibling;
  const show = box.classList.toggle('show');
  btn.textContent = show ? '🙈 Ẩn lời giải' : '💡 Xem mẫu trả lời Senior';
}

function switchTab(groupId, tabId) {
  const group = document.getElementById(groupId);
  if (!group) return;
  group.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
  const contents = group.parentElement.querySelectorAll('.tab-content');
  contents.forEach(c => c.classList.remove('active'));
  const target = document.getElementById(tabId);
  if (target) target.classList.add('active');
  group.querySelectorAll('.tab').forEach(tab => {
    const oc = tab.getAttribute('onclick') || '';
    if (oc.includes(tabId)) tab.classList.add('active');
  });
}

function toggleCheck(box) {
  box.classList.toggle('checked');
  updateProgress();
}

function updateProgress() {
  const checks = document.querySelectorAll('.check-box');
  const checked = document.querySelectorAll('.check-box.checked').length;
  const total = checks.length;
  const pct = total === 0 ? 0 : Math.round((checked / total) * 100);
  const fill = document.getElementById('checklist-progress-fill');
  const text = document.getElementById('checklist-progress-text');
  if (fill) fill.style.width = `${pct}%`;
  if (text) text.textContent = `${checked}/${total} mục hoàn thành (${pct}%)`;
}

showModule(0, navItems[0]);
updateProgress();
</script>
</body>
</html>'''

with open('D:/DE/Tuning_SQL/Module06_Operations_Monitoring_new.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done successfully!')
