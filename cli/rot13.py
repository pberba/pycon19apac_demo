#! /usr/bin/python

import sys
import json

def rot13(ciphertext):
    plaintext = []
    for e in ciphertext:
        if not e.isalpha():
            plaintext.append(e)
        elif e.islower():
            plaintext.append(chr((ord(e) - ord('a') + 13)%26 + ord('a')))
        else:
            plaintext.append(chr((ord(e) - ord('A') + 13)%26 + ord('A')))
    return ''.join(plaintext)

if __name__ == '__main__':
    print(rot13(sys.stdin.read()))
