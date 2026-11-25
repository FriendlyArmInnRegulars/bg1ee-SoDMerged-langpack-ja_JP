"""List strings in dialog.tra that still contain untranslated English prose."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tlk import read_tlk, read_tra

tra_dir, en_tlk, out = sys.argv[1:4]
tra = read_tra(os.path.join(tra_dir, 'dialog.tra'))
traf = read_tra(os.path.join(tra_dir, 'dialogf.tra'))
_, en = read_tlk(en_tlk)

JP = re.compile(r'[぀-ヿ一-鿿]')
# an English run: >=3 consecutive latin words (tokens like <CHARNAME> excluded)
RUN = re.compile(r"(?<![<\w])[A-Za-z][A-Za-z'\-]*(?:[ ,.;:!?\"]+[A-Za-z][A-Za-z'\-]*){2,}")
SKIP_PREFIX = ('(placeholder)', '<<', '0000')

items = []
for i in range(len(en)):
    s = tra[i][0]
    if not s.strip() or s == '<NO TEXT>' or s.startswith(SKIP_PREFIX):
        continue
    body = re.sub(r'^\[[^\]]*\]', '', s)          # dev voice labels like [GENERIC MALE 1]
    body_nl = re.sub(r'<[A-Z0-9_]+>', '', body)
    runs = [r for r in RUN.findall(body_nl) if len(r.split()) >= 3]
    if not runs:
        continue
    ens = en[i][4].decode('utf-8', 'replace')
    if ens == s and not JP.search(s) and re.match(r'^\s*\[', ens):
        continue
    items.append({'id': i, 'en': ens, 'ja': s,
                  'ja_f': traf[i][0] if traf[i][0] != s else None,
                  'kind': 'mixed' if JP.search(body) else 'english'})
json.dump(items, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(items), Counter(x['kind'] for x in items))
