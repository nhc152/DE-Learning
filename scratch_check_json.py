import json
import re

with open(r'D:\TaiLieu\Data Engineer\DE Roadmap\DE-Learning\interview-prep-html\DE_Interview_Handbook.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<script id="handbook-data" type="application/json">(.*?)</script>', content, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    print(f'Modules: {len(data.get("modules", []))}')
    for m in data.get('modules', []):
        print(f"  - {m['id']}: {m['title']}")
    
    questions = data.get('questions', [])
    print(f'\nTotal Questions: {len(questions)}')
    
    issues = []
    mistakes_identical_tradeoffs = 0
    missing_fields = 0
    
    for q in questions:
        if not q.get('question'): issues.append(f"Q {q['id']} missing question")
        if not q.get('raw'): issues.append(f"Q {q['id']} missing raw")
        if not q.get('short'): missing_fields += 1
        if not q.get('deep'): missing_fields += 1
        if not q.get('production'): missing_fields += 1
        if not q.get('tradeoffs'): missing_fields += 1
        if not q.get('mistakes'): missing_fields += 1
        if not q.get('followups'): missing_fields += 1
        
        if q.get('tradeoffs') and q.get('tradeoffs') == q.get('mistakes'):
            mistakes_identical_tradeoffs += 1
            issues.append(f"Q {q['id']} has identical tradeoffs and mistakes")
            
    print(f'\nIssues found: {len(issues)}')
    print(f'Identical tradeoffs/mistakes: {mistakes_identical_tradeoffs}')
    print(f'Missing fields: {missing_fields}')
    for idx, iss in enumerate(issues[:20]):
        print(f'  {iss}')
    if len(issues) > 20:
        print(f'  ... and {len(issues) - 20} more')
else:
    print('JSON not found')
