#!/usr/bin/env python3

import sys
import binascii
import requests
from Crypto.Cipher import AES
from string import printable

#https://crypto.stackexchange.com/questions/55673/why-is-byte-at-a-time-ecb-decryption-a-vulnerability

BLOCK_SIZE = 16

def blocks(arg):
    items = []
    for i in range(0,len(arg),BLOCK_SIZE):
        items.append(arg[i:i+BLOCK_SIZE])
    return items

def decrypt():
    index = 0
    key = b''
    while len(key)<=16:
        sentStr = b'A'*(15-index)
        ret = request(sentStr)
        retBlocks = blocks(ret)
        for i in printable:
            ibyte = str.encode(i)
            req = sentStr+key+ibyte
            
            guess = request(req)
            guessBlocks = blocks(guess)
            print(req)
            print('Wanted: ',retBlocks[0])
            print('Guess bytes: ',guessBlocks[0])
            if retBlocks[0]==guessBlocks[0]:
                key+=ibyte
                print("The Key now is: ",key.decode('utf-8'))
                yield ibyte
                break
        
        print('Index change')
        index+=1

def request(user):
    request = requests.post('http://challenge.acictf.com:2338/register',data=dict(username=user,password='pass'))
    return binascii.unhexlify(request.headers['Set-Cookie'][len('auth_token='):].split(';')[0])

def main():
    key=b''
    for i in decrypt():
        key+=i
        print(key.decode('utf-8'))

main()
