import re
import os

def parse_markdown(lines):
    html = []
    in_list = False
    in_table = False
    in_code = False
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Level labels for sidebar
        if line.startswith('LEVEL:'):
            html.append(f'<!-- LEVEL: {line[6:].strip()} -->')
            i += 1
            continue

        # Code blocks
        if line.startswith('```'):
            if not in_code:
                in_code = True
                html.append('<div class="cmd-block"><div class="cmd-header"><div class="cmd-dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div><span>Prompt / Code</span></div><div class="cmd-body"><pre><code>')
            else:
                in_code = False
                html.append('</code></pre></div></div>')
            i += 1
            continue
            
        if in_code:
            html.append(line.replace('<', '&lt;').replace('>', '&gt;'))
            i += 1
            continue

        # Tables
        if line.startswith('|') and '-|-' not in line and '---' not in line:
            if not in_table:
                in_table = True
                html.append('<table>')
            
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if len(cells) > 0:
                if html[-1] == '<table>':
                    html.append('<tr>' + ''.join(f'<th>{c}</th>' for c in cells) + '</tr>')
                else:
                    html.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
            i += 1
            continue
            
        if line.startswith('|') and ('-|-' in line or '---' in line):
            i += 1
            continue

        if in_table and not line.startswith('|'):
            in_table = False
            html.append('</table>')

        # Blockquotes (info boxes)
        m = re.match(r'^>\s*\*\*(.*?):\*\*\s*(.*)', line)
        if m:
            title, content = m.group(1), m.group(2)
            box_type = 'tip'
            icon = '✅'
            if 'LƯU Ý' in title.upper() or 'QUAN TRỌNG' in title.upper() or 'SAI LẦM' in title.upper():
                box_type = 'warn'
                icon = '⚠️'
            html.append(f'<div class="info-box {box_type}">{icon} <span><strong>{title}:</strong> {content}</span></div>')
            i += 1
            continue

        # Normal blockquotes
        if line.startswith('>'):
            content = line[1:].strip()
            # Try to grab following lines if they are also blockquotes
            while i+1 < len(lines) and lines[i+1].startswith('>'):
                i += 1
                content += ' ' + lines[i][1:].strip()
            html.append(f'<div class="info-box note">📌 <span>{content}</span></div>')
            i += 1
            continue

        # Headings
        if line.startswith('### '):
            html.append(f'<h3>{line[4:].strip()}</h3>')
            i += 1
            continue
        if line.startswith('## '):
            html.append(f'<h2>{line[3:].strip()}</h2>')
            i += 1
            continue
        if line.startswith('# '):
            html.append(f'<h1>{line[2:].strip()}</h1>')
            i += 1
            continue

        # Horizontal rule
        if line == '---':
            html.append('<hr style="border-color: var(--border); margin: 20px 0;">')
            i += 1
            continue

        # Lists
        if line.startswith('- ') or line.startswith('* '):
            if not in_list:
                in_list = True
                html.append('<ul>')
            html.append(f'<li>{line[2:].strip()}</li>')
            i += 1
            continue
            
        if in_list and not (line.startswith('- ') or line.startswith('* ')):
            in_list = False
            html.append('</ul>')
            
        # Bold text processing for normal lines
        if line.strip():
            # Bold
            processed = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            # Italics
            processed = re.sub(r'\*(.*?)\*', r'<em>\1</em>', processed)
            html.append(f'<p>{processed}</p>')
        
        i += 1

    if in_list:
        html.append('</ul>')
    if in_table:
        html.append('</table>')

    return html

