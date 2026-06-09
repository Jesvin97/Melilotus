import json, re

with open('d:/melilotus/melilotus-mobile.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.__LIGHTHOUSE_JSON__ = (\{.*?\});</script>', content, re.DOTALL)
if match:
    lh_data = json.loads(match.group(1))
    print('SCORES:')
    for cid, c in lh_data['categories'].items():
        print(f"{c['title']}: {c.get('score', 0) * 100:.0f}")
    
    print('\nISSUES:')
    for aid, a in lh_data['audits'].items():
        score = a.get('score')
        if score is not None and score < 1 and a.get('scoreDisplayMode') in ('numeric', 'binary'):
            print(f"- {a.get('title')}: {a.get('displayValue', 'Failed')}")
            print(f"  Description: {a.get('description', '').split('.')[0]}")
else:
    print('Could not parse JSON')
