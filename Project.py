# from CeasseEncrypt import *
# from CeaserDecrypt import *
# import imp
# from pydoc import plain
# from getpass import getpass

from Ceaser import *
from Vigenère import *
from AES import *
from DES import *

# PlainText = input("Enter the plain Text: ")
# CeaserCipherKey = input("Enter the CeaserCipherKey: ")
# VignerCipherKey = input("Enter the CeaserCipherKey: ")
# DesCipherKey = input("Enter the CeaserCipherKey: ")
# AESCipherKey = input("Enter the Key: ")
# For secret input
# password = getpass()

PlainText = "I wandered lonely as a cloud That floats on."

VignerCipherKey = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"

DesCipherKey = b'hello123'

AESCipherKey = b'Sixteen byte key'

CeaserCipherKey = len(VignerCipherKey)//3

# Step 1 Ceaser Cipher encryption

CeaserEncryptedText =  CeaserEncrypt(PlainText,CeaserCipherKey)
print("\n")
print("---------------  ENCRYPTION  ---------------")
print("\n")
print("Plain Text after Ceaser Cipher Encryption : \n")
print(CeaserEncryptedText)
print("\n")

# Step 2 AES encryption

AesEncrypttedText=AESEncryption(CeaserEncryptedText.encode(),AESCipherKey)
print("Encrypted Plain Text obatined after AES encryption : \n")
print(AesEncrypttedText[1])
print("\n")

# Step 3 for key Encryption using Vigenere

dec=vigenere_encrypt(AESCipherKey.decode(),VignerCipherKey)
print("Key after Vigenere Encryption: \n")
print(dec)
print("\n")

# Step 4 for key Encryption using DES

dest =DesEncrryption(dec.encode(),DesCipherKey)
print("Key obtained from DES Encryption: \n")
print(dest)
print("\n")

print("---------------  DECRYPTION  ---------------")
print("\n")
# Step 1 Decrypting received Plain text using AES

AesDecrypttedText = AESDEcryption(AesEncrypttedText[1],AESCipherKey,AesEncrypttedText[0])

print("Decrypting received Plain text using AES: \n")
print(AesDecrypttedText)
print("\n")

# Step 2 Decrypting output of AES with ceaser

CeaserDecryptedText = CeaserCipherDecrypt(AesDecrypttedText,CeaserCipherKey)
print("Original Plain Text: \n")
print(CeaserDecryptedText)
print("\n")

# Step 3 for key Decrypt using DES

print("Decrypting Key using DES: \n")
dest1 =DesDecryption(dest,DesCipherKey)
print(dest1)
print("\n")

# Step 4 for key Decryption of output of DES with vigenere

print("Secret Key: \n")
dectxt=vigenere_decrypt(dest1.decode(),VignerCipherKey)
print(dectxt)
