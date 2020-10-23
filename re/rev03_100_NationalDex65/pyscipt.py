#!/usr/bin/env python3
import sys
from Crypto.Cipher import Blowfish

with open(sys.argv[1],'rb') as f:
    cipher = f.read()

K = b'\x17\x6b\x7d\xc3\x4f\xf1\xe8\x08\x16\xfd\x83\x7c\xed\x6d\x1c\x60'
IV = b'\xbf\xa2\x13\xf4\x73\xd4\x7f\x8f'

cipher_little = Blowfish.new(K, Blowfish.MODE_CBC, IV)
P = cipher_little.decrypt(cipher)

print(P)
