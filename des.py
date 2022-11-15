from Crypto.Cipher import DES

def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)

# key = b'hello123'
# text1 = b'Python is the Best Language!'
def DesEncrryption(text,key):

    des = DES.new(key, DES.MODE_ECB)

    padded_text = pad(text)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def DesDecryption(cipher,key):
    des = DES.new(key, DES.MODE_ECB)
    descryptedText = des.decrypt(cipher)
    return descryptedText

# ctp=DesEncrryption(text1,key)
# print(ctp)
# pt=Desdecryption(ctp,key)
# print(pt)
