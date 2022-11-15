from Crypto.Cipher import AES
# key = b'Sixteen byte key'
# text = b'Y MQDTUHUT BEDUBO QI Q SBEKT JXQJ VBEQJI ED.'
def AESEncryption(text,key):
    cipher = AES.new(key, AES.MODE_EAX)

    # data to be encrypted
    # data = "Welcome to copyassignment.com!".encode()


    # encrypt the data
    ciphertext = cipher.encrypt(text)

    # print the encrypted data
    # print("Cipher text:", ciphertext)

    return cipher,ciphertext

# datec=AESEncryption(text,key)
# print(datec)
def AESDEcryption(ctext,key,cipher):
    nonce = cipher.nonce
    cipher =  AES.new(key, AES.MODE_EAX, nonce)
    # decrypt the data
    plaintext = cipher.decrypt(ctext)
    # print("Plain text:", plaintext.decode())
    return plaintext.decode()
# AESDEcryption(datec[1],key,datec[0])