import hashlib
m = hashlib.sha512()
#plain text goes into this m.update command
def sha(txt):
    # enTxt=txt.encode()
    # print("\n\n\n Sha is \n\n",txt)
    m.update(txt)
    # m.update(b" the spammish repetition")
    return m.digest()

