import re

with open('D:/DE/Tuning_SQL/Module03_Schema_Physical_Design.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. S2 Unique Null
s2_old = """      <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>unique-null.sql</span></div><div class="cmd-body">
<pre><span class="db-tag db-pg">PostgreSQL</span>
<span class="kw">CREATE UNIQUE INDEX</span> uq_active_email
<span class="kw">ON</span> users (email)
<span class="kw">WHERE</span> deleted_at <span class="kw">IS NULL</span>;

<span class="db-tag db-oracle">Oracle</span>
<span class="kw">CREATE UNIQUE INDEX</span> uq_active_email
<span class="kw">ON</span> users (
  <span class="kw">CASE WHEN</span> deleted_at <span class="kw">IS NULL THEN</span> email <span class="kw">END</span>
);</pre>
      </div></div>"""

s2_new = """      <div class="tab-group" id="tabs-uq">
        <div class="tab active" onclick="switchTab('tabs-uq','uq-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-uq','uq-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="uq-pg">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>unique-null.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE UNIQUE INDEX</span> uq_active_email
<span class="kw">ON</span> users (email)
<span class="kw">WHERE</span> deleted_at <span class="kw">IS NULL</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="uq-ora">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>unique-null.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE UNIQUE INDEX</span> uq_active_email
<span class="kw">ON</span> users (
  <span class="kw">CASE WHEN</span> deleted_at <span class="kw">IS NULL THEN</span> email <span class="kw">END</span>
);</pre>
        </div></div>
      </div>"""
html = html.replace(s2_old, s2_new)

# 2. S2 Exclusion constraint (just strip the pg tag)
html = html.replace('<span class="db-tag db-pg">PostgreSQL</span>\n', '')


# 3. S3 JSON
s3_old = """      <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>json-index.sql</span></div><div class="cmd-body">
<pre><span class="db-tag db-pg">PostgreSQL</span>
<span class="kw">CREATE TABLE</span> products (
  id <span class="fn">BIGSERIAL</span> <span class="kw">PRIMARY KEY</span>,
  name <span class="fn">TEXT</span> <span class="kw">NOT NULL</span>,
  attrs <span class="fn">JSONB</span> <span class="kw">NOT NULL</span>
);
<span class="kw">CREATE INDEX</span> idx_products_attrs_gin <span class="kw">ON</span> products <span class="kw">USING</span> gin(attrs);
<span class="kw">CREATE INDEX</span> idx_products_color <span class="kw">ON</span> products ((attrs-&gt;&gt;<span class="str">'color'</span>));

<span class="db-tag db-my">MySQL</span>
<span class="kw">ALTER TABLE</span> products
  <span class="kw">ADD COLUMN</span> color <span class="fn">VARCHAR</span>(<span class="num">30</span>) <span class="kw">GENERATED ALWAYS AS</span> (JSON_UNQUOTE(attrs-&gt;<span class="str">'$.color'</span>)) <span class="kw">STORED</span>,
  <span class="kw">ADD INDEX</span> idx_products_color (color);

<span class="db-tag db-oracle">Oracle</span>
<span class="kw">CREATE SEARCH INDEX</span> idx_products_attrs <span class="kw">ON</span> products(attrs) <span class="kw">FOR JSON</span>;</pre>
      </div></div>"""

s3_new = """      <div class="tab-group" id="tabs-json">
        <div class="tab active" onclick="switchTab('tabs-json','json-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-json','json-my')">MySQL</div>
        <div class="tab" onclick="switchTab('tabs-json','json-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="json-pg">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>json-index.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE TABLE</span> products (
  id <span class="fn">BIGSERIAL</span> <span class="kw">PRIMARY KEY</span>,
  name <span class="fn">TEXT</span> <span class="kw">NOT NULL</span>,
  attrs <span class="fn">JSONB</span> <span class="kw">NOT NULL</span>
);
<span class="kw">CREATE INDEX</span> idx_products_attrs_gin <span class="kw">ON</span> products <span class="kw">USING</span> gin(attrs);
<span class="kw">CREATE INDEX</span> idx_products_color <span class="kw">ON</span> products ((attrs-&gt;&gt;<span class="str">'color'</span>));</pre>
        </div></div>
      </div>
      <div class="tab-content" id="json-my">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>json-index.sql</span></div><div class="cmd-body">
<pre><span class="kw">ALTER TABLE</span> products
  <span class="kw">ADD COLUMN</span> color <span class="fn">VARCHAR</span>(<span class="num">30</span>) <span class="kw">GENERATED ALWAYS AS</span> (JSON_UNQUOTE(attrs-&gt;<span class="str">'$.color'</span>)) <span class="kw">STORED</span>,
  <span class="kw">ADD INDEX</span> idx_products_color (color);</pre>
        </div></div>
      </div>
      <div class="tab-content" id="json-ora">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>json-index.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE SEARCH INDEX</span> idx_products_attrs <span class="kw">ON</span> products(attrs) <span class="kw">FOR JSON</span>;</pre>
        </div></div>
      </div>"""
html = html.replace(s3_old, s3_new)

# 4. S5 Partition
s5_old = """      <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>partitioning.sql</span></div><div class="cmd-body">
<pre><span class="db-tag db-pg">PostgreSQL</span>
<span class="kw">CREATE TABLE</span> audit_logs (
  id <span class="fn">BIGINT</span>,
  created_at <span class="fn">TIMESTAMPTZ</span> <span class="kw">NOT NULL</span>,
  payload <span class="fn">JSONB</span> <span class="kw">NOT NULL</span>
) <span class="kw">PARTITION BY RANGE</span> (created_at);

<span class="kw">CREATE TABLE</span> audit_logs_2026_05 <span class="kw">PARTITION OF</span> audit_logs
<span class="kw">FOR VALUES FROM</span> (<span class="str">'2026-05-01'</span>) <span class="kw">TO</span> (<span class="str">'2026-06-01'</span>);

<span class="comment">-- Xóa cả tháng: DROP/TRUNCATE partition, không DELETE từng row</span>

<span class="db-tag db-oracle">Oracle</span>
<span class="kw">CREATE TABLE</span> audit_logs (
  id <span class="fn">NUMBER</span>,
  created_at <span class="fn">TIMESTAMP</span> <span class="kw">NOT NULL</span>,
  payload <span class="fn">CLOB</span> <span class="kw">CHECK</span> (payload <span class="kw">IS JSON</span>)
)
<span class="kw">PARTITION BY RANGE</span> (created_at)
<span class="kw">INTERVAL</span> (<span class="kw">NUMTOYMINTERVAL</span>(<span class="num">1</span>, <span class="str">'MONTH'</span>))
(<span class="kw">PARTITION</span> p_init <span class="kw">VALUES LESS THAN</span> (<span class="kw">TIMESTAMP</span> <span class="str">'2026-01-01 00:00:00'</span>));</pre>
      </div></div>"""

s5_new = """      <div class="tab-group" id="tabs-part">
        <div class="tab active" onclick="switchTab('tabs-part','part-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-part','part-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="part-pg">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>partitioning.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE TABLE</span> audit_logs (
  id <span class="fn">BIGINT</span>,
  created_at <span class="fn">TIMESTAMPTZ</span> <span class="kw">NOT NULL</span>,
  payload <span class="fn">JSONB</span> <span class="kw">NOT NULL</span>
) <span class="kw">PARTITION BY RANGE</span> (created_at);

<span class="kw">CREATE TABLE</span> audit_logs_2026_05 <span class="kw">PARTITION OF</span> audit_logs
<span class="kw">FOR VALUES FROM</span> (<span class="str">'2026-05-01'</span>) <span class="kw">TO</span> (<span class="str">'2026-06-01'</span>);

<span class="comment">-- Xóa cả tháng: DROP/TRUNCATE partition, không DELETE từng row</span></pre>
        </div></div>
      </div>
      <div class="tab-content" id="part-ora">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>partitioning.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE TABLE</span> audit_logs (
  id <span class="fn">NUMBER</span>,
  created_at <span class="fn">TIMESTAMP</span> <span class="kw">NOT NULL</span>,
  payload <span class="fn">CLOB</span> <span class="kw">CHECK</span> (payload <span class="kw">IS JSON</span>)
)
<span class="kw">PARTITION BY RANGE</span> (created_at)
<span class="kw">INTERVAL</span> (<span class="kw">NUMTOYMINTERVAL</span>(<span class="num">1</span>, <span class="str">'MONTH'</span>))
(<span class="kw">PARTITION</span> p_init <span class="kw">VALUES LESS THAN</span> (<span class="kw">TIMESTAMP</span> <span class="str">'2026-01-01 00:00:00'</span>));</pre>
        </div></div>
      </div>"""
html = html.replace(s5_old, s5_new)

# 5. S6 Precompute
s6_old = """      <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>precompute.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Summary table cho dashboard doanh thu theo ngày</span>
<span class="kw">CREATE TABLE</span> daily_revenue (
  revenue_date <span class="fn">DATE</span> <span class="kw">PRIMARY KEY</span>,
  order_count <span class="fn">BIGINT</span> <span class="kw">NOT NULL</span>,
  total_amount <span class="fn">NUMERIC</span>(<span class="num">14</span>,<span class="num">2</span>) <span class="kw">NOT NULL</span>,
  refreshed_at <span class="fn">TIMESTAMP</span> <span class="kw">NOT NULL</span>
);

<span class="db-tag db-pg">PostgreSQL</span>
<span class="kw">CREATE MATERIALIZED VIEW</span> mv_daily_revenue <span class="kw">AS</span>
<span class="kw">SELECT</span> created_at::<span class="fn">date</span> <span class="kw">AS</span> revenue_date,
       <span class="fn">COUNT</span>(*) order_count,
       <span class="fn">SUM</span>(total_amount) total_amount
<span class="kw">FROM</span> orders
<span class="kw">WHERE</span> status = <span class="str">'paid'</span>
<span class="kw">GROUP BY</span> created_at::<span class="fn">date</span>;

<span class="db-tag db-oracle">Oracle</span>
<span class="kw">CREATE MATERIALIZED VIEW</span> mv_daily_revenue
<span class="kw">BUILD IMMEDIATE REFRESH FAST ON DEMAND AS</span>
<span class="kw">SELECT</span> TRUNC(created_at) revenue_date, COUNT(*) order_count, SUM(total_amount) total_amount
<span class="kw">FROM</span> orders
<span class="kw">WHERE</span> status = <span class="str">'PAID'</span>
<span class="kw">GROUP BY</span> TRUNC(created_at);</pre>
      </div></div>"""

s6_new = """      <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>precompute_table.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Summary table cho dashboard doanh thu theo ngày</span>
<span class="kw">CREATE TABLE</span> daily_revenue (
  revenue_date <span class="fn">DATE</span> <span class="kw">PRIMARY KEY</span>,
  order_count <span class="fn">BIGINT</span> <span class="kw">NOT NULL</span>,
  total_amount <span class="fn">NUMERIC</span>(<span class="num">14</span>,<span class="num">2</span>) <span class="kw">NOT NULL</span>,
  refreshed_at <span class="fn">TIMESTAMP</span> <span class="kw">NOT NULL</span>
);</pre>
      </div></div>
      <h3 class="blue">Materialized View</h3>
      <div class="tab-group" id="tabs-mv">
        <div class="tab active" onclick="switchTab('tabs-mv','mv-pg')">PostgreSQL</div>
        <div class="tab" onclick="switchTab('tabs-mv','mv-ora')">Oracle</div>
      </div>
      <div class="tab-content active" id="mv-pg">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>materialized_view.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE MATERIALIZED VIEW</span> mv_daily_revenue <span class="kw">AS</span>
<span class="kw">SELECT</span> created_at::<span class="fn">date</span> <span class="kw">AS</span> revenue_date,
       <span class="fn">COUNT</span>(*) order_count,
       <span class="fn">SUM</span>(total_amount) total_amount
<span class="kw">FROM</span> orders
<span class="kw">WHERE</span> status = <span class="str">'paid'</span>
<span class="kw">GROUP BY</span> created_at::<span class="fn">date</span>;</pre>
        </div></div>
      </div>
      <div class="tab-content" id="mv-ora">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>materialized_view.sql</span></div><div class="cmd-body">
<pre><span class="kw">CREATE MATERIALIZED VIEW</span> mv_daily_revenue
<span class="kw">BUILD IMMEDIATE REFRESH FAST ON DEMAND AS</span>
<span class="kw">SELECT</span> TRUNC(created_at) revenue_date, COUNT(*) order_count, SUM(total_amount) total_amount
<span class="kw">FROM</span> orders
<span class="kw">WHERE</span> status = <span class="str">'PAID'</span>
<span class="kw">GROUP BY</span> TRUNC(created_at);</pre>
        </div></div>
      </div>"""
html = html.replace(s6_old, s6_new)

# 6. S7 Prefix index
s7_old = """      <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>prefix_index.sql</span></div><div class="cmd-body">
<pre><span class="db-tag db-my">MySQL</span>
<span class="comment">-- Đánh index chỉ trên 50 ký tự đầu tiên của chuỗi</span>
<span class="kw">CREATE INDEX</span> idx_articles_title <span class="kw">ON</span> articles(title(<span class="num">50</span>));

<span class="db-tag db-pg">PostgreSQL</span>
<span class="comment">-- Nếu chuỗi quá dài, bạn có thể tạo Hash Index (kích thước nhỏ gọn, dùng để so sánh =)</span>
<span class="kw">CREATE INDEX</span> idx_session_token_hash <span class="kw">ON</span> sessions <span class="kw">USING HASH</span> (token);</pre>
        </div></div>"""

s7_new = """      <div class="tab-group" id="tabs-prefix">
        <div class="tab active" onclick="switchTab('tabs-prefix','prefix-my')">MySQL (Prefix)</div>
        <div class="tab" onclick="switchTab('tabs-prefix','prefix-pg')">PostgreSQL (Hash)</div>
      </div>
      <div class="tab-content active" id="prefix-my">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>prefix_index.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Đánh index chỉ trên 50 ký tự đầu tiên của chuỗi</span>
<span class="kw">CREATE INDEX</span> idx_articles_title <span class="kw">ON</span> articles(title(<span class="num">50</span>));</pre>
        </div></div>
      </div>
      <div class="tab-content" id="prefix-pg">
        <div class="cmd-block"><div class="cmd-header"><span>● ● ●</span><span>hash_index.sql</span></div><div class="cmd-body">
<pre><span class="comment">-- Nếu chuỗi quá dài, bạn có thể tạo Hash Index (kích thước nhỏ gọn, dùng để so sánh =)</span>
<span class="kw">CREATE INDEX</span> idx_session_token_hash <span class="kw">ON</span> sessions <span class="kw">USING HASH</span> (token);</pre>
        </div></div>
      </div>"""
html = html.replace(s7_old, s7_new)


with open('D:/DE/Tuning_SQL/Module03_Schema_Physical_Design_new.html', 'w', encoding='utf-8') as f:
    f.write(html)
