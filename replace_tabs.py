import re

file_path = 'Week01_SQL_Advanced.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(
    r'<div class="cmd-block">\s*<div class="cmd-header"><div class="cmd-dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div><span>postgresql \+ oracle sql · ([^<]+)</span></div>\s*<div class="cmd-body"><pre>(.*?)</pre></div>\s*</div>',
    re.DOTALL
)

def replacer(match):
    filename = match.group(1)
    code = match.group(2)
    
    # generate a short id based on filename
    tab_id = filename.split('.')[0].replace('_', '')
    
    # generate tabs
    res = f'''<div class="tab-group" id="{tab_id}-tabs">
        <div class="tab active" onclick="switchTab('{tab_id}-tabs','{tab_id}-pg')">🐘 PostgreSQL</div>
        <div class="tab" onclick="switchTab('{tab_id}-tabs','{tab_id}-oracle')">🔴 Oracle SQL</div>
      </div>
      <div id="{tab_id}-pg" class="tab-content active">
        <span class="db-tag db-pg">PostgreSQL</span>
        <p style="font-size:0.84rem;color:var(--text-muted);margin:8px 0">Cú pháp chuẩn ANSI SQL, chạy hoàn toàn giống nhau trên PostgreSQL và Oracle.</p>
      <div class="cmd-block">
        <div class="cmd-header"><div class="cmd-dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div><span>postgresql · {filename}</span></div>
        <div class="cmd-body"><pre>{code}</pre></div>
      </div>
      </div>
      <div id="{tab_id}-oracle" class="tab-content">
        <span class="db-tag db-oracle">Oracle SQL</span>
        <p style="font-size:0.84rem;color:var(--text-muted);margin:8px 0">Cú pháp chuẩn ANSI SQL, chạy hoàn toàn giống nhau trên PostgreSQL và Oracle.</p>
      <div class="cmd-block">
        <div class="cmd-header"><div class="cmd-dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div><span>oracle sql · {filename}</span></div>
        <div class="cmd-body"><pre>{code}</pre></div>
      </div>
      </div>'''
    return res

new_content = pattern.sub(replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Replaced successfully')
