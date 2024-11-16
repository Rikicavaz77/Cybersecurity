#!/usr/bin/env python3

import string
import itertools

XOR_KEY = '??' # can be only letters
POSSIBLE_KEYS = [''.join(pair) for pair in list(itertools.permutations(string.ascii_letters, 2))]

# read the file with the encrypted message
with open('encrypted', 'rb') as f:
    encrypted_message = f.read().decode('utf-8', errors='ignore')
    f.close()
    print(f"Cipher text:\n{encrypted_message}", end='\n\n')

    for key in POSSIBLE_KEYS:
        flag = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted_message, itertools.cycle(key)))

        if "spritz" in flag:
            print(f"Key: {key}\n{flag}")
            break
    
