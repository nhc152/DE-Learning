html = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Module 05 &mdash; Transactions, Locks &amp; Concurrency</title>
<meta name="description" content="Hướng dẫn Transaction ACID, Isolation Levels, MVCC, Deadlock, Optimistic Locking, Savepoint, Lock Timeout và Oracle Autonomous Transaction.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{--bg:#0d1117;--surface:#161b22;--surface2:#21262d;--border:#30363d;--accent:#58a6ff;--accent2:#3fb950;--accent3:#f78166;--accent4:#d2a8ff;--accent5:#ffa657;--text:#e6edf3;--text-muted:#8b949e;--code-bg:#0d1117}
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Inter','Segoe UI',-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.7}
  .hero{background:linear-gradient(135deg,#0d1117 0%,#161b22 40%,#1c1a2a 100%);border-bottom:2px solid var(--accent4);padding:40px 24px 30px;text-align:center;position:relative;overflow:hidden}
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
  pre{font-family:'JetBrains Mono','Courier New',monospace;font-size:.82rem;line-height:1.6;white-space:pre;overflow-x:auto;color:var(--text)}
  .kw{color:#ff7b72}.kw2{color:var(--accent)}.str{color:var(--accent5)}.fn{color:var(--accent4)}.num{color:#79c0ff}.comment{color:var(--text-muted)}
  .db-tag{display:inline-block;padding:2px 8px;border-radius:4px;font-size:.68rem;font-weight:700;letter-spacing:.5px;margin-bottom:6px;margin-right:4px}
  .db-pg{background:#4169e122;color:#4d9de0;border:1px solid #4169e155}
  .db-my{background:#f0931322;color:#f09313;border:1px solid #f0931355}
  .db-oracle{background:#cc000022;color:#f97316;border:1px solid #cc000055}
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
  table{width:100%;border-collapse:collapse;margin:12px 0;font-size:.83rem}
  th{background:var(--surface2);padding:8px 12px;text-align:left;border:1px solid var(--border);color:var(--accent4)}
  td{padding:8px 12px;border:1px solid var(--border)}
  tr:nth-child(even) td{background:#ffffff05}
  .mental-model{border-left:4px solid var(--accent);background:#1f6feb1a;padding:12px 14px;border-radius:6px;margin:12px 0;font-size:.88rem}
  .checklist-row{display:flex;align-items:flex-start;gap:10px;margin-bottom:8px}
  .check-box{width:16px;height:16px;border:1px solid var(--border);border-radius:3px;flex-shrink:0;margin-top:.25rem;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center}
  .check-box.checked{background:var(--accent2);border-color:var(--accent2)}
  .check-box.checked::after{content:"\\2713";font-size:10px;color:#000;font-weight:600}
  .progress-text{font-size:.8rem;color:var(--text-muted);margin-bottom:8px}
  @media(max-width:768px){.sidebar{display:none}.main{padding:16px}.summary-grid{grid-template-columns:1fr}}
</style>
</head>
<body>

<div class="hero">
  <h1>Module 05 &mdash; Transactions, Locks &amp; Concurrency</h1>
  <p>Hiểu transaction, isolation, MVCC, lock wait, deadlock, optimistic locking và các kỹ thuật Oracle nâng cao<br>để hệ thống ghi dữ liệu đúng mà vẫn chạy được dưới tải đồng thời cao.</p>
  <div class="badge-row">
    <span class="badge badge-purple">DBA Core</span>
    <span class="badge badge-green">~5&ndash;7 ng&agrave;y</span>
    <span class="badge badge-blue">Concurrency Control</span>
    <span class="badge badge-orange">PostgreSQL &middot; MySQL &middot; Oracle</span>
  </div>
</div>

<div class="container">
  <nav class="sidebar">
    <div class="sidebar-title">Module Navigation</div>
    <div class="level-label">MODULE 05 &middot; LOCKS &amp; CONCURRENCY</div>
    <div class="nav-item active" onclick="showModule(0,this)"><span class="nav-number">S0</span>T&#7893;ng quan &amp; M&#7909;c ti&#234;u</div>
    <div class="nav-item" onclick="showModule(1,this)"><span class="nav-number">S1</span>Transaction &amp; ACID</div>
    <div class="nav-item" onclick="showModule(2,this)"><span class="nav-number">S2</span>Isolation &amp; MVCC</div>
    <div class="nav-item" onclick="showModule(3,this)"><span class="nav-number">S3</span>Row/Table/GAP Locks</div>
    <div class="nav-item" onclick="showModule(4,this)"><span class="nav-number">S4</span>FOR UPDATE &amp; Queues</div>
    <div class="nav-item" onclick="showModule(5,this)"><span class="nav-number">S5</span>Deadlock &amp; Hot Rows</div>
    <div class="nav-item" onclick="showModule(6,this)"><span class="nav-number">S6</span>Optimistic Locking</div>
    <div class="nav-item" onclick="showModule(7,this)"><span class="nav-number">S7</span>Savepoint &amp; Lock Timeout</div>
    <div class="nav-item" onclick="showModule(8,this)"><span class="nav-number">S8</span>Oracle N&#226;ng cao</div>
    <div class="nav-item" onclick="showModule(9,this)"><span class="nav-number">S9</span>Diagnose Lock Waits</div>
    <div class="nav-item" onclick="showModule(10,this)"><span class="nav-number">S10</span>Interview Prep</div>
    <div class="nav-item" onclick="showModule(11,this)"><span class="nav-number">S11</span>Checklist &amp; T&#7893;ng k&#7871;t</div>
  </nav>

  <main class="main">

<!-- S0 -->
<div class="module active" id="s0">
  <div class="module-header">
    <div class="module-tag">S0 &middot; Orientation</div>
    <div class="module-title">T&#7893;ng quan &amp; M&#7909;c ti&#234;u Module 05</div>
    <div class="module-subtitle">Index v&agrave; plan gi&uacute;p query nhanh. Transaction v&agrave; lock gi&uacute;p d&#7919; li&#7879;u &#273;&uacute;ng khi nhi&#7873;u session c&ugrave;ng &#273;&#7885;c/ghi.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-summary">M</span>Roadmap 12 sections<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Section</th><th>T&#234;n</th><th>Tr&#7885;ng t&#226;m</th></tr></thead>
        <tbody>
          <tr><td>S0</td><td>T&#7893;ng quan</td><td>Concurrency gi&#7843;i quy&#7871;t v&#7845;n &#273;&#7873; g&igrave;</td></tr>
          <tr><td>S1</td><td>Transaction &amp; ACID</td><td>Atomicity, consistency, durability</td></tr>
          <tr><td>S2</td><td>Isolation &amp; MVCC</td><td>Read phenomena, snapshot, versioning</td></tr>
          <tr><td>S3</td><td>Row/Table/GAP Locks</td><td>C&aacute;c lo&#7841;i lock ph&#7893; bi&#7871;n</td></tr>
          <tr><td>S4</td><td>FOR UPDATE &amp; Queues</td><td>Kh&oacute;a d&ograve;ng ch&#7911; &#273;&#7897;ng, SKIP LOCKED</td></tr>
          <tr><td>S5</td><td>Deadlock &amp; Hot Rows</td><td>Tr&aacute;nh deadlock, x&#7917; l&yacute; row n&oacute;ng</td></tr>
          <tr><td>S6</td><td>Optimistic Locking</td><td>Version column, CAS pattern</td></tr>
          <tr><td>S7</td><td>Savepoint &amp; Lock Timeout</td><td>Partial rollback, b&#7843;o v&#7879; kh&#7887;i treo v&ocirc; h&#7841;n</td></tr>
          <tr><td>S8</td><td>Oracle N&#226;ng cao</td><td>Autonomous Transaction, ORA-01555</td></tr>
          <tr><td>S9</td><td>Diagnose Lock Waits</td><td>View l&#7879;nh ch&#7849;n &#273;o&aacute;n PostgreSQL/MySQL/Oracle</td></tr>
          <tr><td>S10</td><td>Interview Prep</td><td>C&#226;u h&#7887;i DBA/backend senior</td></tr>
          <tr><td>S11</td><td>Checklist &amp; T&#7893;ng k&#7871;t</td><td>Definition of Done</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-purpose">T</span>Concurrency gi&#7843;i quy&#7871;t v&#7845;n &#273;&#7873; g&igrave;?<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <h3 class="blue">V&#7845;n &#273;&#7873; kh&ocirc;ng n&#7857;m &#7903; m&#7897;t query, m&agrave; &#7903; nhi&#7873;u query c&ugrave;ng l&uacute;c</h3>
      <p>M&#7897;t transaction ch&#7841;y &#273;&uacute;ng khi &#273;&#7913;ng m&#7897;t m&igrave;nh ch&#432;a ch&#7855;c &#273;&uacute;ng khi 100 worker c&ugrave;ng ch&#7841;y. Lock, isolation v&agrave; MVCC l&agrave; c&#417; ch&#7871; database d&ugrave;ng &#273;&#7875; gi&#7919; d&#7919; li&#7879;u nh&#7845;t qu&aacute;n trong khi v&#7851;n cho ph&eacute;p concurrency.</p>
      <div class="mental-model"><strong>Mental model:</strong> Transaction l&agrave; ranh gi&#7899;i thay &#273;&#7893;i d&#7919; li&#7879;u. Lock l&agrave; t&iacute;n hi&#7879;u "t&ocirc;i &#273;ang s&#7917;a ph&#7847;n n&agrave;y". Isolation quy&#7871;t &#273;&#7883;nh session kh&aacute;c &#273;&#432;&#7907;c nh&igrave;n th&#7845;y g&igrave; trong l&uacute;c &#273;&oacute;.</div>
      <h3 class="orange">D&#7845;u hi&#7879;u production c&#7847;n module n&agrave;y</h3>
      <ul>
        <li>Request treo v&igrave; lock wait nh&#432;ng CPU database th&#7845;p.</li>
        <li>Deadlock xu&#7845;t hi&#7879;n ng&#7851;u nhi&#234;n khi traffic t&#259;ng.</li>
        <li>Worker x&#7917; l&yacute; tr&ugrave;ng job ho&#7863;c b&#7887; s&oacute;t job.</li>
        <li>Counter, inventory, balance b&#7883; sai khi nhi&#7873;u request c&#7853;p nh&#7853;t c&ugrave;ng l&uacute;c.</li>
      </ul>
    </div>
  </div>
</div>

<!-- S1 -->
<div class="module" id="s1">
  <div class="module-header">
    <div class="module-tag">S1 &middot; Transaction Basics</div>
    <div class="module-title">Transaction &amp; ACID</div>
    <div class="module-subtitle">Transaction gom nhi&#7873;u thao t&aacute;c th&agrave;nh m&#7897;t &#273;&#417;n v&#7883; logic: ho&#7863;c th&agrave;nh c&ocirc;ng to&agrave;n b&#7897;, ho&#7863;c rollback to&agrave;n b&#7897;.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">A</span>ACID theo c&aacute;ch th&#7921;c d&#7909;ng<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Thu&#7897;c t&iacute;nh</th><th>&#221; ngh&#297;a</th><th>V&iacute; d&#7909;</th></tr></thead>
        <tbody>
          <tr><td>Atomicity</td><td>All-or-nothing</td><td>Tr&#7915; kho v&agrave; t&#7841;o order ph&#7843;i c&ugrave;ng commit</td></tr>
          <tr><td>Consistency</td><td>Kh&ocirc;ng ph&aacute; constraint/invariant</td><td>S&#7889; d&#432; kh&ocirc;ng &acirc;m, FK h&#7907;p l&#7879;</td></tr>
          <tr><td>Isolation</td><td>Transaction kh&ocirc;ng nh&igrave;n th&#7845;y tr&#7841;ng th&aacute;i d&#7903; dang sai m&#7913;c</td><td>Kh&ocirc;ng &#273;&#7885;c order &#273;ang rollback</td></tr>
          <tr><td>Durability</td><td>Commit r&#7891;i th&igrave; kh&ocirc;ng m&#7845;t khi crash</td><td>WAL/binlog/redo log b&#7843;o v&#7879; d&#7919; li&#7879;u</td></tr>
        </tbody>
      </table>
      <div class="tab-group" id="tabs-tx">
        <div class="tab active" onclick="switchTab('tabs-tx','tx-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-tx','tx-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-tx','tx-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="tx-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>transaction.sql</span></div><div class="cmd-body">
<pre><span class="kw">BEGIN</span>;

<span class="kw">UPDATE</span> inventory
<span class="kw">SET</span> quantity = quantity - <span class="num">1</span>
<span class="kw">WHERE</span> product_id = <span class="num">100</span> <span class="kw">AND</span> quantity &gt; <span class="num">0</span>;

<span class="kw">INSERT INTO</span> orders(user_id, product_id, status)
<span class="kw">VALUES</span> (<span class="num">42</span>, <span class="num">100</span>, <span class="str">'created'</span>);

<span class="kw">COMMIT</span>;  <span class="comment">-- hoặc ROLLBACK nếu có lỗi</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="tx-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>transaction.sql</span></div><div class="cmd-body">
<pre><span class="kw">START TRANSACTION</span>;

<span class="kw">UPDATE</span> inventory
<span class="kw">SET</span> quantity = quantity - <span class="num">1</span>
<span class="kw">WHERE</span> product_id = <span class="num">100</span> <span class="kw">AND</span> quantity &gt; <span class="num">0</span>;

<span class="kw">INSERT INTO</span> orders(user_id, product_id, status)
<span class="kw">VALUES</span> (<span class="num">42</span>, <span class="num">100</span>, <span class="str">'created'</span>);

<span class="kw">COMMIT</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="tx-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>transaction.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Oracle: transaction bắt đầu ngầm định sau mỗi DDL/DML</span>
<span class="kw">UPDATE</span> inventory
<span class="kw">SET</span> quantity = quantity - <span class="num">1</span>
<span class="kw">WHERE</span> product_id = <span class="num">100</span> <span class="kw">AND</span> quantity &gt; <span class="num">0</span>;

<span class="kw">INSERT INTO</span> orders(user_id, product_id, status)
<span class="kw">VALUES</span> (<span class="num">42</span>, <span class="num">100</span>, <span class="str">'CREATED'</span>);

<span class="kw">COMMIT</span>;</pre>
        </div></div>
      </div>
      <div class="info-box warn">&#9888;&#65039; <span><strong>Rule:</strong> Transaction c&agrave;ng d&agrave;i, lock c&agrave;ng gi&#7919; l&acirc;u. Kh&ocirc;ng g&#7885;i API ngo&agrave;i, g&#7917;i email, ho&#7863;c ch&#7901; user input trong transaction.</span></div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">F</span>Transaction flow<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>transaction-flow.txt</span></div><div class="cmd-body">
<pre><span class="kw2">BEGIN</span>
  &#9474;
  &#9500;&#9472; read rows          <span class="comment">(snapshot visible theo isolation level)</span>
  &#9500;&#9472; acquire locks      <span class="comment">(khi modify / FOR UPDATE)</span>
  &#9500;&#9472; write undo/redo/WAL
  &#9474;
  &#9500;&#9472; COMMIT   &#8594; changes visible, locks released
  &#9492;&#9472; ROLLBACK &#8594; changes undone, locks released</pre>
      </div></div>
    </div>
  </div>
</div>

<!-- S2 -->
<div class="module" id="s2">
  <div class="module-header">
    <div class="module-tag">S2 &middot; Isolation &amp; MVCC</div>
    <div class="module-title">Isolation Levels &amp; MVCC</div>
    <div class="module-subtitle">Isolation quy&#7871;t &#273;&#7883;nh transaction &#273;&#432;&#7907;c nh&igrave;n th&#7845;y d&#7919; li&#7879;u n&agrave;o. MVCC cho ph&eacute;p read kh&ocirc;ng block write trong nhi&#7873;u t&igrave;nh hu&#7889;ng.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">I</span>Isolation levels &amp; Read Phenomena<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Level</th><th>Ch&#7863;n &#273;&#432;&#7907;c</th><th>V&#7851;n c&oacute; th&#7875;</th><th>Chi ph&iacute;/r&#7911;i ro</th></tr></thead>
        <tbody>
          <tr><td>READ COMMITTED</td><td>Dirty read</td><td>Non-repeatable read, Phantom</td><td>M&#7895;i statement c&oacute; snapshot m&#7899;i</td></tr>
          <tr><td>REPEATABLE READ</td><td>Dirty read, Non-repeatable</td><td>Phantom (tu&ugrave;y DB)</td><td>Snapshot &#7893;n &#273;&#7883;nh h&#417;n; MySQL ch&#7863;n phantom qua next-key lock</td></tr>
          <tr><td>SERIALIZABLE</td><td>H&#7847;u h&#7871;t anomaly</td><td>Serialization failure/retry</td><td>C&oacute; th&#7875; b&#7883; rollback nhi&#7873;u h&#417;n</td></tr>
        </tbody>
      </table>
      <div class="tab-group" id="tabs-iso">
        <div class="tab active" onclick="switchTab('tabs-iso','iso-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-iso','iso-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-iso','iso-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="iso-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>set-isolation.sql</span></div><div class="cmd-body">
<pre><span class="kw">BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ</span>;
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="kw">COMMIT</span>;

<span class="comment">-- Xem isolation level hiện tại:</span>
<span class="kw">SHOW</span> transaction_isolation;
<span class="comment">-- Hoặc toàn phiên:</span>
<span class="kw">SET</span> default_transaction_isolation = <span class="str">'repeatable read'</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="iso-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>set-isolation.sql</span></div><div class="cmd-body">
<pre><span class="kw">SET TRANSACTION ISOLATION LEVEL READ COMMITTED</span>;
<span class="kw">START TRANSACTION</span>;
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="kw">COMMIT</span>;

<span class="comment">-- Mặc định MySQL InnoDB: REPEATABLE READ</span>
<span class="kw">SELECT</span> @@transaction_isolation;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="iso-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>set-isolation.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Oracle mặc định: READ COMMITTED với read consistency</span>
<span class="kw">SET TRANSACTION ISOLATION LEVEL SERIALIZABLE</span>;
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="kw">COMMIT</span>;

<span class="comment">-- Lưu ý: Oracle KHÔNG có REPEATABLE READ theo chuẩn SQL</span>
<span class="comment">-- Readers không block writers, nhưng writers vẫn block writers cùng row</span></pre>
        </div></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">M</span>MVCC trong th&#7921;c t&#7871;<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>MVCC l&#432;u nhi&#7873;u version c&#7911;a row &#273;&#7875; transaction &#273;&#7885;c &#273;&#432;&#7907;c snapshot nh&#7845;t qu&aacute;n m&agrave; kh&ocirc;ng c&#7847;n ch&#7863;n writer trong nhi&#7873;u tr&#432;&#7901;ng h&#7907;p. &#272;&#7893;i l&#7841;i, database c&#7847;n cleanup version c&#361;.</p>
      <table>
        <thead><tr><th>DB</th><th>C&#417; ch&#7871;</th><th>Cleanup</th><th>&#272;i&#7875;m DBA c&#7847;n nh&#7899;</th></tr></thead>
        <tbody>
          <tr><td>PostgreSQL</td><td>Tuple version (xmin/xmax)</td><td>VACUUM / autovacuum</td><td>Long transaction gi&#7919; version c&#361;, g&acirc;y table bloat</td></tr>
          <tr><td>MySQL/InnoDB</td><td>Undo log + read view</td><td>Purge thread</td><td>Long transaction l&agrave;m purge ch&#7853;m, undo l&#7899;n</td></tr>
          <tr><td>Oracle</td><td>Undo segments + SCN</td><td>Undo retention</td><td>Undo kh&ocirc;ng &#273;&#7911; c&oacute; th&#7875; g&acirc;y ORA-01555</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- S3 -->
<div class="module" id="s3">
  <div class="module-header">
    <div class="module-tag">S3 &middot; Lock Types</div>
    <div class="module-title">Row Locks, Table Locks &amp; Gap Locks</div>
    <div class="module-subtitle">Kh&ocirc;ng ph&#7843;i lock n&agrave;o c&#361;ng gi&#7889;ng nhau. Hi&#7875;u lock scope gi&uacute;p b&#7841;n gi&#7843;m lock wait v&agrave; deadlock.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">L</span>C&aacute;c lo&#7841;i lock c&#7847;n bi&#7871;t<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Lock</th><th>Khi xu&#7845;t hi&#7879;n</th><th>R&#7911;i ro</th></tr></thead>
        <tbody>
          <tr><td>Row lock</td><td>UPDATE/DELETE/FOR UPDATE tr&#234;n row</td><td>Session kh&aacute;c update c&ugrave;ng row ph&#7843;i ch&#7901;</td></tr>
          <tr><td>Table lock</td><td>DDL, LOCK TABLE, m&#7897;t s&#7889; bulk operation</td><td>&#7266;nh h&#432;&#7903;ng r&#7897;ng</td></tr>
          <tr><td>Gap / next-key lock</td><td>MySQL InnoDB range scan &#7903; m&#7897;t s&#7889; isolation</td><td>Insert v&agrave;o range b&#7883; ch&#7863;n</td></tr>
          <tr><td>Advisory lock</td><td>App-defined logical lock</td><td>C&#7847;n discipline release/timeout</td></tr>
        </tbody>
      </table>
      <div class="tab-group" id="tabs-rowlock">
        <div class="tab active" onclick="switchTab('tabs-rowlock','rowlock-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-rowlock','rowlock-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-rowlock','rowlock-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="rowlock-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>row-lock.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Session 1: UPDATE giữ row lock đến commit</span>
<span class="kw">BEGIN</span>;
<span class="kw">UPDATE</span> accounts <span class="kw">SET</span> balance = balance - <span class="num">100</span> <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="comment">-- Chưa commit: row id=1 đang bị lock</span>

<span class="comment">-- Advisory lock dùng pg_advisory_lock:</span>
<span class="kw">SELECT</span> <span class="fn">pg_advisory_xact_lock</span>(<span class="num">12345</span>);  <span class="comment">-- tự release khi commit</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="rowlock-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>row-lock.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- MySQL InnoDB row lock:</span>
<span class="kw">START TRANSACTION</span>;
<span class="kw">UPDATE</span> accounts <span class="kw">SET</span> balance = balance - <span class="num">100</span> <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="comment">-- lock được giữ đến COMMIT</span>

<span class="comment">-- Gap lock (REPEATABLE READ): chặn INSERT vào range</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> coupons
<span class="kw">WHERE</span> code <span class="kw">BETWEEN</span> <span class="str">'A100'</span> <span class="kw">AND</span> <span class="str">'A200'</span>
<span class="kw">FOR UPDATE</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="rowlock-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>row-lock.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Oracle: row-level lock tự động khi UPDATE/DELETE</span>
<span class="kw">UPDATE</span> accounts <span class="kw">SET</span> balance = balance - <span class="num">100</span> <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="comment">-- Oracle KHÔNG có Gap Lock như MySQL</span>
<span class="comment">-- Oracle dùng ITL (Interested Transaction List) trong data block</span>
<span class="kw">COMMIT</span>;</pre>
        </div></div>
      </div>
      <div class="info-box warn">&#9888;&#65039; <span><strong>Index ảnh hưởng lock scope:</strong> UPDATE/DELETE không có index phù hợp có thể scan nhiều row, giữ nhiều lock hơn và dễ gây lock wait hơn.</span></div>
    </div>
  </div>
</div>

<!-- S4 -->
<div class="module" id="s4">
  <div class="module-header">
    <div class="module-tag">S4 &middot; FOR UPDATE</div>
    <div class="module-title">FOR UPDATE, NOWAIT &amp; SKIP LOCKED</div>
    <div class="module-subtitle">Kh&oacute;a ch&#7911; &#273;&#7897;ng &#273;&uacute;ng l&uacute;c gi&uacute;p x&#7917; l&yacute; inventory, balance v&agrave; worker queue an to&agrave;n.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">F</span>Lock d&ograve;ng tr&#432;&#7899;c khi s&#7917;a<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="tab-group" id="tabs-foru">
        <div class="tab active" onclick="switchTab('tabs-foru','foru-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-foru','foru-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-foru','foru-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="foru-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>for-update.sql</span></div><div class="cmd-body">
<pre><span class="kw">BEGIN</span>;
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">FOR UPDATE</span>;
<span class="kw">UPDATE</span> accounts <span class="kw">SET</span> balance = balance - <span class="num">100</span> <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="kw">COMMIT</span>;

<span class="comment">-- NOWAIT: lỗi ngay nếu row đang bị lock</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">FOR UPDATE NOWAIT</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="foru-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>for-update.sql</span></div><div class="cmd-body">
<pre><span class="kw">START TRANSACTION</span>;
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">FOR UPDATE</span>;
<span class="kw">UPDATE</span> accounts <span class="kw">SET</span> balance = balance - <span class="num">100</span> <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="kw">COMMIT</span>;

<span class="comment">-- NOWAIT (MySQL 8+):</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">FOR UPDATE NOWAIT</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="foru-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>for-update.sql</span></div><div class="cmd-body">
<pre><span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">FOR UPDATE NOWAIT</span>;
<span class="comment">-- Lỗi ngay: ORA-00054 nếu row đang bị lock</span>

<span class="comment">-- WAIT n giây:</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">FOR UPDATE WAIT</span> <span class="num">5</span>;</pre>
        </div></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">Q</span>Worker queue v&#7899;i SKIP LOCKED<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="tab-group" id="tabs-skip">
        <div class="tab active" onclick="switchTab('tabs-skip','skip-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-skip','skip-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-skip','skip-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="skip-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>skip-locked-queue.sql</span></div><div class="cmd-body">
<pre><span class="kw">WITH</span> picked <span class="kw">AS</span> (
  <span class="kw">SELECT</span> id
  <span class="kw">FROM</span> jobs
  <span class="kw">WHERE</span> status = <span class="str">'pending'</span>
  <span class="kw">ORDER BY</span> priority <span class="kw">DESC</span>, id
  <span class="kw">LIMIT</span> <span class="num">10</span>
  <span class="kw">FOR UPDATE SKIP LOCKED</span>
)
<span class="kw">UPDATE</span> jobs j
<span class="kw">SET</span> status = <span class="str">'processing'</span>, locked_at = <span class="fn">NOW</span>()
<span class="kw">FROM</span> picked p <span class="kw">WHERE</span> j.id = p.id
<span class="kw">RETURNING</span> j.*;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="skip-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>skip-locked-queue.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- MySQL 8+: SKIP LOCKED</span>
<span class="kw">START TRANSACTION</span>;
<span class="kw">SELECT</span> id <span class="kw">FROM</span> jobs
<span class="kw">WHERE</span> status = <span class="str">'pending'</span>
<span class="kw">ORDER BY</span> priority <span class="kw">DESC</span>, id
<span class="kw">LIMIT</span> <span class="num">10</span>
<span class="kw">FOR UPDATE SKIP LOCKED</span>;
<span class="comment">-- Sau đó UPDATE các ID vừa lấy được</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="skip-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>skip-locked-queue.sql</span></div><div class="cmd-body">
<pre><span class="kw">SELECT</span> id <span class="kw">FROM</span> jobs
<span class="kw">WHERE</span> status = <span class="str">'PENDING'</span>
<span class="kw">ORDER BY</span> priority <span class="kw">DESC</span>, id
<span class="kw">FETCH FIRST</span> <span class="num">10</span> <span class="kw">ROWS ONLY</span>
<span class="kw">FOR UPDATE SKIP LOCKED</span>;</pre>
        </div></div>
      </div>
      <div class="info-box tip">&#9989; <span><strong>Index cần:</strong> Queue query thường cần index như <code>(status, priority DESC, id)</code> để chọn ít row và lock đúng phạm vi.</span></div>
    </div>
  </div>
</div>

<!-- S5 -->
<div class="module" id="s5">
  <div class="module-header">
    <div class="module-tag">S5 &middot; Deadlock &amp; Hot Rows</div>
    <div class="module-title">Deadlock, Lock Ordering &amp; Hot Rows</div>
    <div class="module-subtitle">Deadlock kh&ocirc;ng ph&#7843;i l&#7895;i b&iacute; &#7849;n. N&oacute; th&#432;&#7901;ng &#273;&#7871;n t&#7915; vi&#7879;c nhi&#7873;u transaction kh&oacute;a c&ugrave;ng t&agrave;i nguy&#234;n theo th&#7913; t&#7921; kh&aacute;c nhau.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">D</span>Deadlock pattern kinh &#273;i&#7875;n<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>deadlock-pattern.txt</span></div><div class="cmd-body">
<pre><span class="comment">Session A                    Session B</span>
BEGIN                        BEGIN
UPDATE account id=1          UPDATE account id=2
wait... UPDATE id=2  &lt;--&gt;   wait... UPDATE id=1

<span class="kw2">A giữ lock id=1, cần id=2</span>
<span class="kw2">B giữ lock id=2, cần id=1</span>
&#8594; database phát hiện deadlock và rollback một transaction</pre>
      </div></div>
      <div class="tab-group" id="tabs-dl">
        <div class="tab active" onclick="switchTab('tabs-dl','dl-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-dl','dl-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-dl','dl-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="dl-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>deadlock-detect.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Xem deadlock log:</span>
<span class="comment">-- postgresql.conf: log_lock_waits = on, deadlock_timeout = 1s</span>

<span class="comment">-- Fix: khóa theo thứ tự id nhỏ trước, id lớn sau</span>
<span class="kw">UPDATE</span> accounts <span class="kw">SET</span> balance = balance - <span class="num">100</span>
<span class="kw">WHERE</span> id = <span class="fn">LEAST</span>(:id1, :id2);

<span class="kw">UPDATE</span> accounts <span class="kw">SET</span> balance = balance + <span class="num">100</span>
<span class="kw">WHERE</span> id = <span class="fn">GREATEST</span>(:id1, :id2);</pre>
        </div></div>
      </div>
      <div class="tab-content" id="dl-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>deadlock-detect.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Xem thông tin deadlock gần nhất:</span>
<span class="kw">SHOW ENGINE INNODB STATUS</span>;
<span class="comment">-- Tìm "LATEST DETECTED DEADLOCK" trong output</span>

<span class="comment">-- innodb_deadlock_detect (mặc định ON) tự kill victim</span>
<span class="kw">SELECT</span> @@innodb_deadlock_detect;
<span class="kw">SELECT</span> @@innodb_lock_wait_timeout;  <span class="comment">-- mặc định 50 giây</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="dl-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>deadlock-detect.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Oracle tự phát hiện deadlock, ghi vào alert log và trace file</span>
<span class="comment">-- ORA-00060: deadlock detected while waiting for resource</span>

<span class="comment">-- Xem deadlock trace:</span>
<span class="kw">SELECT</span> value <span class="kw">FROM</span> v$diag_info <span class="kw">WHERE</span> name = <span class="str">'Default Trace File'</span>;</pre>
        </div></div>
      </div>
      <div class="info-box tip">&#9989; <span><strong>Fix:</strong> Luôn khóa tài nguyên theo cùng thứ tự, ví dụ account id nhỏ trước id lớn sau. Khi bị deadlock, app phải retry transaction idempotent.</span></div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">H</span>Hot row v&agrave; counter ngh&#7869;n c&#7893; chai<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Hot row l&agrave; m&#7897;t d&ograve;ng b&#7883; r&#7845;t nhi&#7873;u transaction update li&#234;n t&#7909;c. D&ugrave; c&oacute; index t&#7889;t, m&#7885;i transaction v&#7851;n ph&#7843;i x&#7871;p h&agrave;ng tr&#234;n c&ugrave;ng row lock.</p>
      <table>
        <thead><tr><th>Pattern</th><th>Gi&#7843;i ph&aacute;p</th></tr></thead>
        <tbody>
          <tr><td>Global counter</td><td>Shard counter theo bucket r&#7891;i aggregate</td></tr>
          <tr><td>Like/view count</td><td>Append event, batch aggregate sau</td></tr>
          <tr><td>Inventory flash sale</td><td>Reserve theo batch/bucket, gi&#7899;i h&#7841;n concurrency</td></tr>
          <tr><td>Job queue</td><td>SKIP LOCKED + index ch&#7885;n job</td></tr>
        </tbody>
      </table>
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>shard-counter.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Sharded counter: tránh hot row bằng cách phân tán</span>
<span class="kw">CREATE TABLE</span> counters (
  entity_id <span class="fn">BIGINT</span> <span class="kw">NOT NULL</span>,
  bucket    <span class="fn">INT</span> <span class="kw">NOT NULL</span>,          <span class="comment">-- 0..9</span>
  count     <span class="fn">BIGINT</span> <span class="kw">NOT NULL DEFAULT</span> <span class="num">0</span>,
  <span class="kw">PRIMARY KEY</span> (entity_id, bucket)
);

<span class="comment">-- Ghi vào bucket ngẫu nhiên</span>
<span class="kw">UPDATE</span> counters
<span class="kw">SET</span> count = count + <span class="num">1</span>
<span class="kw">WHERE</span> entity_id = :id
  <span class="kw">AND</span> bucket = <span class="fn">FLOOR</span>(<span class="fn">RAND</span>() * <span class="num">10</span>);

<span class="comment">-- Đọc tổng:</span>
<span class="kw">SELECT</span> <span class="fn">SUM</span>(count) <span class="kw">FROM</span> counters <span class="kw">WHERE</span> entity_id = :id;</pre>
      </div></div>
    </div>
  </div>
</div>

<!-- S6: Optimistic Locking -->
<div class="module" id="s6">
  <div class="module-header">
    <div class="module-tag">S6 &middot; Optimistic Locking</div>
    <div class="module-title">Optimistic vs Pessimistic Locking</div>
    <div class="module-subtitle">Pessimistic kh&oacute;a s&#7899;m &#273;&#7875; ng&#259;n conflict. Optimistic gi&#7843; s&#7917; kh&ocirc;ng conflict v&agrave; ch&#7881; ki&#7875;m tra khi commit.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">C</span>So s&aacute;nh hai chi&#7871;n l&#432;&#7907;c<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Ti&#234;u ch&iacute;</th><th>Pessimistic</th><th>Optimistic</th></tr></thead>
        <tbody>
          <tr><td>C&#417; ch&#7871;</td><td>SELECT FOR UPDATE — kh&oacute;a row ngay</td><td>Version/timestamp column — ki&#7875;m tra khi UPDATE</td></tr>
          <tr><td>Ph&ugrave; h&#7907;p khi</td><td>Conflict x&#7843;y ra th&#432;&#7901;ng xuy&#234;n, d&#7919; li&#7879;u tranh ch&#7845;p cao</td><td>Conflict hi&#7871;m, read nhi&#7873;u h&#417;n write</td></tr>
          <tr><td>R&#7911;i ro</td><td>Lock wait, deadlock n&#7871;u gi&#7919; l&acirc;u</td><td>C&#7847;n retry khi conflict, OCC overhead</td></tr>
          <tr><td>V&iacute; d&#7909;</td><td>Inventory flash sale, balance transfer</td><td>CMS edit, config update, profile update</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">O</span>Optimistic Locking v&#7899;i version column<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Th&#234;m c&#7897;t <code>version</code> (ho&#7863;c <code>updated_at</code>) v&agrave;o b&#7843;ng. Khi UPDATE, ki&#7875;m tra version v&#7851;n c&ograve;n &#273;&uacute;ng. N&#7871;u b&#7883; &#273;&#7893;i b&#7903;i session kh&aacute;c, UPDATE tr&#7843; v&#7873; 0 rows &rarr; retry.</p>
      <div class="tab-group" id="tabs-opt">
        <div class="tab active" onclick="switchTab('tabs-opt','opt-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-opt','opt-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-opt','opt-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="opt-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>optimistic-lock.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE TABLE</span> articles (
  id         <span class="fn">BIGSERIAL PRIMARY KEY</span>,
  title      <span class="fn">TEXT</span>,
  content    <span class="fn">TEXT</span>,
  version    <span class="fn">BIGINT</span> <span class="kw">NOT NULL DEFAULT</span> <span class="num">0</span>
);

<span class="comment">-- Bước 1: Đọc record (kèm version)</span>
<span class="kw">SELECT</span> id, title, content, version <span class="kw">FROM</span> articles <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="comment">-- Giả sử: version = 5</span>

<span class="comment">-- Bước 2: UPDATE kèm kiểm tra version</span>
<span class="kw">UPDATE</span> articles
<span class="kw">SET</span> title = <span class="str">'New Title'</span>, version = version + <span class="num">1</span>
<span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">AND</span> version = <span class="num">5</span>;  <span class="comment">-- phải khớp version đã đọc</span>

<span class="comment">-- Kiểm tra rowcount: nếu = 0 → conflict → retry</span>
<span class="kw">GET DIAGNOSTICS</span> affected = ROW_COUNT;
<span class="comment">-- hoặc trong app: check rows_affected == 0</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="opt-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>optimistic-lock.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE TABLE</span> articles (
  id         <span class="fn">BIGINT PRIMARY KEY AUTO_INCREMENT</span>,
  title      <span class="fn">VARCHAR</span>(<span class="num">200</span>),
  content    <span class="fn">TEXT</span>,
  version    <span class="fn">BIGINT</span> <span class="kw">NOT NULL DEFAULT</span> <span class="num">0</span>
);

<span class="comment">-- UPDATE với version check</span>
<span class="kw">UPDATE</span> articles
<span class="kw">SET</span> title = <span class="str">'New Title'</span>, version = version + <span class="num">1</span>
<span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">AND</span> version = <span class="num">5</span>;

<span class="comment">-- Kiểm tra: ROW_COUNT() = 0 → conflict → retry</span>
<span class="kw">SELECT</span> ROW_COUNT();</pre>
        </div></div>
      </div>
      <div class="tab-content" id="opt-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>optimistic-lock.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE TABLE</span> articles (
  id         <span class="fn">NUMBER</span> <span class="kw">PRIMARY KEY</span>,
  title      <span class="fn">VARCHAR2</span>(<span class="num">200</span>),
  content    <span class="fn">CLOB</span>,
  version    <span class="fn">NUMBER</span> <span class="kw">DEFAULT</span> <span class="num">0</span> <span class="kw">NOT NULL</span>
);

<span class="comment">-- Cách 1: version column</span>
<span class="kw">UPDATE</span> articles
<span class="kw">SET</span> title = <span class="str">'New Title'</span>, version = version + <span class="num">1</span>
<span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">AND</span> version = <span class="num">5</span>;

<span class="comment">-- Cách 2: Oracle ORA_ROWSCN (SCN thay đổi tự động)</span>
<span class="kw">SELECT</span> id, title, ORA_ROWSCN <span class="kw">FROM</span> articles <span class="kw">WHERE</span> id = <span class="num">1</span>;
<span class="kw">UPDATE</span> articles <span class="kw">SET</span> title = <span class="str">'New Title'</span>
<span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">AND</span> ORA_ROWSCN = :saved_scn;
<span class="comment">-- SQL%ROWCOUNT = 0 → conflict</span></pre>
        </div></div>
      </div>
      <div class="info-box note">&#128204; <span><strong>ORA_ROWSCN:</strong> Oracle có tính năng độc đáo là dùng SCN (System Change Number) như optimistic version mà không cần thêm cột, nhưng cần <code>ROWDEPENDENCIES</code> để chính xác row-level.</span></div>
    </div>
  </div>
</div>

<!-- S7: Savepoint & Lock Timeout -->
<div class="module" id="s7">
  <div class="module-header">
    <div class="module-tag">S7 &middot; Savepoint &amp; Lock Timeout</div>
    <div class="module-title">Savepoint, Partial Rollback &amp; Lock Timeout</div>
    <div class="module-subtitle">Savepoint gi&uacute;p rollback t&#7915;ng ph&#7847;n. Lock timeout b&#7843;o v&#7879; h&#7879; th&#7889;ng kh&#7887;i treo v&ocirc; h&#7841;n khi lock wait.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">S</span>Savepoint &amp; Partial Rollback<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Savepoint cho ph&eacute;p &#273;&#225;nh d&#7845;u m&#7897;t &#273;i&#7875;m trong transaction &#273;&#7875; c&oacute; th&#7875; rollback v&#7873; &#273;i&#7875;m &#273;&oacute; m&agrave; kh&ocirc;ng m&#7845;t to&agrave;n b&#7897; transaction.</p>
      <div class="tab-group" id="tabs-sv">
        <div class="tab active" onclick="switchTab('tabs-sv','sv-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-sv','sv-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-sv','sv-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="sv-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>savepoint.sql</span></div><div class="cmd-body">
<pre><span class="kw">BEGIN</span>;
<span class="kw">INSERT INTO</span> orders(user_id, amount) <span class="kw">VALUES</span> (<span class="num">1</span>, <span class="num">100</span>);

<span class="kw">SAVEPOINT</span> sp1;

<span class="kw">INSERT INTO</span> order_items(order_id, product_id) <span class="kw">VALUES</span> (<span class="num">1</span>, <span class="num">99</span>);
<span class="comment">-- Giả sử step này lỗi: rollback về sp1</span>

<span class="kw">ROLLBACK TO SAVEPOINT</span> sp1;
<span class="comment">-- order vẫn còn, chỉ mất order_items</span>

<span class="kw">RELEASE SAVEPOINT</span> sp1;
<span class="kw">COMMIT</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="sv-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>savepoint.sql</span></div><div class="cmd-body">
<pre><span class="kw">START TRANSACTION</span>;
<span class="kw">INSERT INTO</span> orders(user_id, amount) <span class="kw">VALUES</span> (<span class="num">1</span>, <span class="num">100</span>);

<span class="kw">SAVEPOINT</span> sp1;

<span class="kw">INSERT INTO</span> order_items(order_id, product_id) <span class="kw">VALUES</span> (<span class="num">1</span>, <span class="num">99</span>);

<span class="kw">ROLLBACK TO SAVEPOINT</span> sp1;
<span class="kw">RELEASE SAVEPOINT</span> sp1;
<span class="kw">COMMIT</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="sv-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>savepoint.sql</span></div><div class="cmd-body">
<pre><span class="kw">INSERT INTO</span> orders(id, user_id, amount) <span class="kw">VALUES</span> (<span class="num">1</span>, <span class="num">1</span>, <span class="num">100</span>);

<span class="kw">SAVEPOINT</span> sp1;

<span class="kw">INSERT INTO</span> order_items(order_id, product_id) <span class="kw">VALUES</span> (<span class="num">1</span>, <span class="num">99</span>);

<span class="kw">ROLLBACK TO SAVEPOINT</span> sp1;
<span class="comment">-- RELEASE không bắt buộc trong Oracle</span>
<span class="kw">COMMIT</span>;  <span class="comment">-- chỉ commit phần trước sp1</span></pre>
        </div></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">T</span>Lock Timeout Configuration<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Khi kh&ocirc;ng c&#7845;u h&igrave;nh lock timeout, m&#7897;t request b&#7883; ch&#7863;n bởi lock wait c&oacute; th&#7875; treo v&#244; h&#7841;n l&agrave;m c&#7841;n ki&#7879;t connection pool v&agrave; s&#7853;p to&agrave;n b&#7897; h&#7879; th&#7889;ng.</p>
      <div class="tab-group" id="tabs-lto">
        <div class="tab active" onclick="switchTab('tabs-lto','lto-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-lto','lto-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-lto','lto-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="lto-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>lock-timeout.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Lock timeout: lỗi sau Xms nếu không acquire được lock</span>
<span class="kw">SET</span> lock_timeout = <span class="str">'3s'</span>;
<span class="kw">SET</span> statement_timeout = <span class="str">'30s'</span>;

<span class="comment">-- DDL lock timeout (tránh ALTER TABLE block mãi):</span>
<span class="kw">SET</span> lock_timeout = <span class="str">'2s'</span>;
<span class="kw">ALTER TABLE</span> orders <span class="kw">ADD COLUMN</span> note <span class="fn">TEXT</span>;

<span class="comment">-- Toàn phiên:</span>
<span class="kw">ALTER ROLE</span> app_user <span class="kw">SET</span> lock_timeout = <span class="str">'5s'</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="lto-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>lock-timeout.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- InnoDB lock wait timeout (giây, mặc định 50s)</span>
<span class="kw">SET</span> innodb_lock_wait_timeout = <span class="num">5</span>;

<span class="comment">-- Toàn global:</span>
<span class="kw">SET GLOBAL</span> innodb_lock_wait_timeout = <span class="num">10</span>;

<span class="comment">-- DDL lock (metadata lock):</span>
<span class="kw">SET</span> lock_wait_timeout = <span class="num">3</span>;  <span class="comment">-- cho DDL/metadata lock</span>

<span class="comment">-- Kiểm tra giá trị hiện tại:</span>
<span class="kw">SHOW VARIABLES LIKE</span> <span class="str">'%lock%timeout%'</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="lto-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>lock-timeout.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Oracle: dùng WAIT n trong FOR UPDATE thay vì global timeout</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> accounts <span class="kw">WHERE</span> id = <span class="num">1</span> <span class="kw">FOR UPDATE WAIT</span> <span class="num">3</span>;

<span class="comment">-- DDL lock timeout (ALTER SESSION):</span>
<span class="kw">ALTER SESSION SET</span> ddl_lock_timeout = <span class="num">10</span>;  <span class="comment">-- giây</span>
<span class="kw">ALTER TABLE</span> orders <span class="kw">ADD</span> note <span class="fn">VARCHAR2</span>(<span class="num">200</span>);

<span class="comment">-- Resource Manager có thể kill session chờ quá lâu</span>
<span class="kw">SELECT</span> name, value <span class="kw">FROM</span> v$parameter
<span class="kw">WHERE</span> name <span class="kw">LIKE</span> <span class="str">'%lock%'</span>;</pre>
        </div></div>
      </div>
      <div class="info-box danger">&#128683; <span><strong>Production rule:</strong> Luôn set <code>lock_timeout</code> (Postgres) hoặc <code>innodb_lock_wait_timeout</code> (MySQL) ở mức hợp lý (3&ndash;10 giây) cho OLTP. Timeout mặc định 50 giây của MySQL dễ gây connection pool exhaustion.</span></div>
    </div>
  </div>
</div>

<!-- S8: Oracle Advanced -->
<div class="module" id="s8">
  <div class="module-header">
    <div class="module-tag">S8 &middot; Oracle N&#226;ng cao</div>
    <div class="module-title">Autonomous Transaction &amp; ORA-01555</div>
    <div class="module-subtitle">C&aacute;c t&iacute;nh n&#259;ng &#273;&#7863;c th&ugrave; Oracle kh&ocirc;ng c&oacute; tr&#234;n PostgreSQL hay MySQL.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">A</span>Autonomous Transaction<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Autonomous Transaction l&agrave; m&#7897;t sub-transaction <strong>commit ho&#7863;c rollback &#273;&#7897;c l&#7853;p</strong> m&agrave; kh&ocirc;ng &#7843;nh h&#432;&#7903;ng transaction cha. D&ugrave;ng ph&#7893; bi&#7871;n &#273;&#7875; ghi log/audit ngay c&#7843; khi transaction cha rollback.</p>
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>autonomous-transaction.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Ví dụ: procedure ghi audit log độc lập</span>
<span class="kw">CREATE OR REPLACE PROCEDURE</span> log_action(
  p_action <span class="kw">IN</span> <span class="fn">VARCHAR2</span>,
  p_user   <span class="kw">IN</span> <span class="fn">VARCHAR2</span>
) <span class="kw">AS</span>
  <span class="kw">PRAGMA AUTONOMOUS_TRANSACTION</span>;  <span class="comment">-- khai báo autonomous</span>
<span class="kw">BEGIN</span>
  <span class="kw">INSERT INTO</span> audit_log(action, username, log_time)
  <span class="kw">VALUES</span> (p_action, p_user, <span class="fn">SYSTIMESTAMP</span>);
  <span class="kw">COMMIT</span>;  <span class="comment">-- commit độc lập, không ảnh hưởng transaction cha</span>
<span class="kw">END</span>;
/

<span class="comment">-- Dùng trong transaction cha:</span>
<span class="kw">BEGIN</span>
  <span class="kw">UPDATE</span> orders <span class="kw">SET</span> status = <span class="str">'CANCELLED'</span> <span class="kw">WHERE</span> id = <span class="num">100</span>;
  log_action(<span class="str">'CANCEL_ORDER'</span>, <span class="str">'USER_42'</span>);  <span class="comment">-- audit đã commit</span>
  <span class="kw">ROLLBACK</span>;  <span class="comment">-- rollback order, nhưng audit_log vẫn còn</span>
<span class="kw">END</span>;
/</pre>
      </div></div>
      <div class="info-box tip">&#9989; <span><strong>Use cases:</strong> Audit logging, error logging, sequence generator, caching table. KHÔNG dùng cho business logic chính vì khó debug và tạo side effects.</span></div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">E</span>ORA-01555: Snapshot Too Old<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Oracle g&#7863;p ORA-01555 khi transaction c&#7847;n &#273;&#7885;c d&#7919; li&#7879;u c&#361; t&#7915; undo segment nh&#432;ng undo &#273;&atilde; b&#7883; ghi &#273;&egrave;. Th&#432;&#7901;ng x&#7843;y ra &#7903; c&aacute;c long-running query ho&#7863;c report ch&#7841;y tr&#234;n database &#273;ang write nhi&#7873;u.</p>
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>ora-01555.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Chẩn đoán:</span>
<span class="kw">SELECT</span> name, value <span class="kw">FROM</span> v$parameter
<span class="kw">WHERE</span> name <span class="kw">IN</span> (<span class="str">'undo_retention'</span>, <span class="str">'undo_tablespace'</span>);

<span class="comment">-- Xem undo tablespace hiện tại:</span>
<span class="kw">SELECT</span> tablespace_name, status, retention
<span class="kw">FROM</span> dba_tablespaces
<span class="kw">WHERE</span> contents = <span class="str">'UNDO'</span>;

<span class="comment">-- Fix 1: Tăng undo_retention (giây)</span>
<span class="kw">ALTER SYSTEM SET</span> undo_retention = <span class="num">3600</span>;  <span class="comment">-- 1 giờ</span>

<span class="comment">-- Fix 2: Bật GUARANTEE (giữ undo cho dù tablespace đầy)</span>
<span class="kw">ALTER TABLESPACE</span> undotbs1 <span class="kw">RETENTION GUARANTEE</span>;

<span class="comment">-- Fix 3: Tăng kích thước undo tablespace</span>
<span class="kw">ALTER DATABASE DATAFILE</span> <span class="str">'/path/to/undotbs01.dbf'</span>
<span class="kw">RESIZE</span> <span class="num">4</span>G;

<span class="comment">-- Fix 4: Tối ưu query dài để chạy nhanh hơn</span>
<span class="comment">-- (ít thời gian cần undo hơn)</span></pre>
      </div></div>
      <div class="info-box danger">&#128683; <span><strong>ORA-01555 không phải lỗi data:</strong> Dữ liệu của bạn vẫn ổn. Chỉ là Oracle không còn undo đủ để cung cấp consistent read snapshot cho query đang chạy. Tăng <code>undo_retention</code> và undo tablespace size là giải pháp bền vững nhất.</span></div>
    </div>
  </div>
</div>

<!-- S9: Diagnose -->
<div class="module" id="s9">
  <div class="module-header">
    <div class="module-tag">S9 &middot; Diagnose Locks</div>
    <div class="module-title">Ch&#7849;n &#273;o&aacute;n Lock Waits tr&#234;n PostgreSQL, MySQL, Oracle</div>
    <div class="module-subtitle">Khi production treo, DBA c&#7847;n tr&#7843; l&#7901;i nhanh: ai &#273;ang ch&#7901;, ai &#273;ang gi&#7919; lock, SQL n&agrave;o g&acirc;y ra.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">D</span>Diagnostic SQL<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="tab-group" id="tabs-diag">
        <div class="tab active" onclick="switchTab('tabs-diag','diag-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-diag','diag-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-diag','diag-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="diag-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>diagnose-locks.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Tìm session đang bị blocked và blocking session</span>
<span class="kw">SELECT</span>
  blocked.pid          <span class="kw">AS</span> blocked_pid,
  blocked.query        <span class="kw">AS</span> blocked_query,
  blocked.wait_event   <span class="kw">AS</span> wait_event,
  blocking.pid         <span class="kw">AS</span> blocking_pid,
  blocking.query       <span class="kw">AS</span> blocking_query,
  blocking.state       <span class="kw">AS</span> blocking_state,
  <span class="fn">now</span>() - blocking.xact_start <span class="kw">AS</span> blocking_duration
<span class="kw">FROM</span> pg_stat_activity blocked
<span class="kw">JOIN</span> pg_locks blocked_locks <span class="kw">ON</span> blocked_locks.pid = blocked.pid
<span class="kw">JOIN</span> pg_locks blocking_locks
  <span class="kw">ON</span>  blocking_locks.locktype = blocked_locks.locktype
  <span class="kw">AND</span> blocking_locks.relation <span class="kw">IS NOT DISTINCT FROM</span> blocked_locks.relation
  <span class="kw">AND</span> blocking_locks.transactionid <span class="kw">IS NOT DISTINCT FROM</span> blocked_locks.transactionid
  <span class="kw">AND</span> blocking_locks.pid &lt;&gt; blocked_locks.pid
<span class="kw">JOIN</span> pg_stat_activity blocking <span class="kw">ON</span> blocking.pid = blocking_locks.pid
<span class="kw">WHERE NOT</span> blocked_locks.granted;

<span class="comment">-- Kill blocking session (cẩn thận):</span>
<span class="kw">SELECT</span> <span class="fn">pg_terminate_backend</span>(&lt;blocking_pid&gt;);</pre>
        </div></div>
      </div>
      <div class="tab-content" id="diag-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>diagnose-locks.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Performance Schema (MySQL 8):</span>
<span class="kw">SELECT</span>
  w.requesting_engine_transaction_id <span class="kw">AS</span> waiting_tx,
  w.blocking_engine_transaction_id   <span class="kw">AS</span> blocking_tx,
  r.thread_id   <span class="kw">AS</span> requesting_thread,
  b.thread_id   <span class="kw">AS</span> blocking_thread
<span class="kw">FROM</span> performance_schema.data_lock_waits w
<span class="kw">JOIN</span> performance_schema.data_locks r <span class="kw">ON</span> r.engine_lock_id = w.requesting_engine_lock_id
<span class="kw">JOIN</span> performance_schema.data_locks b <span class="kw">ON</span> b.engine_lock_id = w.blocking_engine_lock_id;

<span class="comment">-- Chi tiết InnoDB status:</span>
<span class="kw">SHOW ENGINE INNODB STATUS</span>\G;

<span class="comment">-- Kill session:</span>
<span class="kw">KILL</span> &lt;process_id&gt;;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="diag-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>diagnose-locks.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Session đang bị block:</span>
<span class="kw">SELECT</span> s.sid, s.serial#, s.username, s.status,
       s.blocking_session, s.seconds_in_wait,
       q.sql_text
<span class="kw">FROM</span> v$session s
<span class="kw">LEFT JOIN</span> v$sql q <span class="kw">ON</span> q.sql_id = s.sql_id
<span class="kw">WHERE</span> s.blocking_session <span class="kw">IS NOT NULL</span>;

<span class="comment">-- Xem lock holder và waiter:</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> dba_blockers;
<span class="kw">SELECT</span> * <span class="kw">FROM</span> dba_waiters;

<span class="comment">-- Chi tiết lock object:</span>
<span class="kw">SELECT</span> l.sid, o.object_name, o.object_type,
       l.locked_mode, s.username
<span class="kw">FROM</span> v$locked_object l
<span class="kw">JOIN</span> dba_objects o <span class="kw">ON</span> o.object_id = l.object_id
<span class="kw">JOIN</span> v$session s <span class="kw">ON</span> s.sid = l.session_id;

<span class="comment">-- Kill session (SID, SERIAL#):</span>
<span class="kw">ALTER SYSTEM KILL SESSION</span> <span class="str">'123,456'</span> <span class="kw">IMMEDIATE</span>;</pre>
        </div></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-summary">E</span>Error catalog &mdash; Lock symptoms<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Tri&#7879;u ch&#7913;ng</th><th>Root cause</th><th>Fix</th></tr></thead>
        <tbody>
          <tr><td>Request treo, CPU th&#7845;p</td><td>Lock wait</td><td>T&igrave;m blocking session, gi&#7843;m transaction length</td></tr>
          <tr><td>Deadlock th&#7881;nh tho&#7843;ng xu&#7845;t hi&#7879;n</td><td>Lock order kh&ocirc;ng nh&#7845;t qu&aacute;n</td><td>Chu&#7849;n h&oacute;a th&#7913; t&#7921; kh&oacute;a, retry transaction</td></tr>
          <tr><td>UPDATE ch&#7863;n nhi&#7873;u session</td><td>WHERE kh&ocirc;ng index, scan nhi&#7873;u row</td><td>Th&#234;m index/rewrite DML/batch nh&#7887;</td></tr>
          <tr><td>Worker x&#7917; l&yacute; tr&ugrave;ng job</td><td>Kh&ocirc;ng kh&oacute;a khi claim job</td><td>FOR UPDATE SKIP LOCKED</td></tr>
          <tr><td>Counter r&#7845;t ch&#7853;m</td><td>Hot row</td><td>Shard counter ho&#7863;c append event</td></tr>
          <tr><td>Request treo m&atilde;i kh&ocirc;ng error</td><td>Kh&ocirc;ng c&#7845;u h&igrave;nh lock timeout</td><td>Set lock_timeout/innodb_lock_wait_timeout</td></tr>
          <tr><td>Oracle ORA-01555</td><td>Undo retention kh&ocirc;ng &#273;&#7911;</td><td>T&#259;ng undo_retention, m&#7903; r&#7897;ng undo tablespace</td></tr>
          <tr><td>Optimistic update m&#7845;t d&#7919; li&#7879;u</td><td>Kh&ocirc;ng ki&#7875;m tra version khi commit</td><td>Th&#234;m version column + check rowcount</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- S10: Interview Prep -->
<div class="module" id="s10">
  <div class="module-header">
    <div class="module-tag">S10 &middot; Interview Prep</div>
    <div class="module-title">Interview Prep &mdash; Transactions &amp; Locks</div>
    <div class="module-subtitle">C&acirc;u h&#7887;i th&#432;&#7901;ng ph&acirc;n bi&#7879;t ng&#432;&#7901;i ch&#7881; bi&#7871;t SQL v&#7899;i ng&#432;&#7901;i hi&#7875;u production concurrency.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-quiz">Q</span>Quick quiz<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="quiz-item">
        <div class="quiz-q">Deadlock th&#432;&#7901;ng x&#7843;y ra khi n&agrave;o?</div>
        <div class="quiz-options">
          <div class="quiz-opt" onclick="answerQuiz(this,false,'Query ch&#7853;m c&oacute; th&#7875; g&acirc;y lock wait l&acirc;u, nh&#432;ng deadlock c&#7847;n v&ograve;ng ch&#7901;.')">A. Khi m&#7897;t query ch&#7841;y l&acirc;u</div>
          <div class="quiz-opt" onclick="answerQuiz(this,true,'&#272;&uacute;ng. Deadlock l&agrave; v&ograve;ng ch&#7901;: A gi&#7919; lock B c&#7847;n, B gi&#7919; lock A c&#7847;n.')">B. Khi c&aacute;c transaction gi&#7919; lock v&agrave; ch&#7901; nhau theo v&ograve;ng</div>
          <div class="quiz-opt" onclick="answerQuiz(this,false,'Thi&#7871;u index c&oacute; th&#7875; t&#259;ng lock scope, nh&#432;ng kh&ocirc;ng ph&#7843;i &#273;&#7883;nh ngh&#297;a deadlock.')">C. Khi b&#7843;ng thi&#7871;u index</div>
        </div>
        <div class="quiz-explain"></div>
      </div>
      <div class="quiz-item">
        <div class="quiz-q">Optimistic Locking kh&aacute;c Pessimistic Locking ch&#7911; y&#7871;u &#7903; &#273;i&#7875;m n&agrave;o?</div>
        <div class="quiz-options">
          <div class="quiz-opt" onclick="answerQuiz(this,false,'Kh&ocirc;ng ph&#7843;i. C&#7843; hai &#273;&#7873;u c&oacute; th&#7875; d&ugrave;ng transaction.')">A. Optimistic kh&ocirc;ng d&ugrave;ng transaction</div>
          <div class="quiz-opt" onclick="answerQuiz(this,true,'&#272;&uacute;ng. Pessimistic kh&oacute;a row s&#7899;m (FOR UPDATE). Optimistic ch&#7881; ki&#7875;m tra conflict khi UPDATE qua version/timestamp.')">B. Pessimistic kh&oacute;a row ngay; Optimistic ki&#7875;m tra conflict khi commit</div>
          <div class="quiz-opt" onclick="answerQuiz(this,false,'Sai. Optimistic c&oacute; th&#7875; nhanh h&#417;n v&igrave; &iacute;t lock wait khi conflict hi&#7871;m.')">C. Optimistic lu&ocirc;n ch&#7853;m h&#417;n</div>
        </div>
        <div class="quiz-explain"></div>
      </div>
      <div class="quiz-item">
        <div class="quiz-q">Pattern n&agrave;o ph&ugrave; h&#7907;p &#273;&#7875; nhi&#7873;u worker c&ugrave;ng l&#7845;y job m&agrave; kh&ocirc;ng x&#7917; l&yacute; tr&ugrave;ng?</div>
        <div class="quiz-options">
          <div class="quiz-opt" onclick="answerQuiz(this,false,'SELECT th&#432;&#7901;ng kh&ocirc;ng kh&oacute;a job, worker kh&aacute;c v&#7851;n c&oacute; th&#7875; l&#7845;y c&ugrave;ng row.')">A. SELECT job pending r&#7891;i update sau</div>
          <div class="quiz-opt" onclick="answerQuiz(this,true,'&#272;&uacute;ng. FOR UPDATE SKIP LOCKED gi&uacute;p worker b&#7887; qua row &#273;&atilde; b&#7883; lock b&#7903;i worker kh&aacute;c.')">B. FOR UPDATE SKIP LOCKED trong transaction ng&#7855;n</div>
          <div class="quiz-opt" onclick="answerQuiz(this,false,'ORDER BY ch&#7881; quy&#7871;t &#273;&#7883;nh th&#7913; t&#7921;, kh&ocirc;ng gi&#7843;i quy&#7871;t concurrency.')">C. ORDER BY priority DESC</div>
        </div>
        <div class="quiz-explain"></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">S</span>Senior answer templates<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <h3 class="blue">Q1: Production b&#7883; treo do lock, b&#7841;n l&agrave;m g&igrave;?</h3>
      <p>T&ocirc;i t&igrave;m blocking session v&agrave; blocked sessions tr&#432;&#7899;c, l&#7845;y SQL &#273;ang ch&#7841;y, th&#7901;i gian transaction, app user v&agrave; object b&#7883; lock. Sau &#273;&oacute; &#273;&aacute;nh gi&aacute; c&oacute; th&#7875; kill session kh&ocirc;ng, gi&#7843;m batch/transaction length, th&#234;m index cho DML ho&#7863;c s&#7917;a th&#7913; t&#7921; lock. Sau incident c&#7847;n th&#234;m monitoring lock wait v&agrave; review code path gi&#7919; transaction l&acirc;u.</p>
      <h3 class="green">Q2: Khi n&agrave;o d&ugrave;ng Optimistic, khi n&agrave;o d&ugrave;ng Pessimistic?</h3>
      <p>D&ugrave;ng <strong>Pessimistic</strong> khi conflict x&#7843;y ra th&#432;&#7901;ng xuy&#234;n (inventory flash sale, balance transfer) &mdash; kh&oacute;a s&#7899;m gi&uacute;p &#273;&#7843;m b&#7843;o consistency. D&ugrave;ng <strong>Optimistic</strong> khi read nhi&#7873;u h&#417;n write, conflict hi&#7871;m (CMS, config update) &mdash; hi&#7879;u n&#259;ng cao h&#417;n v&igrave; kh&ocirc;ng lock wait. Optimistic c&#7847;n app retry khi ph&aacute;t hi&#7879;n conflict (rowcount=0).</p>
      <h3 class="orange">Q3: MVCC c&oacute; ngh&#297;a l&agrave; kh&ocirc;ng c&#7847;n lock kh&ocirc;ng?</h3>
      <p>Kh&ocirc;ng. MVCC gi&uacute;p read kh&ocirc;ng block write trong nhi&#7873;u tr&#432;&#7901;ng h&#7907;p b&#7857;ng snapshot/versioning. Nh&#432;ng writers v&#7851;n ph&#7843;i lock rows khi update/delete, v&agrave; SELECT FOR UPDATE v&#7851;n kh&oacute;a ch&#7911; &#273;&#7897;ng. MVCC c&ograve;n t&#7841;o chi ph&iacute; cleanup version c&#361; (VACUUM/purge/undo).</p>
      <h3 class="red">Q4: Oracle Autonomous Transaction d&ugrave;ng khi n&agrave;o?</h3>
      <p>D&ugrave;ng khi c&#7847;n m&#7897;t sub-routine commit &#273;&#7897;c l&#7853;p v&#7899;i transaction cha, &#273;i&#7875;n h&igrave;nh l&agrave; audit logging &mdash; ghi log ph&#7843;i th&agrave;nh c&ocirc;ng d&ugrave; business transaction c&oacute; rollback. Kh&ocirc;ng d&ugrave;ng cho business logic ch&iacute;nh v&igrave; kh&oacute; debug v&agrave; t&#7841;o side effects kh&oacute; d&#7921; &#273;o&aacute;n.</p>
    </div>
  </div>
</div>

<!-- S11: Checklist -->
<div class="module" id="s11">
  <div class="module-header">
    <div class="module-tag">S11 &middot; Summary</div>
    <div class="module-title">Checklist &amp; T&#7893;ng k&#7871;t Module 05</div>
    <div class="module-subtitle">Ho&agrave;n th&agrave;nh checklist n&agrave;y tr&#432;&#7899;c khi chuy&#7875;n sang Operations &amp; Monitoring.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-summary">S</span>Summary &mdash; &#272;i&#7875;m ch&#7889;t c&#7847;n nh&#7899;<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="summary-grid">
        <div class="summary-item"><strong>Transaction c&agrave;ng ng&#7855;n c&agrave;ng t&#7889;t</strong>Lock &#273;&#432;&#7907;c gi&#7919; &#273;&#7871;n commit/rollback.</div>
        <div class="summary-item"><strong>Isolation l&agrave; trade-off</strong>C&agrave;ng m&#7841;nh c&agrave;ng d&#7877; t&#259;ng conflict/retry/lock cost.</div>
        <div class="summary-item"><strong>MVCC kh&ocirc;ng lo&#7841;i b&#7887; write lock</strong>Readers d&#7877; th&#7903; h&#417;n, writers v&#7851;n c&#7841;nh tranh row.</div>
        <div class="summary-item"><strong>Index gi&#7843;m lock scope</strong>DML kh&ocirc;ng index c&oacute; th&#7875; scan v&agrave; lock r&#7897;ng h&#417;n.</div>
        <div class="summary-item"><strong>Deadlock c&#7847;n retry</strong>Fix root cause, nh&#432;ng app v&#7851;n n&#234;n retry transaction an to&agrave;n.</div>
        <div class="summary-item"><strong>SKIP LOCKED cho queue</strong>Pattern chu&#7849;n cho nhi&#7873;u worker claim job.</div>
        <div class="summary-item"><strong>Optimistic cho read-heavy</strong>Version column + check rowcount khi conflict hi&#7871;m.</div>
        <div class="summary-item"><strong>Lock timeout b&#7855;t bu&#7897;c</strong>Kh&ocirc;ng set timeout = request treo v&ocirc; h&#7841;n.</div>
        <div class="summary-item"><strong>SPM vs Autonomous Tx</strong>Autonomous &#273;&#7897;c l&#7853;p v&#7899;i transaction cha &mdash; ch&#7881; d&ugrave;ng cho audit/log.</div>
        <div class="summary-item"><strong>ORA-01555</strong>T&#259;ng undo_retention + tablespace size khi query d&agrave;i tr&#234;n Oracle.</div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-practice">D</span>Definition of Done<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p class="progress-text" id="checklist-progress-text">0/11 m&#7909;c ho&agrave;n th&agrave;nh (0%)</p>
      <div class="progress-bar"><div class="progress-fill" id="checklist-progress-fill"></div></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Gi&#7843;i th&iacute;ch &#273;&#432;&#7907;c ACID v&agrave; v&igrave; sao transaction d&agrave;i g&acirc;y lock wait.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Ph&acirc;n bi&#7879;t READ COMMITTED, REPEATABLE READ, SERIALIZABLE &#7903; m&#7913;c th&#7921;c d&#7909;ng.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Hi&#7875;u MVCC tr&#234;n PostgreSQL/MySQL/Oracle v&agrave; chi ph&iacute; cleanup version c&#361;.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>D&ugrave;ng &#273;&#432;&#7907;c <code>FOR UPDATE</code>, <code>NOWAIT</code>, <code>SKIP LOCKED</code>.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Bi&#7871;t ph&acirc;n t&iacute;ch deadlock v&agrave; chu&#7849;n h&oacute;a th&#7913; t&#7921; kh&oacute;a.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Implement Optimistic Locking v&#7899;i version column v&agrave; ki&#7875;m tra rowcount.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>D&ugrave;ng &#273;&#432;&#7907;c SAVEPOINT v&agrave; ROLLBACK TO SAVEPOINT.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>C&#7845;u h&igrave;nh lock timeout tr&#234;n PostgreSQL v&agrave; MySQL cho m&ocirc;i tr&#432;&#7901;ng OLTP.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Gi&#7843;i th&iacute;ch Oracle Autonomous Transaction v&agrave; khi n&agrave;o d&ugrave;ng.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Bi&#7871;t x&#7917; l&yacute; ORA-01555 b&#7857;ng undo_retention v&agrave; tablespace.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Ch&#7841;y &#273;&#432;&#7907;c SQL ch&#7849;n &#273;o&aacute;n lock wait tr&#234;n PostgreSQL, MySQL v&agrave; Oracle.</span></div>
    </div>
  </div>
</div>

  </main>
</div>

<script>
const navItems = document.querySelectorAll('.nav-item');
let currentModule = 0;
const totalModules = 12;

function showModule(index, navEl) {
  document.querySelectorAll('.module').forEach(m => m.classList.remove('active'));
  const target = document.getElementById('s' + index);
  if (target) { target.classList.add('active'); currentModule = index; window.scrollTo({top: 0, behavior: 'smooth'}); }
  navItems.forEach(n => n.classList.remove('active'));
  if (navEl) { navEl.classList.add('active'); }
  else { if (navItems[index]) navItems[index].classList.add('active'); }
}

function toggleSection(header) {
  const content = header.nextElementSibling;
  const toggle = header.querySelector('.section-toggle');
  const isHidden = content.style.display === 'none';
  content.style.display = isHidden ? 'block' : 'none';
  toggle.textContent = isHidden ? '\\u25BC' : '\\u25B6';
}

function answerQuiz(el, isCorrect, msg) {
  const item = el.closest('.quiz-item');
  const opts = item.querySelectorAll('.quiz-opt');
  const explain = item.querySelector('.quiz-explain');
  opts.forEach(opt => (opt.style.pointerEvents = 'none'));
  el.classList.add(isCorrect ? 'correct' : 'wrong');
  if (!isCorrect) { opts.forEach(opt => { const o = opt.getAttribute('onclick'); if (o && o.includes('true')) opt.classList.add('correct'); }); }
  explain.textContent = (isCorrect ? '\\u2713 Ch\\u00EDnh x\\u00E1c! ' : '\\u2717 Sai. ') + msg;
  explain.classList.add('show');
}

function toggleSolution(btn) {
  const box = btn.nextElementSibling;
  const show = box.classList.toggle('show');
  btn.textContent = show ? '\\u1F316 \\u1EA8n l\\u1EDD\\u1EDD gi\\u1EA3i' : '\\u1F4A1 Xem l\\u1EDD\\u1EDD gi\\u1EA3i';
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
  if (text) text.textContent = `${checked}/${total} m\\u1EE5c ho\\u00E0n th\\u00E0nh (${pct}%)`;
}

showModule(0, navItems[0]);
updateProgress();
</script>
</body>
</html>'''

with open('D:/DE/Tuning_SQL/Module05_Transactions_Locks_Concurrency_new.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
