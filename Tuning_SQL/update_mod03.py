import re
import os

with open('D:/DE/Tuning_SQL/Module01_SQL_Tuning_Index.html', 'r', encoding='utf-8') as f:
    mod1 = f.read()

with open('D:/DE/Tuning_SQL/Module03_Schema_Physical_Design.html', 'r', encoding='utf-8') as f:
    mod2 = f.read()

style1 = re.search(r'(<style>.*?</style>)', mod1, re.DOTALL).group(1)
script1 = re.search(r'(<script>.*?</script>)', mod1, re.DOTALL).group(1)

# Replace style and script
mod2 = re.sub(r'<style>.*?</style>', style1, mod2, flags=re.DOTALL)
mod2 = re.sub(r'<script>.*?</script>', script1, mod2, flags=re.DOTALL)

# Remove nav-buttons
mod2 = re.sub(r'<div class="nav-buttons">.*?</div>', '', mod2, flags=re.DOTALL)

# Update Roadmap table in S0 (add S7 and shift S7, S8, S9)
mod2 = mod2.replace('Roadmap 10 sections', 'Roadmap 11 sections')
mod2 = mod2.replace('<tr><td>S7</td><td>Practice & Error Catalog</td><td>Bài tập thiết kế schema và lỗi thường gặp</td></tr>',
                    '<tr><td>S7</td><td>Các Index Đặc Thù Khác</td><td>Spatial, Trigram, Prefix Index</td></tr>\n          <tr><td>S8</td><td>Practice & Error Catalog</td><td>Bài tập thiết kế schema và lỗi thường gặp</td></tr>')
mod2 = mod2.replace('<tr><td>S8</td><td>Interview Prep</td>', '<tr><td>S9</td><td>Interview Prep</td>')
mod2 = mod2.replace('<tr><td>S9</td><td>Checklist & Tổng kết</td>', '<tr><td>S10</td><td>Checklist & Tổng kết</td>')

# Update Sidebar nav-items
sidebar_s7 = '<div class="nav-item" onclick="showModule(7,this)"><span class="nav-number">S7</span>Practice & Error Catalog</div>'
new_sidebar = '<div class="nav-item" onclick="showModule(7,this)"><span class="nav-number">S7</span>Các Index Đặc Thù Khác</div>\n    <div class="nav-item" onclick="showModule(8,this)"><span class="nav-number">S8</span>Practice & Error Catalog</div>'
mod2 = mod2.replace(sidebar_s7, new_sidebar)

sidebar_s8 = '<div class="nav-item" onclick="showModule(8,this)"><span class="nav-number">S8</span>Interview Prep</div>'
new_sidebar_s8 = '<div class="nav-item" onclick="showModule(9,this)"><span class="nav-number">S9</span>Interview Prep</div>'
mod2 = mod2.replace(sidebar_s8, new_sidebar_s8)

sidebar_s9 = '<div class="nav-item" onclick="showModule(9,this)"><span class="nav-number">S9</span>Checklist & Tổng kết</div>'
new_sidebar_s9 = '<div class="nav-item" onclick="showModule(10,this)"><span class="nav-number">S10</span>Checklist & Tổng kết</div>'
mod2 = mod2.replace(sidebar_s9, new_sidebar_s9)

# Shift existing module IDs
mod2 = mod2.replace('<div class="module" id="s9">', '<div class="module" id="s10">')
mod2 = mod2.replace('<div class="module-tag">S9 · Summary</div>', '<div class="module-tag">S10 · Summary</div>')

mod2 = mod2.replace('<div class="module" id="s8">', '<div class="module" id="s9">')
mod2 = mod2.replace('<div class="module-tag">S8 · Interview Prep</div>', '<div class="module-tag">S9 · Interview Prep</div>')

mod2 = mod2.replace('<div class="module" id="s7">', '<div class="module" id="s8">')
mod2 = mod2.replace('<div class="module-tag">S7 · Practice & Error Catalog</div>', '<div class="module-tag">S8 · Practice & Error Catalog</div>')