def convert_file(md_path, html_path, template_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
        
    css_start = template_content.find('<style>')
    css_end = template_content.find('</style>') + 8
    css = template_content[css_start:css_end]
    
    js_start = template_content.find('<script>')
    js_end = template_content.find('</script>') + 9
    js = template_content[js_start:js_end]

    with open(md_path, 'r', encoding='utf-8') as f:
        md_lines = f.readlines()

    parsed_html = parse_markdown(md_lines)

    modules = []
    level_labels = {}
    current_module = None
    current_section = None
    hero_title = ""
    hero_desc = []

    for tag in parsed_html:
        if tag.startswith('<!-- LEVEL:'):
            target_idx = len(modules)
            if current_module:
                target_idx += 1
            level_labels[target_idx] = tag[11:-3].strip()
        elif tag.startswith('<h1>'):
            hero_title = tag[4:-5]
        elif tag.startswith('<h2>'):
            if current_section:
                current_module['sections'].append(current_section)
                current_section = None
            if current_module:
                modules.append(current_module)
            current_module = {'title': tag[4:-5], 'sections': [], 'content': []}
        elif tag.startswith('<h3>'):
            if current_section:
                current_module['sections'].append(current_section)
            current_section = {'title': tag[4:-5], 'content': []}
        else:
            if current_section:
                current_section['content'].append(tag)
            elif current_module:
                current_module['content'].append(tag)
            elif not hero_title and tag.startswith('<p>'):
                pass
            elif hero_title and tag.startswith('<p>'):
                hero_desc.append(tag[3:-4])

    if current_section:
        current_module['sections'].append(current_section)
    if current_module:
        modules.append(current_module)

    # Build final HTML
    output = []
    output.append('<!DOCTYPE html>\n<html lang="vi">\n<head>')
    output.append('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    output.append(f'<title>{hero_title}</title>')
    output.append(css)
    output.append('</head>\n<body>')
    
    # Hero
    output.append('<div class="hero">')
    output.append(f'  <h1>{hero_title}</h1>')
    for p in hero_desc:
        output.append(f'  <p>{p}</p>')
    output.append('  <div class="badge-row"><span class="badge badge-blue">Claude AI Guide</span></div>')
    output.append('</div>')

    output.append('<div class="container">')
    
    # Sidebar
    output.append('  <div class="sidebar">')
    output.append('    <div class="sidebar-title">NỘI DUNG CHÍNH</div>')
    for i, mod in enumerate(modules):
        if i in level_labels:
            output.append(f'    <div class="level-label l0">{level_labels[i]}</div>')
        active = 'active' if i == 0 else ''
        output.append(f'    <a class="nav-item {active}" onclick="showModule({i}, this)">M{i+1}: {mod["title"]}</a>')
    output.append('  </div>')

    # Main content
    output.append('  <div class="main">')
    
    for i, mod in enumerate(modules):
        active = 'active' if i == 0 else ''
        output.append(f'    <div class="module {active}" id="module-{i}">')
        output.append('      <div class="module-header">')
        output.append(f'        <div class="module-tag">MODULE {i+1}</div>')
        output.append(f'        <div class="module-title">{mod["title"]}</div>')
        output.append('      </div>')
        
        for c in mod['content']:
            output.append(c)
            
        for j, sec in enumerate(mod['sections']):
            output.append('      <div class="section">')
            output.append(f'        <div class="section-header" onclick="toggleSection(this)">')
            output.append('          <div class="section-icon icon-detail">📖</div>')
            output.append(f'          {sec["title"]}')
            output.append('          <span class="section-toggle">▼ Mở rộng</span>')
            output.append('        </div>')
            output.append('        <div class="section-content">')
            for c in sec['content']:
                output.append(c)
            output.append('        </div>')
            output.append('      </div>')
            
        # Nav buttons
        output.append('      <div class="nav-buttons">')
        if i > 0:
            output.append(f'        <button class="nav-btn" onclick="goPrev({i})">← Phần trước</button>')
        else:
            output.append('        <div></div>')
        if i < len(modules) - 1:
            output.append(f'        <button class="nav-btn primary" onclick="goNext({i})">Phần tiếp theo →</button>')
        output.append('      </div>')
            
        output.append('    </div>') # end module
        
    output.append('  </div>') # end main
    output.append('</div>') # end container
    
    # Custom toggle section script to match the template exactly
    custom_js = """
<script>
function showModule(idx, el) {
  document.querySelectorAll('.module').forEach(m => m.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  document.getElementById('module-' + idx).classList.add('active');
  if(el) el.classList.add('active');
  else {
    const navs = document.querySelectorAll('.nav-item');
    if(navs[idx]) navs[idx].classList.add('active');
  }
  window.scrollTo(0, 0);
}
function goNext(idx) {
  showModule(idx + 1, null);
}
function goPrev(idx) {
  showModule(idx - 1, null);
}
function toggleSection(header) {
  const content = header.nextElementSibling;
  const toggle = header.querySelector('.section-toggle');
  if (content.style.display === 'none') {
    content.style.display = 'block';
    toggle.textContent = '▼ Thu gọn';
  } else {
    content.style.display = 'none';
    toggle.textContent = '▶ Mở rộng';
  }
}
</script>
"""
    output.append(custom_js)
    output.append('</body>\n</html>')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))

if __name__ == '__main__':
    base_dir = r'D:\TaiLieu\Data Engineer\DE Roadmap\DE-Learning'
    template = os.path.join(base_dir, 'Week00_Setup.html')
    
    files = [
        ('Huong-dan-su-dung-Claude-AI-hieu-qua.md', 'Huong-dan-su-dung-Claude-AI-hieu-qua.html'),
        ('Claude-AI-cho-CEO-Thuc-hanh.md', 'Claude-AI-cho-CEO-Thuc-hanh.html')
    ]
    
    for md_name, html_name in files:
        convert_file(
            os.path.join(base_dir, md_name),
            os.path.join(base_dir, html_name),
            template
        )
