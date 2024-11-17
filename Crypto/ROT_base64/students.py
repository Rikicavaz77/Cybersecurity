import base64
import string

ALPHABET = list(string.printable)  
LEN = len(ALPHABET)

def decrypt_rotation_cipher(text, shift):
    result = ''
    for c in text:
        result += ALPHABET[(ALPHABET.index(c) - shift) % LEN]
    return result

def base64_to_string(text):
    return base64.b64decode(text).decode('utf-8', errors='ignore')

with open('encrypted_flag.txt', 'r') as f:
    encrypted_message=f.read()
    f.close()
    print(f"Cipher text:\n{encrypted_message}", end='\n\n')

    first_step = decrypt_rotation_cipher(encrypted_message, 13)
    print(first_step, end='\n\n')

    w = len(first_step)
    print(f"Length of text: {w}")
    print(f"Multiple of 4: {w % 4 == 0}", end='\n\n')
    flag = base64_to_string(first_step)
    print(flag)
    