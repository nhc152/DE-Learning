import json
import re
from collections import Counter

with open(r'D:\TaiLieu\Data Engineer\DE Roadmap\DE-Learning\interview-prep-html\DE_Interview_Handbook.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<script id="handbook-data" type="application/json">(.*?)</script>', content, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    c = Counter(q['moduleId'] for q in data['questions'])
    for m in data['modules']:
        print(f"{m['id']}: {c[m['id']]} questions")
