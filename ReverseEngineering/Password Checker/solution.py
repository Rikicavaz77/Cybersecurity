from pwn import *

def caesar_cipher_encoder(cipher_text, shift):
  result = ''
  for c in cipher_text:
    if c.isalpha():
      offset = 65 if c.isupper() else 97
      result += chr((ord(c) - offset + shift) % 26 + offset)
    else:
      result += c
  return result

context.binary = "./password_checker"
p = process()

plain_text = "passwd"
shift = 3
payload = caesar_cipher_encoder(plain_text, shift)
print(payload)

p.sendline(payload.encode())
p.interactive()