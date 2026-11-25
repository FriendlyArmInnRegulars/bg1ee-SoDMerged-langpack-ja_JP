"""Replace the text of selected @N entries in a WeiDU .tra file in place,
keeping everything else (line endings, sound refs, other entries) byte-identical.
usage: patch_tra.py <file.tra> <replacements.json>   (json: {"<id>": "<text>"})"""
import sys, re, json

path, rep_path = sys.argv[1:3]
rep = {int(k): v for k, v in json.load(open(rep_path, encoding='utf-8')).items()}
raw = open(path, 'rb').read()
crlf = b'\r\n' in raw
t = raw.decode('utf-8')
ENTRY = re.compile(r'(@(\d+)\s*=\s*)(~~~~~.*?~~~~~|~.*?~|".*?"|%.*?%)', re.S)

def delim(s):
    for o, c in (('~', '~'), ('"', '"'), ('%', '%'), ('~~~~~', '~~~~~')):
        if o not in s:
            return o + s + c
    raise ValueError('cannot delimit: ' + s[:50])

done = set()
def sub(m):
    i = int(m.group(2))
    if i not in rep:
        return m.group(0)
    done.add(i)
    s = rep[i].replace('\r\n', '\n')
    if crlf:
        s = s.replace('\n', '\r\n')
    return m.group(1) + delim(s)

out = ENTRY.sub(sub, t)
missing = set(rep) - done
assert not missing, sorted(missing)[:10]
open(path, 'wb').write(out.encode('utf-8'))
print(f'{path}: replaced {len(done)} entries')
