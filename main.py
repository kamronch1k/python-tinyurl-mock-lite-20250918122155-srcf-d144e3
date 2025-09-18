import hashlib
s='liteabbos'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
