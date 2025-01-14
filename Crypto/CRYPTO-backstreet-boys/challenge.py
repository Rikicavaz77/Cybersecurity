#!/usr/bin/env python3

# encryption method
def encryption(plain_text, key):
    encrypted_text = ""
    key_extended = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]

    for i in range(len(plain_text)):
        char_plain = plain_text[i]
        char_key = key_extended[i]

        offset = 97

        if char_plain.isalpha():
            # here is the most important part
            encrypted_char = chr((ord(char_plain) + ord(char_key) - 2 * offset)   % 26 + offset)
            
            encrypted_text += encrypted_char
        else:
            encrypted_text += char_plain

    return encrypted_text

def decryption(cipher_text, key):
    plain_text = ""
    key_extended = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]

    for i in range(len(cipher_text)):
        encrypted_char = cipher_text[i]
        char_key = key_extended[i]

        offset = 97

        if encrypted_char.isalpha():
            decrypted_char = chr((ord(encrypted_char) - ord(char_key)) % 26 + offset)

            plain_text += decrypted_char
        else:
            plain_text += encrypted_char

    return plain_text

# key for the encryption
k = "tellmewhy"

# this is my message
flag = '??????????????????????????'
        
cipher_text = "ltctfd{p-peye-mp-raee-ieu}"
flag = decryption(cipher_text, k)
print(flag)
