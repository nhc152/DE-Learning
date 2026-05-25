html = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Module 04 — Optimizer &amp; Execution Plan</title>
<meta name="description" content="Hướng dẫn đọc Execution Plan, Statistics, Join Algorithms, Plan Regression và các tính năng nâng cao Oracle trên PostgreSQL, MySQL, Oracle.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{--bg:#0d1117;--surface:#161b22;--surface2:#21262d;--border:#30363d;--accent:#58a6ff;--accent2:#3fb950;--accent3:#f78166;--accent4:#d2a8ff;--accent5:#ffa657;--text:#e6edf3;--text-muted:#8b949e;--code-bg:#0d1117;--highlight:#388bfd26}
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
  .module{display:none}
  .module.active{display:block}
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
  ul,ol{padding-left:20px;margin-bottom:12px}
  li{font-size:.88rem;margin-bottom:5px}
  strong{color:var(--text)}
  .cmd-block{background:var(--code-bg);border:1px solid var(--border);border-radius:8px;margin:12px 0;overflow:hidden}
  .cmd-header{display:flex;align-items:center;justify-content:space-between;padding:8px 14px;background:var(--surface2);border-bottom:1px solid var(--border);font-size:.72rem;color:var(--text-muted);font-family:'JetBrains Mono',monospace}
  .cmd-body{padding:14px}
  pre{font-family:'JetBrains Mono','Courier New','Consolas',monospace;font-size:.82rem;line-height:1.6;white-space:pre;overflow-x:auto;color:var(--text)}
  .kw{color:#ff7b72}.kw2{color:var(--accent)}.str{color:var(--accent5)}.fn{color:var(--accent4)}.num{color:#79c0ff}.comment{color:var(--text-muted)}
  .db-tag{display:inline-block;padding:2px 8px;border-radius:4px;font-size:.68rem;font-weight:700;letter-spacing:.5px;margin-bottom:6px;margin-right:4px}
  .db-pg{background:#4169e122;color:#4d9de0;border:1px solid #4169e155}
  .db-my{background:#f0931322;color:#f09313;border:1px solid #f0931355}
  .db-oracle{background:#cc000022;color:#f97316;border:1px solid #cc000055}
  code{font-family:'JetBrains Mono',monospace;background:var(--surface2);border:1px solid var(--border);padding:1px 6px;border-radius:4px;font-size:.82rem;color:var(--accent4)}
  .tab-group{display:flex;gap:4px;margin:14px 0 0;padding:0 0 0 0;border-bottom:2px solid var(--border)}
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
  .check-box.checked::after{content:'checkmark';font-size:10px;color:#000;font-weight:600}
  .progress-text{font-size:.8rem;color:var(--text-muted);margin-bottom:8px}
  @media(max-width:768px){.sidebar{display:none}.main{padding:16px}.summary-grid{grid-template-columns:1fr}}
</style>
</head>
<body>

<div class="hero">
  <h1>Module 04 &mdash; Optimizer &amp; Execution Plan</h1>
  <p>Hiểu cách database chọn plan, đọc execution plan, xử lý statistics sai và kiểm soát plan regression.<br>Bao gồm Index Skip Scan, SQL Plan Management và Parallel Query trên Oracle.</p>
  <div class="badge-row">
    <span class="badge badge-purple">DBA Core</span>
    <span class="badge badge-green">~5&ndash;7 ng&agrave;y</span>
    <span class="badge badge-blue">Query Optimizer</span>
    <span class="badge badge-orange">PostgreSQL &middot; MySQL &middot; Oracle</span>
  </div>
</div>

<div class="container">
  <nav class="sidebar">
    <div class="sidebar-title">Module Navigation</div>
    <div class="level-label">MODULE 04 &middot; OPTIMIZER &amp; PLAN</div>
    <div class="nav-item active" onclick="showModule(0,this)"><span class="nav-number">S0</span>T&#7893;ng quan &amp; M&#7909;c ti&#234;u</div>
    <div class="nav-item" onclick="showModule(1,this)"><span class="nav-number">S1</span>Optimizer n&#7873;n t&#7843;ng</div>
    <div class="nav-item" onclick="showModule(2,this)"><span class="nav-number">S2</span>&#272;&#7885;c Execution Plan</div>
    <div class="nav-item" onclick="showModule(3,this)"><span class="nav-number">S3</span>Join Algorithms</div>
    <div class="nav-item" onclick="showModule(4,this)"><span class="nav-number">S4</span>Statistics &amp; Histogram</div>
    <div class="nav-item" onclick="showModule(5,this)"><span class="nav-number">S5</span>Plan Regression</div>
    <div class="nav-item" onclick="showModule(6,this)"><span class="nav-number">S6</span>Oracle N&#226;ng cao</div>
    <div class="nav-item" onclick="showModule(7,this)"><span class="nav-number">S7</span>L&#7895;i th&#432;&#7901;ng g&#7863;p</div>
    <div class="nav-item" onclick="showModule(8,this)"><span class="nav-number">S8</span>Interview Prep</div>
    <div class="nav-item" onclick="showModule(9,this)"><span class="nav-number">S9</span>Checklist &amp; T&#7893;ng k&#7871;t</div>
  </nav>

  <main class="main">

<!-- ===== S0 ===== -->
<div class="module active" id="s0">
  <div class="module-header">
    <div class="module-tag">S0 &middot; Orientation</div>
    <div class="module-title">T&#7893;ng quan &amp; M&#7909;c ti&#234;u Module 04</div>
    <div class="module-subtitle">Optimizer l&agrave; b&#7897; n&atilde;o ch&#7885;n c&aacute;ch ch&#7841;y query. DBA c&#7847;n &#273;&#7885;c &#273;&#432;&#7907;c plan, bi&#7871;t optimizer sai &#7903; &#273;&#226;u v&agrave; s&#7917;a &#273;&#250;ng ch&#7895;.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-summary">M</span>Roadmap 10 sections<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Section</th><th>T&#234;n section</th><th>Tr&#7885;ng t&#226;m</th></tr></thead>
        <tbody>
          <tr><td>S0</td><td>T&#7893;ng quan</td><td>Optimizer gi&#7843;i quy&#7871;t v&#7845;n &#273;&#7873; g&igrave;</td></tr>
          <tr><td>S1</td><td>Optimizer n&#7873;n t&#7843;ng</td><td>Cost, cardinality, selectivity, predicate pushdown</td></tr>
          <tr><td>S2</td><td>&#272;&#7885;c Execution Plan</td><td>EXPLAIN tr&#234;n PostgreSQL/MySQL/Oracle</td></tr>
          <tr><td>S3</td><td>Join Algorithms</td><td>Nested Loop, Hash Join, Merge Join</td></tr>
          <tr><td>S4</td><td>Statistics &amp; Histogram</td><td>Khi &#432;&#7899;c l&#432;&#7907;ng row sai l&agrave;m plan sai</td></tr>
          <tr><td>S5</td><td>Plan Regression</td><td>Bind variables, hints, plan stability</td></tr>
          <tr><td>S6</td><td>Oracle N&#226;ng cao</td><td>Index Skip Scan, SQL Plan Management, Parallel Query, Adaptive Optimization</td></tr>
          <tr><td>S7</td><td>L&#7895;i th&#432;&#7901;ng g&#7863;p</td><td>Error catalog v&agrave; c&aacute;ch fix</td></tr>
          <tr><td>S8</td><td>Interview Prep</td><td>C&#226;u h&#7887;i DBA/backend senior</td></tr>
          <tr><td>S9</td><td>Checklist &amp; T&#7893;ng k&#7871;t</td><td>Definition of Done</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-purpose">T</span>Optimizer gi&#7843;i quy&#7871;t v&#7845;n &#273;&#7873; g&igrave;?<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <h3 class="blue">M&#7897;t query c&oacute; nhi&#7873;u c&aacute;ch ch&#7841;y</h3>
      <p>C&ugrave;ng m&#7897;t c&acirc;u SQL c&oacute; th&#7875; ch&#7841;y b&#7857;ng full scan, index scan, nested loop, hash join, sort ho&#7863;c &#273;&#7885;c index theo th&#7913; t&#7921;. Optimizer ch&#7885;n plan c&oacute; cost th&#7845;p nh&#7845;t d&#7921;a tr&#234;n statistics, index, constraint v&agrave; tham s&#7889; query.</p>
      <div class="mental-model"><strong>Mental model:</strong> SQL n&oacute;i "mu&#7889;n k&#7871;t qu&#7843; g&igrave;". Execution plan n&oacute;i "database s&#7869; l&#7845;y k&#7871;t qu&#7843; b&#7857;ng &#273;&#432;&#7901;ng n&agrave;o". DBA tuning l&agrave; ki&#7875;m tra con &#273;&#432;&#7901;ng &#273;&oacute; c&oacute; h&#7907;p l&yacute; kh&ocirc;ng.</div>
      <h3 class="orange">Khi optimizer sai, th&#432;&#7901;ng kh&ocirc;ng ph&#7843;i v&igrave; n&oacute; k&eacute;m</h3>
      <ul>
        <li>Statistics c&#361; ho&#7863;c histogram thi&#7871;u.</li>
        <li>Cardinality estimate sai v&igrave; d&#7919; li&#7879;u l&#7879;ch/skewed.</li>
        <li>Predicate kh&oacute; hi&#7875;u: function tr&#234;n c&#7897;t, type mismatch, expression ph&#7913;c t&#7841;p.</li>
        <li>Bind variable l&agrave;m optimizer kh&ocirc;ng bi&#7871;t gi&aacute; tr&#7883; th&#7853;t t&#7841;i parse time.</li>
      </ul>
    </div>
  </div>
</div>

<!-- ===== S1 ===== -->
<div class="module" id="s1">
  <div class="module-header">
    <div class="module-tag">S1 &middot; Foundations</div>
    <div class="module-title">Cost-Based Optimizer t&#7915; g&#7889;c</div>
    <div class="module-subtitle">Mu&#7889;n &#273;&#7885;c plan t&#7889;t, tr&#432;&#7899;c h&#7871;t ph&#7843;i hi&#7875;u optimizer &#432;&#7899;c l&#432;&#7907;ng s&#7889; d&ograve;ng v&agrave; chi ph&iacute; nh&#432; th&#7871; n&agrave;o.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">C</span>Cost, cardinality, selectivity<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Kh&aacute;i ni&#7879;m</th><th>&#221; ngh&#297;a</th><th>V&igrave; sao quan tr&#7885;ng</th></tr></thead>
        <tbody>
          <tr><td>Cardinality</td><td>S&#7889; d&ograve;ng optimizer ngh&#297; s&#7869; tr&#7843; v&#7873;</td><td>Sai cardinality k&eacute;o theo sai join order/algorithm</td></tr>
          <tr><td>Selectivity</td><td>T&#7927; l&#7879; d&ograve;ng match predicate</td><td>C&#7897;t c&agrave;ng selective, index c&agrave;ng c&oacute; c&#417; h&#7897;i h&#7919;u &iacute;ch</td></tr>
          <tr><td>Cost</td><td>&#431;&#7899;c l&#432;&#7907;ng chi ph&iacute; t&#432;&#417;ng &#273;&#7889;i</td><td>Kh&ocirc;ng ph&#7843;i th&#7901;i gian tuy&#7879;t &#273;&#7889;i, d&ugrave;ng &#273;&#7875; so plan</td></tr>
          <tr><td>Statistics</td><td>Th&ocirc;ng tin ph&acirc;n b&#7889; d&#7919; li&#7879;u</td><td>N&#7873;n t&#7843;ng &#273;&#7875; optimizer &#432;&#7899;c l&#432;&#7907;ng</td></tr>
        </tbody>
      </table>
      <div class="info-box note">&#128204; <span><strong>&#272;i&#7875;m ch&#7889;t:</strong> Khi plan x&#7845;u, ki&#7875;m tra estimated rows tr&#432;&#7899;c. N&#7871;u estimated rows l&#7879;ch xa actual rows, v&#7845;n &#273;&#7873; th&#432;&#7901;ng n&#7857;m &#7903; statistics ho&#7863;c predicate shape.</span></div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">P</span>Predicate Pushdown &amp; Subquery Unnesting<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Tr&#432;&#7899;c khi t&#7841;o plan, optimizer <em>rewrite</em> l&#7841;i c&#226;u SQL &#273;&#7875; &#273;&#7849;y c&aacute;c &#273;i&#7873;u ki&#7879;n <code>WHERE</code> v&agrave;o s&acirc;u b&#234;n trong subquery/view (predicate pushdown) ho&#7863;c bi&#7871;n subquery th&agrave;nh JOIN (unnesting) nh&#7857;m t&#7899;i &#432;u sớm.</p>
      <div class="tab-group" id="tabs-push">
        <div class="tab active" onclick="switchTab('tabs-push','push-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-push','push-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-push','push-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="push-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>predicate-pushdown.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- PostgreSQL t&#7921; &#273;&#7897;ng push WHERE v&agrave;o trong CTE/subquery</span>
<span class="kw">EXPLAIN</span> (<span class="kw2">ANALYZE, VERBOSE</span>)
<span class="kw">SELECT</span> * <span class="kw">FROM</span> (
  <span class="kw">SELECT</span> * <span class="kw">FROM</span> orders
) sub
<span class="kw">WHERE</span> user_id = <span class="num">42</span>;
<span class="comment">-- Optimizer nh&#7853;n ra v&agrave; push: "Filter: (user_id = 42)" xu&#7889;ng table scan</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="push-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>predicate-pushdown.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- MySQL 8 c&oacute; derived condition pushdown</span>
<span class="kw">EXPLAIN FORMAT=TREE</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> (
  <span class="kw">SELECT</span> id, user_id, amount <span class="kw">FROM</span> orders
) sub
<span class="kw">WHERE</span> user_id = <span class="num">42</span>;
<span class="comment">-- K&#7871;t qu&#7843;: index lookup tr&#234;n b&#7843;ng g&#7889;c, kh&ocirc;ng materialize subquery</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="push-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>predicate-pushdown.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Oracle: ki&#7875;m tra xem predicate c&oacute; &#273;&#432;&#7907;c push kh&ocirc;ng</span>
<span class="kw">EXPLAIN PLAN FOR</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> (
  <span class="kw">SELECT</span> * <span class="kw">FROM</span> orders
) sub
<span class="kw">WHERE</span> user_id = <span class="num">42</span>;

<span class="kw">SELECT</span> * <span class="kw">FROM TABLE</span>(<span class="fn">DBMS_XPLAN.DISPLAY</span>(format =&gt; <span class="str">'BASIC +PREDICATE'</span>));
<span class="comment">-- N&#7871;u th&#7845;y "Predicate Information: access("USER_ID"=42)" th&igrave; &#273;&atilde; push th&agrave;nh c&ocirc;ng</span>
<span class="comment">-- N&#7871;u th&#7845;y "filter" th&igrave; ch&#432;a push &#273;&#432;&#7907;c, c&#7847;n rewrite query</span></pre>
        </div></div>
      </div>
      <div class="info-box warn">&#9888;&#65039; <span><strong>D&#7845;u hi&#7879;u ch&#432;a push:</strong> Plan hi&#7875;n th&#7883; <code>FILTER</code> sau khi materialize subquery, ho&#7863;c <code>HASH JOIN</code> tr&#234;n to&agrave;n b&#7897; b&#7843;ng thay v&igrave; index lookup.</span></div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">F</span>Flow ch&#7885;n plan<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>optimizer-flow.txt</span></div><div class="cmd-body">
<pre><span class="kw2">SQL text</span>
    &#9474; parse / validate
    &#9660;
<span class="kw2">Rewrite</span>  <span class="comment">-- view merge, subquery unnest, predicate pushdown</span>
    &#9474;
    &#9660;
<span class="kw2">Estimate cardinality</span>  <span class="comment">-- stats, histogram, constraints</span>
    &#9474;
    &#9660;
<span class="kw2">Enumerate plans</span>  <span class="comment">-- access path, join order, join method</span>
    &#9474;
    &#9660;
<span class="kw2">Pick lowest cost plan</span>
    &#9474;
    &#9660;
<span class="kw2">Execute</span></pre>
      </div></div>
    </div>
  </div>
</div>

<!-- ===== S2 ===== -->
<div class="module" id="s2">
  <div class="module-header">
    <div class="module-tag">S2 &middot; Reading Plans</div>
    <div class="module-title">&#272;&#7885;c Execution Plan tr&#234;n 3 h&#7879; qu&#7843;n tr&#7883;</div>
    <div class="module-subtitle">Kh&ocirc;ng ch&#7881; nh&igrave;n "c&oacute; d&ugrave;ng index kh&ocirc;ng". Ph&#7843;i &#273;&#7885;c t&#7915; data access, rows estimate, join order, sort/hash v&agrave; actual time.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">E</span>EXPLAIN commands<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="tab-group" id="tabs-explain">
        <div class="tab active" onclick="switchTab('tabs-explain','explain-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-explain','explain-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-explain','explain-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="explain-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>explain-commands.sql</span></div><div class="cmd-body">
<pre><span class="kw">EXPLAIN</span> (<span class="kw2">ANALYZE, BUFFERS, VERBOSE</span>)
<span class="kw">SELECT</span> *
<span class="kw">FROM</span> orders
<span class="kw">WHERE</span> user_id = <span class="num">42</span>
<span class="kw">ORDER BY</span> created_at <span class="kw">DESC</span>
<span class="kw">LIMIT</span> <span class="num">20</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="explain-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>explain-commands.sql</span></div><div class="cmd-body">
<pre><span class="kw">EXPLAIN FORMAT=TREE</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> orders
<span class="kw">WHERE</span> user_id = <span class="num">42</span>
<span class="kw">ORDER BY</span> created_at <span class="kw">DESC</span>
<span class="kw">LIMIT</span> <span class="num">20</span>;

<span class="comment">-- Ch&#7841;y th&#7853;t v&agrave; l&#7845;y actual time:</span>
<span class="kw">EXPLAIN ANALYZE</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> orders <span class="kw">WHERE</span> user_id = <span class="num">42</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="explain-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>explain-commands.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Plan d&#7921; ki&#7871;n (ch&#432;a th&#7921;c s&#7921; ch&#7841;y)</span>
<span class="kw">EXPLAIN PLAN FOR</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> orders <span class="kw">WHERE</span> user_id = <span class="num">42</span>
<span class="kw">ORDER BY</span> created_at <span class="kw">DESC</span>;

<span class="kw">SELECT</span> * <span class="kw">FROM TABLE</span>(
  <span class="fn">DBMS_XPLAN.DISPLAY</span>(format =&gt; <span class="str">'BASIC +PREDICATE +COST'</span>)
);

<span class="comment">-- Plan th&#7921;c t&#7871; sau khi ch&#7841;y query (ch&iacute;nh x&aacute;c h&#417;n):</span>
<span class="kw">SELECT</span> <span class="comment">/*+ GATHER_PLAN_STATISTICS */</span> * <span class="kw">FROM</span> orders <span class="kw">WHERE</span> user_id = <span class="num">42</span>;

<span class="kw">SELECT</span> * <span class="kw">FROM TABLE</span>(
  <span class="fn">DBMS_XPLAN.DISPLAY_CURSOR</span>(format =&gt; <span class="str">'ALLSTATS LAST +PEEKED_BINDS'</span>)
);</pre>
        </div></div>
        <div class="info-box warn">&#9888;&#65039; <span><strong>Oracle:</strong> <code>EXPLAIN PLAN</code> l&agrave; plan d&#7921; ki&#7871;n. Mu&#7889;n xem actual rows/time sau khi ch&#7841;y, d&ugrave;ng <code>DBMS_XPLAN.DISPLAY_CURSOR('ALLSTATS LAST')</code>.</span></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">R</span>C&aacute;ch &#273;&#7885;c plan nhanh<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <ol>
        <li>&#272;&#7885;c node tr&#7843; v&#7873; cu&#7889;i c&ugrave;ng tr&#432;&#7899;c &#273;&#7875; hi&#7875;u output.</li>
        <li>T&igrave;m full scan, sort, hash aggregate, temporary table, nested loop l&#7899;n.</li>
        <li>So s&aacute;nh estimated rows v&#7899;i actual rows.</li>
        <li>Ki&#7875;m tra predicate n&#7857;m &#7903; access condition hay filter condition.</li>
        <li>Ki&#7875;m tra sort c&oacute; tr&aacute;nh &#273;&#432;&#7907;c b&#7857;ng index kh&ocirc;ng.</li>
      </ol>
      <table>
        <thead><tr><th>DB</th><th>Plan t&#7889;t th&#432;&#7901;ng th&#7845;y</th><th>D&#7845;u hi&#7879;u c&#7847;n nghi ng&#7901;</th></tr></thead>
        <tbody>
          <tr><td>PostgreSQL</td><td>Index Scan, Bitmap Heap Scan h&#7907;p l&yacute;</td><td>Seq Scan l&#7899;n, Sort l&#7899;n, rows estimate l&#7879;ch nhi&#7873;u</td></tr>
          <tr><td>MySQL</td><td>type const/ref/range, Using index</td><td>type ALL, Using filesort, Using temporary</td></tr>
          <tr><td>Oracle</td><td>INDEX RANGE SCAN, NESTED LOOPS nh&#7887;, HASH JOIN l&#7899;n</td><td>TABLE ACCESS FULL b&#7845;t ng&#7901;, FILTER nhi&#7873;u, cardinality sai</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ===== S3 ===== -->
<div class="module" id="s3">
  <div class="module-header">
    <div class="module-tag">S3 &middot; Join Methods</div>
    <div class="module-title">Join Algorithms: Nested Loop, Hash Join, Merge Join</div>
    <div class="module-subtitle">Join ch&#7853;m th&#432;&#7901;ng kh&ocirc;ng ph&#7843;i v&igrave; JOIN x&#7845;u, m&agrave; v&igrave; join order/method sai so v&#7899;i cardinality th&#7853;t.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">J</span>Khi n&agrave;o d&ugrave;ng join n&agrave;o?<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Join method</th><th>M&#7841;nh khi</th><th>Y&#7871;u khi</th></tr></thead>
        <tbody>
          <tr><td>Nested Loop</td><td>Outer nh&#7887;, inner c&oacute; index t&#7889;t</td><td>Outer l&#7899;n l&agrave;m probe inner qu&aacute; nhi&#7873;u l&#7847;n</td></tr>
          <tr><td>Hash Join</td><td>Join hai t&#7853;p l&#7899;n, equality join</td><td>Thi&#7871;u memory, spill temp/disk</td></tr>
          <tr><td>Merge Join</td><td>Hai input &#273;&atilde; sorted ho&#7863;c c&oacute; index order ph&ugrave; h&#7907;p</td><td>C&#7847;n sort l&#7899;n tr&#432;&#7899;c khi merge</td></tr>
        </tbody>
      </table>
      <div class="tab-group" id="tabs-join">
        <div class="tab active" onclick="switchTab('tabs-join','join-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-join','join-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-join','join-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="join-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>join-hints.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- PostgreSQL: d&ugrave;ng enable/disable &#273;&#7875; test gi&#7843; thuy&#7871;t</span>
<span class="kw">SET</span> enable_hashjoin = <span class="kw">off</span>;
<span class="kw">EXPLAIN</span> (<span class="kw2">ANALYZE</span>) <span class="kw">SELECT</span> u.country, <span class="fn">COUNT</span>(*) <span class="kw">FROM</span> users u <span class="kw">JOIN</span> orders o <span class="kw">ON</span> o.user_id = u.id <span class="kw">GROUP BY</span> u.country;
<span class="kw">SET</span> enable_hashjoin = <span class="kw">on</span>; <span class="comment">-- nh&#7899; b&#7853;t l&#7841;i!</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="join-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>join-hints.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- MySQL 8: d&ugrave;ng optimizer hints</span>
<span class="kw">SELECT</span> <span class="comment">/*+ HASH_JOIN(u, o) */</span> u.country, <span class="fn">COUNT</span>(*)
<span class="kw">FROM</span> users u <span class="kw">JOIN</span> orders o <span class="kw">ON</span> o.user_id = u.id
<span class="kw">GROUP BY</span> u.country;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="join-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>join-hints.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Oracle: d&ugrave;ng hint &#273;&#7875; ki&#7875;m ch&#7913;ng gi&#7843; thuy&#7871;t</span>
<span class="kw">SELECT</span> <span class="comment">/*+ USE_NL(o u) LEADING(u o) */</span> o.*
<span class="kw">FROM</span> users u <span class="kw">JOIN</span> orders o <span class="kw">ON</span> o.user_id = u.id
<span class="kw">WHERE</span> u.email = <span class="str">'a@example.com'</span>;

<span class="kw">SELECT</span> <span class="comment">/*+ USE_HASH(o u) */</span> u.country, <span class="fn">COUNT</span>(*)
<span class="kw">FROM</span> users u <span class="kw">JOIN</span> orders o <span class="kw">ON</span> o.user_id = u.id
<span class="kw">GROUP BY</span> u.country;</pre>
        </div></div>
      </div>
      <div class="info-box tip">&#9989; <span><strong>DBA workflow:</strong> N&#7871;u optimizer ch&#7885;n Nested Loop nh&#432;ng outer actual rows r&#7845;t l&#7899;n, h&atilde;y ki&#7875;m tra cardinality estimate, statistics v&agrave; join predicate tr&#432;&#7899;c khi th&#234;m index b&#7915;a.</span></div>
    </div>
  </div>
</div>

<!-- ===== S4 ===== -->
<div class="module" id="s4">
  <div class="module-header">
    <div class="module-tag">S4 &middot; Statistics</div>
    <div class="module-title">Statistics, Histogram &amp; Cardinality Estimation</div>
    <div class="module-subtitle">Nhi&#7873;u plan x&#7845;u b&#7855;t &#273;&#7847;u t&#7915; m&#7897;t con s&#7889; sai: optimizer ngh&#297; query tr&#7843; 10 rows nh&#432;ng th&#7921;c t&#7871; l&agrave; 10 tri&#7879;u rows.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">S</span>C&#7853;p nh&#7853;t statistics<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="tab-group" id="tabs-stats">
        <div class="tab active" onclick="switchTab('tabs-stats','stats-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-stats','stats-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-stats','stats-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="stats-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>update-statistics.sql</span></div><div class="cmd-body">
<pre><span class="kw">ANALYZE</span> orders;
<span class="kw">ANALYZE VERBOSE</span> orders;

<span class="comment">-- T&#259;ng statistics target cho c&#7897;t skewed</span>
<span class="kw">ALTER TABLE</span> orders <span class="kw">ALTER COLUMN</span> status <span class="kw">SET STATISTICS</span> <span class="num">1000</span>;
<span class="kw">ANALYZE</span> orders;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="stats-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>update-statistics.sql</span></div><div class="cmd-body">
<pre><span class="kw">ANALYZE TABLE</span> orders;

<span class="comment">-- Histogram MySQL 8</span>
<span class="kw">ANALYZE TABLE</span> orders
<span class="kw">UPDATE HISTOGRAM ON</span> status, country
<span class="kw">WITH</span> <span class="num">128</span> <span class="kw">BUCKETS</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="stats-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>update-statistics.sql</span></div><div class="cmd-body">
<pre><span class="kw">BEGIN</span>
  <span class="fn">DBMS_STATS.GATHER_TABLE_STATS</span>(
    ownname =&gt; <span class="str">'APP'</span>,
    tabname =&gt; <span class="str">'ORDERS'</span>,
    estimate_percent =&gt; <span class="fn">DBMS_STATS.AUTO_SAMPLE_SIZE</span>,
    method_opt =&gt; <span class="str">'FOR ALL COLUMNS SIZE AUTO'</span>,
    cascade =&gt; <span class="kw">TRUE</span>
  );
<span class="kw">END</span>;
/

<span class="comment">-- Ki&#7875;m tra stats hi&#7879;n t&#7841;i:</span>
<span class="kw">SELECT</span> column_name, num_distinct, num_nulls, histogram
<span class="kw">FROM</span> user_tab_col_statistics
<span class="kw">WHERE</span> table_name = <span class="str">'ORDERS'</span>;</pre>
        </div></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">H</span>Khi n&agrave;o c&#7847;n histogram?<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Histogram h&#7919;u &iacute;ch khi d&#7919; li&#7879;u l&#7879;ch m&#7841;nh. V&iacute; d&#7909; <code>status='paid'</code> chi&#7871;m 95%, c&ograve;n <code>status='fraud_review'</code> ch&#7881; 0.01%. N&#7871;u optimizer ch&#7881; bi&#7871;t s&#7889; distinct values, n&oacute; c&oacute; th&#7875; &#432;&#7899;c l&#432;&#7907;ng sai n&#7863;ng.</p>
      <table>
        <thead><tr><th>D&#7845;u hi&#7879;u</th><th>H&agrave;nh &#273;&#7897;ng</th></tr></thead>
        <tbody>
          <tr><td>Estimated rows l&#7879;ch actual rows nhi&#7873;u l&#7847;n</td><td>Update stats, th&#234;m histogram/extended stats</td></tr>
          <tr><td>D&#7919; li&#7879;u thay &#273;&#7893;i nhanh sau batch load</td><td>Gather stats sau load</td></tr>
          <tr><td>C&aacute;c c&#7897;t t&#432;&#417;ng quan m&#7841;nh</td><td>Extended statistics ho&#7863;c composite index ph&ugrave; h&#7907;p</td></tr>
          <tr><td>Plan &#273;&#7893;i sau deploy/data growth</td><td>So s&aacute;nh stats tr&#432;&#7899;c/sau, ki&#7875;m tra histogram</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ===== S5 ===== -->
<div class="module" id="s5">
  <div class="module-header">
    <div class="module-tag">S5 &middot; Plan Stability</div>
    <div class="module-title">Plan Regression, Bind Variables &amp; Hints</div>
    <div class="module-subtitle">Query h&ocirc;m qua nhanh, h&ocirc;m nay ch&#7853;m: th&#432;&#7901;ng do data distribution, statistics, bind value ho&#7863;c optimizer ch&#7885;n plan m&#7899;i.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">B</span>Bind variables v&agrave; parameter sensitivity<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>C&ugrave;ng m&#7897;t SQL nh&#432;ng gi&aacute; tr&#7883; bind kh&aacute;c nhau c&oacute; th&#7875; c&#7847;n plan kh&aacute;c nhau. V&iacute; d&#7909; <code>status='paid'</code> match g&#7847;n h&#7871;t b&#7843;ng, c&ograve;n <code>status='fraud_review'</code> match r&#7845;t &iacute;t.</p>
      <div class="tab-group" id="tabs-bind">
        <div class="tab active" onclick="switchTab('tabs-bind','bind-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-bind','bind-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-bind','bind-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="bind-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>bind-sensitive.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- PostgreSQL: generic plan vs custom plan (PREPARE)</span>
<span class="kw">PREPARE</span> q(text) <span class="kw">AS SELECT</span> * <span class="kw">FROM</span> orders <span class="kw">WHERE</span> status = $<span class="num">1</span>;
<span class="kw">EXECUTE</span> q(<span class="str">'paid'</span>);

<span class="comment">-- Ki&#7875;m tra generic plan:</span>
<span class="kw">EXPLAIN EXECUTE</span> q(<span class="str">'paid'</span>);
<span class="comment">-- pg_stat_statements &#273;&#7875; theo d&otilde;i:</span>
<span class="kw">SELECT</span> query, calls, mean_exec_time <span class="kw">FROM</span> pg_stat_statements <span class="kw">WHERE</span> query <span class="kw">LIKE</span> <span class="str">'%orders%'</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="bind-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>bind-sensitive.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- MySQL: prepared statements &amp; performance_schema</span>
<span class="kw">PREPARE</span> q <span class="kw">FROM</span> <span class="str">'SELECT * FROM orders WHERE status = ?'</span>;
<span class="kw">SET</span> @s = <span class="str">'paid'</span>;
<span class="kw">EXECUTE</span> q <span class="kw">USING</span> @s;

<span class="kw">SELECT</span> * <span class="kw">FROM</span> performance_schema.events_statements_history
<span class="kw">WHERE</span> sql_text <span class="kw">LIKE</span> <span class="str">'%orders%'</span> <span class="kw">LIMIT</span> <span class="num">5</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="bind-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>bind-sensitive.sql</span></div><div class="cmd-body">
<pre><span class="kw">SELECT</span> * <span class="kw">FROM</span> orders <span class="kw">WHERE</span> status = :status;

<span class="comment">-- Xem bind &#273;&#432;&#7907;c peek v&agrave; actual plan:</span>
<span class="kw">SELECT</span> * <span class="kw">FROM TABLE</span>(
  <span class="fn">DBMS_XPLAN.DISPLAY_CURSOR</span>(
    sql_id =&gt; <span class="kw">NULL</span>,
    cursor_child_no =&gt; <span class="kw">NULL</span>,
    format =&gt; <span class="str">'ALLSTATS LAST +PEEKED_BINDS +OUTLINE'</span>
  )
);</pre>
        </div></div>
      </div>
      <div class="info-box warn">&#9888;&#65039; <span><strong>Hint l&agrave; dao s&#7855;c:</strong> D&ugrave;ng hint &#273;&#7875; test gi&#7843; thuy&#7871;t ho&#7863;c &#7893;n &#273;&#7883;nh plan khi c&#7847;n, nh&#432;ng &#432;u ti&#234;n s&#7917;a statistics, index, query shape tr&#432;&#7899;c.</span></div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">H</span>Hint &#273;&#250;ng c&aacute;ch<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="tab-group" id="tabs-hints">
        <div class="tab active" onclick="switchTab('tabs-hints','hints-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-hints','hints-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-hints','hints-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="hints-pg">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>hints.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- PostgreSQL kh&ocirc;ng c&oacute; hint tr&#7921;c ti&#7871;p, d&ugrave;ng GUC &#273;&#7875; test:</span>
<span class="kw">SET</span> enable_seqscan = <span class="kw">off</span>;
<span class="kw">EXPLAIN ANALYZE SELECT</span> * <span class="kw">FROM</span> orders <span class="kw">WHERE</span> user_id = :user_id;
<span class="kw">SET</span> enable_seqscan = <span class="kw">on</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="hints-my">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>hints.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- MySQL: force index hint</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> orders <span class="kw">FORCE INDEX</span> (idx_orders_user_created)
<span class="kw">WHERE</span> user_id = <span class="num">42</span>
<span class="kw">ORDER BY</span> created_at <span class="kw">DESC</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="hints-ora">
        <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>hints.sql</span></div><div class="cmd-body">
<pre><span class="kw">SELECT</span> <span class="comment">/*+ INDEX(o idx_orders_user_created) */</span> *
<span class="kw">FROM</span> orders o
<span class="kw">WHERE</span> o.user_id = :user_id
<span class="kw">ORDER BY</span> o.created_at <span class="kw">DESC</span>;

<span class="comment">-- Thu th&#7853;p actual plan statistics:</span>
<span class="kw">SELECT</span> <span class="comment">/*+ GATHER_PLAN_STATISTICS */</span> * <span class="kw">FROM</span> orders o <span class="kw">WHERE</span> o.status = :status;
<span class="kw">SELECT</span> * <span class="kw">FROM TABLE</span>(<span class="fn">DBMS_XPLAN.DISPLAY_CURSOR</span>(format =&gt; <span class="str">'ALLSTATS LAST'</span>));</pre>
        </div></div>
      </div>
    </div>
  </div>
</div>

<!-- ===== S6: Oracle Advanced ===== -->
<div class="module" id="s6">
  <div class="module-header">
    <div class="module-tag">S6 &middot; Oracle Advanced</div>
    <div class="module-title">Oracle N&#226;ng cao: Skip Scan, SPM, Parallel &amp; Adaptive</div>
    <div class="module-subtitle">C&aacute;c t&iacute;nh n&#259;ng &#273;&#7863;c th&ugrave; c&#7911;a Oracle kh&ocirc;ng c&oacute; tr&#234;n PostgreSQL hay MySQL. B&#7855;t bu&#7897;c ph&#7843;i bi&#7871;t cho l&#7897; tr&igrave;nh DBA Oracle.</div>
  </div>

  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">1</span>Index Skip Scan<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>B&igrave;nh th&#432;&#7901;ng m&#7897;t composite index <code>(a, b)</code> ch&#7881; h&#7919;u &iacute;ch khi predicate ch&#7913;a c&#7897;t <strong>&#273;&#7847;u ti&#234;n</strong> (<code>a</code>). Oracle c&oacute; th&#7875; <strong>b&#7887; qua c&#7897;t &#273;&#7847;u</strong> b&#7857;ng c&#417; ch&#7871; Skip Scan n&#7871;u c&#7897;t &#273;&#7847;u c&oacute; &iacute;t gi&aacute; tr&#7883; distinct (low cardinality).</p>
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>index-skip-scan.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Gi&#7843; s&#7917;: index composite(gender, age) — gender ch&#7881; c&oacute; M/F</span>
<span class="kw">CREATE INDEX</span> idx_users_gender_age <span class="kw">ON</span> users(gender, age);

<span class="comment">-- Query ch&#7881; filter theo age (kh&ocirc;ng c&oacute; gender)</span>
<span class="kw">EXPLAIN PLAN FOR</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> users <span class="kw">WHERE</span> age = <span class="num">30</span>;

<span class="kw">SELECT</span> * <span class="kw">FROM TABLE</span>(<span class="fn">DBMS_XPLAN.DISPLAY</span>(format =&gt; <span class="str">'BASIC +PREDICATE'</span>));
<span class="comment">-- Plan c&oacute; th&#7875; th&#7845;y: INDEX SKIP SCAN | idx_users_gender_age</span>
<span class="comment">-- Oracle scan theo t&#7915;ng gi&aacute; tr&#7883; gender (M, F) r&#7891;i t&igrave;m age=30 b&#234;n trong</span>

<span class="comment">-- Xem c&#7897;t n&agrave;o th&iacute;ch h&#7907;p cho skip scan:</span>
<span class="kw">SELECT</span> column_name, num_distinct
<span class="kw">FROM</span> user_tab_col_statistics
<span class="kw">WHERE</span> table_name = <span class="str">'USERS'</span>
<span class="kw">ORDER BY</span> num_distinct;</pre>
      </div></div>
      <div class="info-box note">&#128204; <span><strong>Khi n&agrave;o Skip Scan hi&#7879;u qu&#7843;:</strong> C&#7897;t &#273;&#7847;u trong composite index c&oacute; &iacute;t gi&aacute; tr&#7883; distinct (&lt;50). N&#7871;u c&oacute; r&#7845;t nhi&#7873;u gi&aacute; tr&#7883; distinct, Oracle s&#7869; &#432;u ti&#234;n Full Table Scan thay v&igrave; Skip Scan.</span></div>
      <div class="info-box warn">&#9888;&#65039; <span>PostgreSQL v&agrave; MySQL <strong>kh&ocirc;ng c&oacute;</strong> Index Skip Scan. PostgreSQL 14+ c&oacute; <em>Skip Scan</em> cho B-Tree nh&#432;ng ch&#7881; &#7903; m&#7913;c h&#7841;n ch&#7871;.</span></div>
    </div>
  </div>

  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">2</span>SQL Plan Management (SPM)<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>SPM l&agrave; c&#417; ch&#7871; Oracle <strong>freeze/lock m&#7897;t execution plan t&#7889;t</strong> v&agrave;o SQL Plan Baseline, ng&#259;n optimizer t&#7921; &yacute; &#273;&#7893;i plan khi statistics thay &#273;&#7893;i. &#272;&acirc;y l&agrave; gi&#7843;i ph&aacute;p production-grade &#7893;n &#273;&#7883;nh plan.</p>
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>sql-plan-management.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- B1: B&#7853;t Automatic Plan Capture (Oracle ch&#7921; &#273;&#7897;ng ghi l&#7841;i plan)</span>
<span class="kw">ALTER SYSTEM SET</span> optimizer_capture_sql_plan_baselines = <span class="kw">TRUE</span>;

<span class="comment">-- B2: Ch&#7845;p nh&#7853;n m&#7897;t plan t&#7889;t v&agrave;o baseline th&#7911; c&ocirc;ng</span>
<span class="kw">DECLARE</span>
  l_count <span class="fn">NUMBER</span>;
<span class="kw">BEGIN</span>
  l_count := <span class="fn">DBMS_SPM.LOAD_PLANS_FROM_CURSOR_CACHE</span>(
    sql_id =&gt; <span class="str">'abc123xyz'</span>  <span class="comment">-- t&#236;m sql_id trong v$sql</span>
  );
  <span class="fn">DBMS_OUTPUT.PUT_LINE</span>(<span class="str">'Plans loaded: '</span> || l_count);
<span class="kw">END</span>;
/

<span class="comment">-- B3: Xem c&aacute;c plan &#273;&atilde; c&oacute; trong baseline</span>
<span class="kw">SELECT</span> sql_handle, plan_name, enabled, accepted, fixed
<span class="kw">FROM</span> dba_sql_plan_baselines
<span class="kw">WHERE</span> sql_text <span class="kw">LIKE</span> <span class="str">'%orders%'</span>;

<span class="comment">-- B4: Fixed plan — kh&oacute;a c&#7913;ng, kh&ocirc;ng cho optimizer t&#7921; &#273;&#7893;i</span>
<span class="kw">DECLARE</span>
  l_count <span class="fn">NUMBER</span>;
<span class="kw">BEGIN</span>
  l_count := <span class="fn">DBMS_SPM.ALTER_SQL_PLAN_BASELINE</span>(
    sql_handle  =&gt; <span class="str">'SQL_abc...'</span>,
    plan_name   =&gt; <span class="str">'SQL_PLAN_abc...'</span>,
    attribute_name  =&gt; <span class="str">'fixed'</span>,
    attribute_value =&gt; <span class="str">'YES'</span>
  );
<span class="kw">END</span>;
/

<span class="comment">-- B5: Evolve plan (th&#7917; plan m&#7899;i, n&#7871;u t&#7889;t h&#417;n th&igrave; ch&#7845;p nh&#7853;n)</span>
<span class="kw">SELECT</span> <span class="fn">DBMS_SPM.EVOLVE_SQL_PLAN_BASELINE</span>(
  sql_handle =&gt; <span class="str">'SQL_abc...'</span>
) <span class="kw">FROM</span> dual;</pre>
      </div></div>
      <table>
        <thead><tr><th>Thu&#7897;c t&iacute;nh</th><th>Enabled</th><th>Accepted</th><th>Fixed</th></tr></thead>
        <tbody>
          <tr><td>&#221; ngh&#297;a</td><td>Baseline &#273;ang ho&#7841;t &#273;&#7897;ng</td><td>Oracle ch&#7845;p nh&#7853;n d&ugrave;ng plan n&agrave;y</td><td>Kh&oacute;a c&#7913;ng, kh&ocirc;ng evolve</td></tr>
          <tr><td>Gi&aacute; tr&#7883;</td><td>YES/NO</td><td>YES/NO</td><td>YES/NO</td></tr>
        </tbody>
      </table>
      <div class="info-box tip">&#9989; <span><strong>Workflow th&#7921;c t&#7871;:</strong> Khi ph&aacute;t hi&#7879;n plan t&#7889;t trong UAT, load v&agrave;o baseline → set accepted=YES → deploy l&#234;n production. N&#7871;u plan x&#7845;u xu&#7845;t hi&#7879;n, fixed baseline s&#7869; ng&#259;n Oracle d&ugrave;ng n&oacute;.</span></div>
    </div>
  </div>

  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">3</span>Parallel Query (DOP)<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Oracle c&oacute; th&#7875; ph&acirc;n t&aacute;n m&#7897;t query ra nhi&#7873;u ti&#7871;n tr&igrave;nh song song (parallel slaves) &#273;&#7875; x&#7917; l&yacute; OLAP/analytics tr&#234;n d&#7919; li&#7879;u l&#7899;n. DOP (Degree of Parallelism) l&agrave; s&#7889; worker process.</p>
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>parallel-query.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- C&aacute;ch 1: Hint tr&#7921;c ti&#7871;p trong query</span>
<span class="kw">SELECT</span> <span class="comment">/*+ PARALLEL(orders, 4) */</span>
  <span class="fn">COUNT</span>(*), <span class="fn">SUM</span>(amount)
<span class="kw">FROM</span> orders
<span class="kw">WHERE</span> created_at &gt;= DATE <span class="str">'2026-01-01'</span>;

<span class="comment">-- C&aacute;ch 2: Set DOP tr&#234;n b&#7843;ng (c&#7849;n th&#7853;n trong production)</span>
<span class="kw">ALTER TABLE</span> orders <span class="kw">PARALLEL</span> <span class="num">4</span>;
<span class="kw">ALTER TABLE</span> orders <span class="kw">NOPARALLEL</span>;  <span class="comment">-- t&#7855;t sau khi xong</span>

<span class="comment">-- Theo d&otilde;i parallel session &#273;ang ch&#7841;y:</span>
<span class="kw">SELECT</span> qcsid, server#, degree, req_degree, status
<span class="kw">FROM</span> v$px_session
<span class="kw">WHERE</span> qcsid IS <span class="kw">NOT NULL</span>;

<span class="comment">-- Ki&#7875;m tra xem query c&oacute; ch&#7841;y parallel kh&ocirc;ng:</span>
<span class="kw">SELECT</span> * <span class="kw">FROM TABLE</span>(<span class="fn">DBMS_XPLAN.DISPLAY_CURSOR</span>(format =&gt; <span class="str">'ALLSTATS LAST +PARALLEL'</span>));</pre>
      </div></div>
      <table>
        <thead><tr><th>&#272;i&#7873;u ki&#7879;n</th><th>Khuy&#7871;n ngh&#7883;</th></tr></thead>
        <tbody>
          <tr><td>OLAP/analytics, b&#7843;ng l&#7899;n &gt; 1GB</td><td>Th&#432; Parallel DOP 4&ndash;8, monitor CPU</td></tr>
          <tr><td>OLTP, query nh&#7887; &lt; 10ms</td><td>NOPARALLEL &mdash; overhead kh&#7903;i t&#7841;o slaves cao h&#417;n l&#7907;i</td></tr>
          <tr><td>Production peak hours</td><td>D&ugrave;ng Resource Manager gi&#7899;i h&#7841;n DOP</td></tr>
        </tbody>
      </table>
      <div class="info-box warn">&#9888;&#65039; <span><strong>Trade-off:</strong> Parallel query d&ugrave;ng nhi&#7873;u CPU. Trong h&#7879; th&#7889;ng OLTP, m&#7897;t query parallel sai c&oacute; th&#7875; &oacute;ng to&agrave;n b&#7897; CPU c&#7911;a server.</span></div>
    </div>
  </div>

  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">4</span>Adaptive Query Optimization (Oracle 12c+)<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p>Oracle 12c+ c&oacute; kh&#7843; n&#259;ng <strong>t&#7921; ch&#7881;nh plan trong l&uacute;c ch&#7841;y</strong> (runtime) khi ph&aacute;t hi&#7879;n cardinality estimate sai v&#432;&#7907;t ng&#432;&#7905;ng. G&#7891;m 2 th&agrave;nh ph&#7847;n ch&iacute;nh: <strong>Adaptive Plans</strong> v&agrave; <strong>Adaptive Statistics</strong>.</p>
      <div class="cmd-block"><div class="cmd-header"><span>&#9679; &#9679; &#9679;</span><span>adaptive-optimization.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Ki&#7875;m tra adaptive optimization c&oacute; &#273;ang b&#7853;t:</span>
<span class="kw">SELECT</span> name, value
<span class="kw">FROM</span> v$parameter
<span class="kw">WHERE</span> name <span class="kw">IN</span> (
  <span class="str">'optimizer_adaptive_plans'</span>,
  <span class="str">'optimizer_adaptive_statistics'</span>
);

<span class="comment">-- Xem query c&oacute; d&ugrave;ng adaptive plan kh&ocirc;ng (Note: "adaptive" trong plan):</span>
<span class="kw">SELECT</span> * <span class="kw">FROM TABLE</span>(<span class="fn">DBMS_XPLAN.DISPLAY_CURSOR</span>(format =&gt; <span class="str">'ALLSTATS LAST +ADAPTIVE'</span>));
<span class="comment">-- N&#7871;u th&#7845;y d&#7845;u "-" tr&#432;&#7899;c 1 operation, &#273;&oacute; l&agrave; sub-plan b&#7883; lo&#7841;i b&#7887; l&uacute;c runtime</span>

<span class="comment">-- T&#7855;t adaptive plans n&#7871;u g&acirc;y ra plan b&#7845;t &#7893;n &#273;&#7883;nh:</span>
<span class="kw">ALTER SESSION SET</span> optimizer_adaptive_plans = <span class="kw">FALSE</span>;
<span class="comment">-- ho&#7863;c t&#7855;t to&agrave;n c&#7909;c:</span>
<span class="kw">ALTER SYSTEM SET</span> optimizer_adaptive_plans = <span class="kw">FALSE</span>;</pre>
      </div></div>
      <table>
        <thead><tr><th>T&iacute;nh n&#259;ng</th><th>M&ocirc; t&#7843;</th><th>Note</th></tr></thead>
        <tbody>
          <tr><td>Adaptive Plans</td><td>&#272;&#7893;i join method (NL&#8596;HJ) l&uacute;c runtime n&#7871;u rows sai</td><td>Oracle 12c+, m&#7863;c &#273;&#7883;nh ON</td></tr>
          <tr><td>Adaptive Statistics</td><td>Dynamic sampling nhi&#7873;u h&#417;n khi stats thi&#7871;u</td><td>C&oacute; th&#7875; g&acirc;y overhead khi parse</td></tr>
          <tr><td>SQL Plan Directives</td><td>L&#432;u ghi ch&uacute; c&#7843;nh b&aacute;o cardinality sai cho l&#7847;n sau</td><td>T&#7921; &#273;&#7897;ng, l&#432;u trong SYSAUX</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ===== S7 ===== -->
<div class="module" id="s7">
  <div class="module-header">
    <div class="module-tag">S7 &middot; Error Catalog</div>
    <div class="module-title">L&#7895;i th&#432;&#7901;ng g&#7863;p &amp; C&aacute;ch fix</div>
    <div class="module-subtitle">Catalog n&agrave;y gi&uacute;p b&#7841;n debug query ch&#7853;m theo tri&#7879;u ch&#7913;ng thay v&igrave; &#273;o&aacute;n m&ograve;.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-summary">E</span>Error catalog &mdash; Optimizer &amp; Plan<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <table>
        <thead><tr><th>Tri&#7879;u ch&#7913;ng</th><th>Root cause</th><th>Fix</th></tr></thead>
        <tbody>
          <tr><td>Estimated rows l&#7879;ch actual rows 100x</td><td>Statistics/histogram thi&#7871;u ho&#7863;c c&#361;</td><td>ANALYZE/GATHER_TABLE_STATS, t&#259;ng stats target</td></tr>
          <tr><td>Nested Loop ch&#7841;y c&#7921;c l&acirc;u</td><td>Outer actual rows l&#7899;n h&#417;n estimate</td><td>S&#7917;a stats, xem hash join, index inner side</td></tr>
          <tr><td>Sort l&#7899;n ho&#7863;c temp spill</td><td>ORDER BY/GROUP BY kh&ocirc;ng kh&#7899;p index ho&#7863;c thi&#7871;u memory</td><td>Index theo order/group, tune memory/workarea</td></tr>
          <tr><td>Plan &#273;&#7893;i sau batch load</td><td>Data distribution &#273;&#7893;i, stats ch&#432;a c&#7853;p nh&#7853;t</td><td>Gather stats sau load, ki&#7875;m tra histogram</td></tr>
          <tr><td>Index c&oacute; nh&#432;ng kh&ocirc;ng &#273;&#432;&#7907;c d&ugrave;ng</td><td>Full scan r&#7867; h&#417;n, predicate kh&ocirc;ng sargable, stats sai</td><td>Rewrite predicate, update stats, ki&#7875;m ch&#7913;ng b&#7857;ng hint</td></tr>
          <tr><td>Oracle EXPLAIN PLAN kh&aacute;c runtime</td><td>EXPLAIN l&agrave; plan d&#7921; ki&#7871;n, bind/runtime kh&aacute;c</td><td>D&ugrave;ng DBMS_XPLAN.DISPLAY_CURSOR v&#7899;i ALLSTATS LAST</td></tr>
          <tr><td>Oracle plan thay &#273;&#7893;i sau stats gather</td><td>Optimizer ch&#7885;n plan m&#7899;i ch&#432;a ki&#7875;m ch&#7913;ng</td><td>D&ugrave;ng SPM (DBMS_SPM) &#273;&#7875; lock plan t&#7889;t</td></tr>
          <tr><td>Skip Scan xu&#7845;t hi&#7879;n khi kh&ocirc;ng mong mu&#7889;n</td><td>Oracle ch&#7885;n skip scan v&igrave; c&#7897;t &#273;&#7847;u c&oacute; &iacute;t distinct</td><td>Ki&#7875;m tra statistics, th&#234;m index ph&ugrave; h&#7907;p ho&#7863;c dung hint NO_INDEX_SS</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-practice">P</span>Debug checklist khi query ch&#7853;m<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <ol>
        <li>L&#7845;y actual plan, kh&ocirc;ng ch&#7881; estimated plan.</li>
        <li>T&igrave;m node t&#7889;n th&#7901;i gian/row nhi&#7873;u nh&#7845;t.</li>
        <li>So estimated rows v&#7899;i actual rows.</li>
        <li>Ki&#7875;m tra access predicate vs filter predicate.</li>
        <li>C&#7853;p nh&#7853;t statistics n&#7871;u estimate sai.</li>
        <li>Test index/query rewrite/hint &#273;&#7875; x&aacute;c nh&#7853;n gi&#7843; thuy&#7871;t.</li>
        <li>(Oracle) N&#7871;u plan kh&ocirc;ng &#7893;n &#273;&#7883;nh: d&ugrave;ng SPM/baseline &#273;&#7875; lock plan t&#7889;t.</li>
      </ol>
    </div>
  </div>
</div>

<!-- ===== S8 ===== -->
<div class="module" id="s8">
  <div class="module-header">
    <div class="module-tag">S8 &middot; Interview Prep</div>
    <div class="module-title">Interview Prep &mdash; Optimizer &amp; Execution Plan</div>
    <div class="module-subtitle">C&aacute;c c&acirc;u h&#7887;i n&agrave;y ki&#7875;m tra b&#7841;n c&oacute; &#273;&#7885;c &#273;&#432;&#7907;c "&#253; &#273;&#7883;nh c&#7911;a database" hay ch&#7881; bi&#7871;t t&#7841;o index.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-quiz">Q</span>Quick quiz<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="quiz-item">
        <div class="quiz-q">Estimated rows l&#7879;ch actual rows r&#7845;t nhi&#7873;u th&#432;&#7901;ng ch&#7881; ra &#273;i&#7873;u g&igrave;?</div>
        <div class="quiz-options">
          <div class="quiz-opt" onclick="answerQuiz(this,false,'Kh&ocirc;ng h&#7859;n. Index c&oacute; th&#7875; &#273;&uacute;ng nh&#432;ng estimate sai v&#7851;n l&agrave;m join order sai.')">A. Ch&#7855;c ch&#7855;n thi&#7871;u index</div>
          <div class="quiz-opt" onclick="answerQuiz(this,true,'&#272;&uacute;ng. &#272;&acirc;y l&agrave; d&#7845;u hi&#7879;u statistics/histogram/correlation kh&ocirc;ng ph&#7843;n &aacute;nh d&#7919; li&#7879;u th&#7853;t.')">B. Statistics ho&#7863;c cardinality estimate c&oacute; v&#7845;n &#273;&#7873;</div>
          <div class="quiz-opt" onclick="answerQuiz(this,false,'Cache &#7843;nh h&#432;&#7903;ng th&#7901;i gian, nh&#432;ng kh&ocirc;ng gi&#7843;i th&iacute;ch estimated rows sai.')">C. Cache database b&#7883; l&#7841;nh</div>
        </div>
        <div class="quiz-explain"></div>
      </div>
      <div class="quiz-item">
        <div class="quiz-q">Oracle n&#234;n d&ugrave;ng g&igrave; &#273;&#7875; xem actual execution plan sau khi query ch&#7841;y?</div>
        <div class="quiz-options">
          <div class="quiz-opt" onclick="answerQuiz(this,false,'EXPLAIN PLAN ch&#7881; l&agrave; plan d&#7921; ki&#7871;n.')">A. Ch&#7881; EXPLAIN PLAN</div>
          <div class="quiz-opt" onclick="answerQuiz(this,true,'&#272;&uacute;ng. DISPLAY_CURSOR v&#7899;i ALLSTATS LAST cho actual rows/time c&#7911;a cursor &#273;&atilde; ch&#7841;y.')">B. DBMS_XPLAN.DISPLAY_CURSOR v&#7899;i ALLSTATS LAST</div>
          <div class="quiz-opt" onclick="answerQuiz(this,false,'DESC ch&#7881; xem c&#7845;u tr&uacute;c b&#7843;ng.')">C. DESC table</div>
        </div>
        <div class="quiz-explain"></div>
      </div>
      <div class="quiz-item">
        <div class="quiz-q">Oracle Index Skip Scan ho&#7841;t &#273;&#7897;ng hi&#7879;u qu&#7843; nh&#7845;t khi n&agrave;o?</div>
        <div class="quiz-options">
          <div class="quiz-opt" onclick="answerQuiz(this,false,'Sai. C&agrave;ng nhi&#7873;u distinct value, chi ph&iacute; skip c&agrave;ng cao.')">A. C&#7897;t &#273;&#7847;u c&oacute; nhi&#7873;u gi&aacute; tr&#7883; distinct</div>
          <div class="quiz-opt" onclick="answerQuiz(this,true,'&#272;&uacute;ng. &Iacute;t distinct = &iacute;t sub-range c&#7847;n scan, Skip Scan hi&#7879;u qu&#7843;.')">B. C&#7897;t &#273;&#7847;u c&oacute; &iacute;t gi&aacute; tr&#7883; distinct (&lt;50)</div>
          <div class="quiz-opt" onclick="answerQuiz(this,false,'Kh&ocirc;ng ph&#7843;i. Skip Scan li&#234;n quan &#273;&#7871;n c&#7845;u tr&uacute;c index, kh&ocirc;ng ph&#7843;i table size.')">C. Table c&oacute; &iacute;t h&#417;n 1000 rows</div>
        </div>
        <div class="quiz-explain"></div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-detail">S</span>Senior answer templates<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <h3 class="blue">Q1: Query ch&#7853;m d&ugrave; c&oacute; index, b&#7841;n debug th&#7871; n&agrave;o?</h3>
      <p>T&ocirc;i l&#7845;y actual plan tr&#432;&#7899;c. Sau &#273;&oacute; t&igrave;m node t&#7889;n nh&#7845;t, so estimated rows v&#7899;i actual rows, ki&#7875;m tra index access hay filter, sort/temp, join order v&agrave; join method. N&#7871;u estimate sai, t&ocirc;i x&#7917; l&yacute; statistics/histogram. N&#7871;u predicate kh&ocirc;ng sargable, t&ocirc;i rewrite query ho&#7863;c d&ugrave;ng functional index. Hint ch&#7881; d&ugrave;ng &#273;&#7875; ki&#7875;m ch&#7913;ng ho&#7863;c &#7893;n &#273;&#7883;nh plan khi &#273;&atilde; hi&#7875;u root cause.</p>
      <h3 class="green">Q2: Khi n&agrave;o Nested Loop t&#7889;t h&#417;n Hash Join?</h3>
      <p>Nested Loop t&#7889;t khi outer input nh&#7887; v&agrave; inner side c&oacute; index selective. Hash Join t&#7889;t h&#417;n khi join hai t&#7853;p l&#7899;n b&#7857;ng equality v&agrave; &#273;&#7911; memory &#273;&#7875; build hash table. N&#7871;u optimizer ch&#7885;n Nested Loop cho outer l&#7899;n, t&ocirc;i nghi ng&#7901; cardinality estimate sai ho&#7863;c thi&#7871;u stats.</p>
      <h3 class="orange">Q3: SPM v&agrave; hint kh&aacute;c nhau nh&#432; th&#7871; n&agrave;o?</h3>
      <p>Hint n&#7857;m trong SQL text, n&#7871;u SQL thay &#273;&#7893;i th&igrave; m&#7845;t. SPM l&#432;u plan baseline ri&#234;ng bi&#7879;t, ho&#7841;t &#273;&#7897;ng &#7903; l&#7899;p optimizer, d&ugrave; SQL text c&oacute; &#273;&#7893;i th&igrave; plan v&#7851;n &#7893;n &#273;&#7883;nh. SPM l&agrave; gi&#7843;i ph&aacute;p s&#7843;n xu&#7845;t, hint ch&#7881; l&agrave; gi&#7843;i ph&aacute;p ng&#7855;n h&#7841;n.</p>
    </div>
  </div>
</div>

<!-- ===== S9 ===== -->
<div class="module" id="s9">
  <div class="module-header">
    <div class="module-tag">S9 &middot; Summary</div>
    <div class="module-title">Checklist &amp; T&#7893;ng k&#7871;t Module 04</div>
    <div class="module-subtitle">Ho&agrave;n th&agrave;nh checklist n&agrave;y tr&#432;&#7899;c khi chuy&#7875;n sang module Locks &amp; Concurrency.</div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-summary">S</span>Summary &mdash; &#272;i&#7875;m ch&#7889;t c&#7847;n nh&#7899;<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <div class="summary-grid">
        <div class="summary-item"><strong>Plan l&agrave; &#273;&#432;&#7901;ng ch&#7841;y</strong>SQL n&oacute;i k&#7871;t qu&#7843;, plan n&oacute;i c&aacute;ch l&#7845;y k&#7871;t qu&#7843;.</div>
        <div class="summary-item"><strong>Estimate sai k&eacute;o plan sai</strong>Rows estimate l&agrave; t&iacute;n hi&#7879;u debug s&#7889; m&#7897;t.</div>
        <div class="summary-item"><strong>Actual plan quan tr&#7885;ng</strong>Oracle c&#7847;n DISPLAY_CURSOR, PostgreSQL/MySQL d&ugrave;ng EXPLAIN ANALYZE.</div>
        <div class="summary-item"><strong>Join method c&oacute; ng&#7919; c&#7843;nh</strong>Nested Loop kh&ocirc;ng x&#7845;u, Hash Join kh&ocirc;ng lu&ocirc;n t&#7889;t.</div>
        <div class="summary-item"><strong>Stats l&agrave; nhi&#234;n li&#7879;u optimizer</strong>Stats c&#361; ho&#7863;c thi&#7871;u histogram l&agrave;m optimizer m&ugrave;.</div>
        <div class="summary-item"><strong>SPM &gt; Hint</strong>Lock plan b&#7857;ng baseline, kh&ocirc;ng n&#234;n l&#7879; thu&#7897;c hint trong production.</div>
        <div class="summary-item"><strong>Index Skip Scan</strong>Oracle-only, hi&#7879;u qu&#7843; khi c&#7897;t &#273;&#7847;u index c&oacute; &iacute;t distinct value.</div>
        <div class="summary-item"><strong>Parallel Query = &#273;ao 2 l&#432;&#7905;i</strong>T&#259;ng t&#7889;c OLAP nh&#432;ng &#7843;nh h&#432;&#7903;ng CPU OLTP n&#7871;u d&ugrave;ng sai.</div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)"><span class="section-icon icon-practice">D</span>Definition of Done<span class="section-toggle">&#9660;</span></div>
    <div class="section-content">
      <p class="progress-text" id="checklist-progress-text">0/9 m&#7909;c ho&agrave;n th&agrave;nh (0%)</p>
      <div class="progress-bar"><div class="progress-fill" id="checklist-progress-fill"></div></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Gi&#7843;i th&iacute;ch &#273;&#432;&#7907;c cost, cardinality, selectivity, statistics.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Bi&#7871;t predicate pushdown l&agrave; g&igrave; v&agrave; nh&#7853;n bi&#7871;t trên execution plan.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>&#272;&#7885;c &#273;&#432;&#7907;c EXPLAIN/EXPLAIN ANALYZE tr&#234;n PostgreSQL v&agrave; MySQL.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>D&ugrave;ng &#273;&#432;&#7907;c Oracle <code>EXPLAIN PLAN</code>, <code>DBMS_XPLAN.DISPLAY</code>, <code>DISPLAY_CURSOR</code>.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Ph&acirc;n bi&#7879;t Nested Loop, Hash Join, Merge Join v&agrave; t&igrave;nh hu&#7889;ng ph&ugrave; h&#7907;p.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Bi&#7871;t c&#7853;p nh&#7853;t statistics/histogram b&#7857;ng PostgreSQL, MySQL, Oracle.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Hi&#7875;u c&#417; ch&#7871; Oracle Index Skip Scan v&agrave; &#273;i&#7873;u ki&#7879;n &#225;p d&#7909;ng.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Bi&#7871;t d&ugrave;ng DBMS_SPM &#273;&#7875; load v&agrave; fix plan baseline tr&#234;n Oracle.</span></div>
      <div class="checklist-row"><div class="check-box" onclick="toggleCheck(this)"></div><span>Bi&#7871;t d&ugrave;ng hint &#273;&#7875; ki&#7875;m ch&#7913;ng gi&#7843; thuy&#7871;t, kh&ocirc;ng l&#7841;m d&#7909;ng.</span></div>
    </div>
  </div>
</div>

  </main>
</div>

<script>
const navItems = document.querySelectorAll('.nav-item');
let currentModule = 0;
const totalModules = 10;

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
  toggle.textContent = isHidden ? '&#9660;' : '&#9654;';
}

function answerQuiz(el, isCorrect, msg) {
  const item = el.closest('.quiz-item');
  const opts = item.querySelectorAll('.quiz-opt');
  const explain = item.querySelector('.quiz-explain');
  opts.forEach(opt => (opt.style.pointerEvents = 'none'));
  el.classList.add(isCorrect ? 'correct' : 'wrong');
  if (!isCorrect) { opts.forEach(opt => { const o = opt.getAttribute('onclick'); if (o && o.includes('true')) opt.classList.add('correct'); }); }
  explain.textContent = (isCorrect ? '&#10003; Ch&iacute;nh x&aacute;c! ' : '&#10007; Sai. ') + msg;
  explain.classList.add('show');
}

function toggleSolution(btn) {
  const box = btn.nextElementSibling;
  const show = box.classList.toggle('show');
  btn.textContent = show ? '&#128316; &Acirc;̉n l&#7901;i gi&#7843;i' : '&#128161; Xem l&#7901;i gi&#7843;i';
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
  if (text) text.textContent = `${checked}/${total} m&#7909;c ho&agrave;n th&agrave;nh (${pct}%)`;
}

showModule(0, navItems[0]);
updateProgress();
</script>
</body>
</html>'''

with open('D:/DE/Tuning_SQL/Module04_Optimizer_Execution_Plan_new.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done! Saved to Module04_Optimizer_Execution_Plan_new.html')
