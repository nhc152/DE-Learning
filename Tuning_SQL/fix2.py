import re
import os

with open('D:/DE/Tuning_SQL/Module01_SQL_Tuning_Index.html', 'r', encoding='utf-8') as f:
    mod1 = f.read()

with open('D:/DE/Tuning_SQL/Module02_SQL_Tuning_Query_Workflows.html', 'r', encoding='utf-8') as f:
    mod2 = f.read()

style1 = re.search(r'(<style>.*?</style>)', mod1, re.DOTALL).group(1)
script1 = re.search(r'(<script>.*?</script>)', mod1, re.DOTALL).group(1)

# Replace style
mod2 = re.sub(r'<style>.*?</style>', style1, mod2, flags=re.DOTALL)

# Replace sidebar tags
mod2 = mod2.replace('<aside class="sidebar">', '<nav class="sidebar">')
mod2 = mod2.replace('</aside>', '</nav>')

# Remove nav-buttons
mod2 = re.sub(r'<div class="nav-buttons">.*?</div>', '', mod2, flags=re.DOTALL)

# Fix progress bar HTML
prog_old = r'<div class="progress-text">Progress: <span id="progressPct">0%</span></div>\s*<div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>'
prog_new = r'<p class="progress-text" id="checklist-progress-text">0/6 mục hoàn thành (0%)</p>\n      <div class="progress-bar"><div class="progress-fill" id="checklist-progress-fill"></div></div>'
mod2 = re.sub(prog_old, prog_new, mod2, flags=re.DOTALL)

# Replace script
mod2 = re.sub(r'<script>.*?</script>', script1, mod2, flags=re.DOTALL)

# Replace onclick attributes for the sidebar items
mod2 = mod2.replace('onclick="showModule(0,this)"', 'onclick="showModule(0,this)"')
# Note: Module01 has onclick="showModule(x,this)" instead of nextModule()/prevModule(), but wait, the nav items in Module02 already use onclick="showModule(x,this)"! Let's verify that. Yes they do.

# Save to a new file since the old one is permission denied
new_file_path = 'D:/DE/Tuning_SQL/Module02_SQL_Tuning_Query_Workflows_new.html'
with open(new_file_path, 'w', encoding='utf-8') as f:
    f.write(mod2)

print('Success')
