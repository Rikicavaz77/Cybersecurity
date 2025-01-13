import itertools

KEY_LENGTH = 26

def repeated_key_xor(text, key):
  return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, itertools.cycle(key)))

def hex_to_string(text):
  return ''.join(chr(int(text[i * 2 : (i + 1) * 2], 16)) for i in range(len(text) // 2))

def find_plain_text(text, key):
  for i in range(len(text)):
    plain_text = repeated_key_xor(text[i : i + len(key)], key)
    if i % KEY_LENGTH == 0:
      print(f"Step {i}: {plain_text}")

def find_key(text, plain_text):
  for i in range(len(text)):
    key = repeated_key_xor(text[i : i + len(plain_text)], plain_text)

    if "ALEXCTF" in key:
      print(key)

with open('encrypted', 'r') as f:
  encrypted_message = f.read()
  print(encrypted_message)
  encrypted_message = ''.join(encrypted_message.split("\n"))
    
  decoded = hex_to_string(encrypted_message)
  print(decoded)

  key = "ALEXCTF{"
  plain_text = repeated_key_xor(decoded, key)
  print(plain_text)

  find_plain_text(decoded, key)
  find_key(decoded, "agree with me ")

  key = r"ALEXCTF{HERE_"
  plain_text = repeated_key_xor(decoded, key)
  print(plain_text)

  find_plain_text(decoded, key)
  find_key(decoded, "encryption scheme")
  find_key(decoded, "secure, Let Me know")
  
  key = r"ALEXCTF{HERE_GOES_THE_KEY}"
  plain_text = repeated_key_xor(decoded, key)
  print(plain_text)
        