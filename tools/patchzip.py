"""Replace entries in a STORED zip in place: append new local entries where the
central directory was, then write a fresh central directory + EOCD.
usage: patchzip.py <zip> <entry_name>=<file> [...]"""
import sys, struct, zlib, os

zpath = sys.argv[1]
repl = dict(a.split('=', 1) for a in sys.argv[2:])

with open(zpath, 'r+b') as f:
    f.seek(0, 2); size = f.tell()
    f.seek(size - 22); eocd = f.read(22)
    sig, disk, cddisk, n1, n, cdsize, cdoff, clen = struct.unpack('<4s4H2IH', eocd)
    assert sig == b'PK\x05\x06' and clen == 0 and cdoff + cdsize == size - 22
    f.seek(cdoff); cd = f.read(cdsize)
    entries, p = [], 0
    for _ in range(n):
        assert cd[p:p + 4] == b'PK\x01\x02'
        fnl, exl, cml = struct.unpack_from('<3H', cd, p + 28)
        name = cd[p + 46:p + 46 + fnl].decode('cp437')
        entries.append([name, bytearray(cd[p:p + 46 + fnl + exl + cml])])
        p += 46 + fnl + exl + cml
    junk = cd[p:]  # trailing stale records after the real directory; preserved as-is
    names = {e[0] for e in entries}
    missing = set(repl) - names
    assert not missing, missing

    f.seek(cdoff); f.truncate()
    pos = cdoff
    for name, rec in entries:
        if name not in repl:
            continue
        data = open(repl[name], 'rb').read()
        crc = zlib.crc32(data) & 0xffffffff
        method, mtime, mdate = struct.unpack_from('<3H', rec, 10)
        assert method == 0
        nb = name.encode('cp437')
        lh = struct.pack('<4s5H3I2H', b'PK\x03\x04', 20, 0, 0, mtime, mdate, crc, len(data), len(data), len(nb), 0) + nb
        f.write(lh); f.write(data)
        struct.pack_into('<3I', rec, 16, crc, len(data), len(data))
        struct.pack_into('<I', rec, 42, pos)
        print('replaced', name, len(data), 'at', pos)
        pos += len(lh) + len(data)
    newcd = b''.join(bytes(r) for _, r in entries) + junk
    f.write(newcd)
    f.write(struct.pack('<4s4H2IH', b'PK\x05\x06', 0, 0, n, n, len(newcd), pos, 0))
print('done')
