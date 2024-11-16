#!/usr/bin/env python3

import base64
from collections import Counter
import string

def binary_to_string(text):
    return ''.join(chr(int(c, 2)) for c in text)

def base64_decode(text):
    return base64.b64decode(text).decode('utf-8', errors='ignore')

def replace_chars(text, dict):
    return ''.join(dict.get(c, c) for c in text)

def get_sorted_freq(text):
    freq = Counter(text)
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

with open("ciphertext.txt", "r") as file:
    cipher_text = file.read().strip()
    file.close()
    print(f"Cipher text:\n{cipher_text}", end='\n\n')
    
    cipher_text = replace_chars(cipher_text, {
        "Z": "0",
        "O": "1",
    })
    print(cipher_text, end='\n\n')

    cipher_text = binary_to_string(cipher_text.split())
    print(cipher_text)
    
    w = len(cipher_text)
    print(f"Length of text: {w}")
    print(f"Multiple of 4: {w % 4 == 0}", end='\n\n')
    decoded = base64_decode(cipher_text)
    print(decoded)

    sorted_freq = get_sorted_freq(decoded)
    print(sorted_freq)

    # Step by step manual construction of the substitution dictionary
    decryption_dictionary = {
        # I'M
        'R': 'i',
        'W': 'm',
        # SPRITZ
        'B': 's',
        'N': 'p',
        'O': 'r',
        'T': 't',
        'U': 'z',
        # THIS
        'Q': 'h',
        # THAT
        'K': 'a',
        # ALL
        'J': 'l',
        # YOU
        'Z': 'y',
        'A': 'o',
        'F': 'u',
        # THE
        'Y': 'e',
        # EXPLAIN
        'L': 'x',
        'G': 'n',
        # THINK
        'S': 'k',
        # DO
        'V': 'd',
        # WHAT
        'E': 'w',
        # DOING
        'I': 'g',
        # PROTECT
        'C': 'c',
        # JUSTICE
        'D': 'j',
        # VENGEANCE
        'P': 'v',
        # DOUBT
        'H': 'b',
        # FULFILL
        'X': 'f',
    }

    flag = replace_chars(decoded, decryption_dictionary)
    print(flag)

    sorted_freq = get_sorted_freq(flag.split())
    print(sorted_freq, end='\n\n')

    alphabet = list(string.ascii_uppercase)
    is_alphabet_complete = True
    for a in alphabet:
        if a not in decryption_dictionary:
            print(a)
            is_alphabet_complete = False
    print(f"Alphabet complete: {is_alphabet_complete}")