import itertools

def repeated_key_xor(text, key):
  return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, itertools.cycle(key)))

encrypted_message = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"

plain_text = "ctflearn{"
key = []
for c, k in zip(encrypted_message, plain_text):
  key.append(chr(ord(c) ^ ord(k)))

print(key)

key = "jowls"
flag = repeated_key_xor(encrypted_message, key)
print(flag)