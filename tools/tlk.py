"""TLK V1 reader/writer and WeiDU .tra parser (shared by the other tools)."""
import struct, re, sys

def read_tlk(path):
    d = open(path, 'rb').read()
    assert d[:8] == b'TLK V1  '
    lang, n, off = struct.unpack_from('<HII', d, 8)
    entries = []
    for i in range(n):
        flags, snd, vol, pitch, o, ln = struct.unpack_from('<H8sIIII', d, 18 + 26 * i)
        txt = d[off + o: off + o + ln]
        entries.append([flags, snd, vol, pitch, txt])
    return lang, entries

def write_tlk(path, lang, entries):
    hdr = bytearray(b'TLK V1  ' + struct.pack('<HII', lang, len(entries), 18 + 26 * len(entries)))
    body = bytearray()
    for flags, snd, vol, pitch, txt in entries:
        hdr += struct.pack('<H8sIIII', flags, snd, vol, pitch, len(body), len(txt))
        body += txt
    open(path, 'wb').write(bytes(hdr + body))

TRA_RE = re.compile(r'@(\d+)\s*=\s*(?:~~~~~(.*?)~~~~~|~(.*?)~|"(.*?)"|%(.*?)%)(?:[ 	]*\[([^\]]*)\])?', re.S)

def read_tra(path):
    t = open(path, encoding='utf-8-sig').read().replace('\r\n', '\n')
    res = {}
    for m in TRA_RE.finditer(t):
        txt = next(g for g in m.group(2,3,4,5) if g is not None)
        res[int(m.group(1))] = (txt, m.group(6))
    return res
