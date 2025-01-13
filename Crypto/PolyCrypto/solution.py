import re

def binary_to_hex(text):
  return ''.join(hex(int(text[i * 8: (i + 1) * 8], 2))[2:].upper() for i in range(len(text) // 8))

def hex_to_string(text):
  return ''.join(chr(int(text[i * 2 : (i + 1) * 2], 16)) for i in range(len(text) // 2))

def poly_to_binary(text):
  text = re.sub(r"(?<!x\^)\d+$", "x^0", text)
  poly_exp = re.findall(r"x\^(\d+)", text)
  max_degree = int(poly_exp[0])
  decoded = ''.join('1' if str(i) in poly_exp else '0' for i in range(max_degree, -1, -1))
  return decoded.zfill((len(decoded) + 7) // 8 * 8)

with open('encrypted.txt', 'r') as f:
  encrypted_message = f.read()
  print(encrypted_message)

  decoded = poly_to_binary(encrypted_message)
  print(decoded)

  decoded = binary_to_hex(decoded)
  print(decoded)

  flag = hex_to_string(decoded)
  print(flag)