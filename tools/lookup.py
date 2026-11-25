"""Show English -> Japanese pairs whose official English text matches a regex.
usage: py -I lookup.py <en_US dialog.tlk> <dialog.tra> <regex> [max]"""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tlk import read_tlk, read_tra

_, en = read_tlk(sys.argv[1])
tra = read_tra(sys.argv[2])
rx = re.compile(sys.argv[3], re.I)
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 15
JP = re.compile(r'[\u3040-\u30ff\u4e00-\u9fff]')
n = 0
for i, e in enumerate(en):
    s = e[4].decode('utf-8', 'replace')
    if rx.search(s) and JP.search(tra[i][0]):
        print(f'#{i}\nEN: {s[:400]}\nJA: {tra[i][0][:400]}\n')
        n += 1
        if n >= mx:
            break
