"""Build ja_JP dialog.tlk / dialogf.tlk from repo .tra files, using official SoD ja_JP tlk as base."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tlk import read_tlk, write_tlk, read_tra

base_dir, tra_dir, out_dir = sys.argv[1:4]
lang, male = read_tlk(os.path.join(base_dir, 'dialog.tlk'))
langf, fem = read_tlk(os.path.join(base_dir, 'dialogf.tlk'))
tra = read_tra(os.path.join(tra_dir, 'dialog.tra'))
traf = read_tra(os.path.join(tra_dir, 'dialogf.tra'))
assert len(male) == len(fem) == 71404 and len(tra) == len(traf) == 71404

def apply(entries, texts):
    out = []
    changed = 0
    for i, (flags, snd, vol, pitch, txt) in enumerate(entries):
        new = texts[i].encode('utf-8')
        if new != txt:
            changed += 1
        f = flags
        if new:
            f |= 1
        out.append([f, snd, vol, pitch, new])
    return out, changed

male_txt = [tra[i][0] for i in range(len(male))]
# Female: keep a female-specific variant only where it actually differs from the
# official male text; otherwise follow the (more complete) male translation.
fem_txt = []
for i in range(len(fem)):
    tf = traf[i][0]
    official_male = male[i][4].decode('utf-8', 'replace')
    fem_txt.append(tf if tf != official_male else tra[i][0])

m, cm = apply(male, male_txt)
f, cf = apply(fem, fem_txt)
os.makedirs(out_dir, exist_ok=True)
write_tlk(os.path.join(out_dir, 'dialog.tlk'), lang, m)
write_tlk(os.path.join(out_dir, 'dialogf.tlk'), langf, f)
print('dialog.tlk changed', cm, '/ dialogf.tlk changed', cf)