# Insert new S7
s7_html = """
<div class="module" id="s7">
  <div class="module-header">
    <div class="module-tag">S7 · Special Indexes</div>
    <div class="module-title">Các Index Đặc Thù Khác</div>
    <div class="module-subtitle">Không phải lúc nào B-Tree cũng giải quyết được mọi bài toán. Spatial, Text và chuỗi dài đòi hỏi những loại index chuyên biệt.</div>
  </div>
  
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)">
      <span class="section-icon icon-detail">1</span>Tìm kiếm Không gian (Spatial Index)
      <span class="section-toggle">▼</span>
    </div>
    <div class="section-content">
      <p>Khi tìm kiếm dữ liệu địa lý (tọa độ, khoảng cách, bán kính), B-Tree không thể xử lý tốt vì dữ liệu có 2 chiều (Latitude/Longitude). Giải pháp là dùng <strong>R-Tree</strong> hoặc <strong>GIST</strong>.</p>
      
      <div class="tab-group" id="tabs-spatial">
        <div class="tab active" onclick="switchTab('tabs-spatial','spatial-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-spatial','spatial-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-spatial','spatial-ora')">Oracle</div>
      </div>
      
      <div class="tab-content active" id="spatial-pg">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>postgis.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Yêu cầu extension PostGIS</span>
<span class="kw">CREATE EXTENSION</span> postgis;
<span class="kw">CREATE TABLE</span> stores (
  id <span class="fn">SERIAL</span> <span class="kw">PRIMARY KEY</span>,
  name <span class="fn">VARCHAR</span>(<span class="num">100</span>),
  location <span class="fn">GEOMETRY</span>(Point, <span class="num">4326</span>)
);
<span class="comment">-- Dùng GIST index</span>
<span class="kw">CREATE INDEX</span> idx_stores_location <span class="kw">ON</span> stores <span class="kw">USING GIST</span> (location);

<span class="comment">-- Tìm store trong bán kính 5km</span>
<span class="kw">SELECT</span> name <span class="kw">FROM</span> stores 
<span class="kw">WHERE ST_DWithin</span>(location, ST_MakePoint(lng, lat)::geography, <span class="num">5000</span>);</pre>
        </div></div>
      </div>
      
      <div class="tab-content" id="spatial-my">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>spatial.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE TABLE</span> stores (
  id <span class="fn">INT PRIMARY KEY AUTO_INCREMENT</span>,
  name <span class="fn">VARCHAR</span>(<span class="num">100</span>),
  location <span class="fn">POINT NOT NULL SRID</span> <span class="num">4326</span>,
  <span class="kw">SPATIAL INDEX</span> (location)
);

<span class="comment">-- Tìm store bằng ST_Distance_Sphere</span>
<span class="kw">SELECT</span> name <span class="kw">FROM</span> stores 
<span class="kw">WHERE ST_Distance_Sphere</span>(location, ST_PointFromText(<span class="str">'POINT(lng lat)'</span>, <span class="num">4326</span>)) &lt;= <span class="num">5000</span>;</pre>
        </div></div>
      </div>
      
      <div class="tab-content" id="spatial-ora">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>spatial.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Dùng Oracle Spatial (MDSYS.SDO_GEOMETRY)</span>
<span class="kw">CREATE TABLE</span> stores (
  id <span class="fn">NUMBER PRIMARY KEY</span>,
  name <span class="fn">VARCHAR2</span>(<span class="num">100</span>),
  location SDO_GEOMETRY
);
<span class="comment">-- Đăng ký metadata cho cột spatial</span>
<span class="kw">INSERT INTO</span> user_sdo_geom_metadata <span class="kw">VALUES</span> (
  <span class="str">'STORES'</span>, <span class="str">'LOCATION'</span>, SDO_DIM_ARRAY(SDO_DIM_ELEMENT(<span class="str">'X'</span>, -180, 180, 0.005), SDO_DIM_ELEMENT(<span class="str">'Y'</span>, -90, 90, 0.005)), <span class="num">4326</span>
);
<span class="kw">CREATE INDEX</span> idx_stores_location <span class="kw">ON</span> stores(location) <span class="kw">INDEXTYPE IS</span> MDSYS.SPATIAL_INDEX;

<span class="comment">-- Tìm store trong bán kính 5km</span>
<span class="kw">SELECT</span> name <span class="kw">FROM</span> stores 
<span class="kw">WHERE SDO_WITHIN_DISTANCE</span>(location, SDO_GEOMETRY(<span class="num">2001</span>, <span class="num">4326</span>, SDO_POINT_TYPE(lng, lat, NULL), NULL, NULL), <span class="str">'distance=5000 unit=m'</span>) = <span class="str">'TRUE'</span>;</pre>
        </div></div>
      </div>
      
    </div>
  </div>

  <div class="section">
    <div class="section-header" onclick="toggleSection(this)">
      <span class="section-icon icon-detail">2</span>Trigram Index cho LIKE '%text%'
      <span class="section-toggle">▼</span>
    </div>
    <div class="section-content">
      <p>Khi dùng chuỗi tìm kiếm bắt đầu bằng dấu <code>%</code> (vd: <code>LIKE '%abc%'</code>), B-Tree bị vô hiệu hóa vì không thể so sánh tiền tố. Thay vào đó, ta băm nhỏ chuỗi thành các cụm 3 ký tự (trigram).</p>
      
      <div class="tab-group" id="tabs-trigram">
        <div class="tab active" onclick="switchTab('tabs-trigram','trig-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-trigram','trig-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-trigram','trig-ora')">Oracle</div>
      </div>
      
      <div class="tab-content active" id="trig-pg">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>pg_trgm.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE EXTENSION IF NOT EXISTS</span> pg_trgm;
<span class="comment">-- Hỗ trợ LIKE '%...' hoặc biểu thức chính quy (Regex) siêu nhanh</span>
<span class="kw">CREATE INDEX</span> idx_users_name_trgm <span class="kw">ON</span> users <span class="kw">USING GIN</span> (name gin_trgm_ops);

<span class="kw">SELECT</span> * <span class="kw">FROM</span> users <span class="kw">WHERE</span> name <span class="kw">ILIKE</span> <span class="str">'%duc%'</span>;</pre>
        </div></div>
      </div>
      
      <div class="tab-content" id="trig-my">
        <div class="info-box note">📌 <span>MySQL không có trigram chuyên dụng như Postgres. Thay vào đó, sử dụng <strong>FULLTEXT INDEX</strong> hoặc các search engine như Elasticsearch.</span></div>
      </div>
      
      <div class="tab-content" id="trig-ora">
        <div class="info-box note">📌 <span>Oracle sử dụng <strong>Oracle Text (CTXSYS.CONTEXT)</strong> để thực hiện Full-text search thay cho LIKE '%...%'.</span></div>
      </div>
      
    </div>
  </div>

  <div class="section">
    <div class="section-header" onclick="toggleSection(this)">
      <span class="section-icon icon-detail">3</span>Giới hạn Index & Prefix Index
      <span class="section-toggle">▼</span>
    </div>
    <div class="section-content">
      <p>B-Tree có giới hạn số bytes tối đa (vd: InnoDB MySQL giới hạn 3072 bytes). Nếu cột <code>VARCHAR(5000)</code> hoặc <code>TEXT</code> được đánh index, database sẽ từ chối. Giải pháp là đánh <strong>Prefix Index</strong> (Index tiền tố).</p>
      
      <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>prefix_index.sql</span></div><div class="cmd-body">
<pre><span class="db-tag db-my">MySQL</span>
<span class="comment">-- Đánh index chỉ trên 50 ký tự đầu tiên của chuỗi</span>
<span class="kw">CREATE INDEX</span> idx_articles_title <span class="kw">ON</span> articles(title(<span class="num">50</span>));

<span class="db-tag db-pg">PostgreSQL</span>
<span class="comment">-- Nếu chuỗi quá dài, bạn có thể tạo Hash Index (kích thước nhỏ gọn, dùng để so sánh =)</span>
<span class="kw">CREATE INDEX</span> idx_session_token_hash <span class="kw">ON</span> sessions <span class="kw">USING HASH</span> (token);</pre>
        </div></div>
        <div class="info-box warn">⚠️ <span><strong>Trade-off:</strong> Prefix index không thể dùng cho <code>ORDER BY</code> hoặc <code>GROUP BY</code>, và cũng không thể đóng vai trò làm Covering Index được.</span></div>
    </div>
  </div>
</div>
"""

mod2 = mod2.replace('<div class="module" id="s8">', s7_html + '\n<div class="module" id="s8">')

# Update checklist progress html in the new s10 module
prog_old = r'<div class="progress-text">Progress: <span id="progressPct">0%</span></div>\s*<div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>'
prog_new = r'<p class="progress-text" id="checklist-progress-text">0/6 mục hoàn thành (0%)</p>\n      <div class="progress-bar"><div class="progress-fill" id="checklist-progress-fill"></div></div>'
mod2 = re.sub(prog_old, prog_new, mod2, flags=re.DOTALL)

with open('D:/DE/Tuning_SQL/Module03_Schema_Physical_Design_new.html', 'w', encoding='utf-8') as f:
    f.write(mod2)

print('Success')
