import itertools

def repeated_key_xor(text, key):
  return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, itertools.cycle(key)))

encrypted_message = "q{vpln'bH_varHuebcrqxetrHOXEj"

for key in range(255):
  flag = repeated_key_xor(encrypted_message, chr(key))
  print(f"Key: {key}\n{flag}")

  if "flag" in flag:
    break

  