#!/usr/bin/python3
import os
import binascii
import random
import sys

#Modified encrypt_otp for decrypting the ciphertext
def decrypt_otp(bytesStr,byteskey):
    out = []
    for i in range(0, len(bytesStr)):
        out.append(bytesStr[i] ^ byteskey[i % len(byteskey)])
    return bytes(out)

fullStr=""
M = "The following encoded individuals are to be given a $27.3k bonus"

with open(sys.argv[1],'r') as fd:
    fdRead = fd.readlines()
    for i in fdRead:
        fullStr+=i.strip()
bytesStr = binascii.unhexlify(fullStr)
first64 = bytesStr[0:64] # First 64 bytes of the ciphertext
byteskey = M.encode('utf-8')
#Xor the key(Known message) and the first 64 bytes of hte ciphertext
otpRet = decrypt_otp(first64,byteskey)
#Use the returned OTP to decypt the entire message
decrypted = decrypt_otp(bytesStr,otpRet)
print(decrypted)
