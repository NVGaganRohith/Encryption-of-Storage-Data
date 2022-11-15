import hashlib
m = hashlib.sha512()
def sha(txt):
    m.update(txt)
    return m.digest()