#! /usr/bin/python

import sys
import json
import subprocess

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

def pop_up(title, body):
    subprocess.call(['notify-send', title, body])

if __name__ == '__main__':
    data = subprocess.check_output('xsel')
    output = rot13(data)
    pop_up('ROT13', output)
