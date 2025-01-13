import base64

def base64_decode(text):
    return base64.b64decode(text).decode('utf-8', errors='ignore')

def hex_to_string(text):
  return ''.join(chr(int(text[i * 2 : (i + 1) * 2], 16)) for i in range(len(text) // 2))

def binary_to_string(text):
  return ''.join(chr(int(text[i * 8: (i + 1) * 8], 2)) for i in range(len(text) // 8))

with open('encrypted.txt', 'r') as f:
  encrypted_message = f.read()
  print(encrypted_message)
  encrypted_message = encrypted_message.split()[-1]

  decoded = base64_decode(encrypted_message)
  print(decoded)
  decoded = decoded.split()[-1]

  decoded = hex_to_string(decoded)
  print(decoded)
  decoded = ''.join(decoded.split()[2:])

  decoded = binary_to_string(decoded)
  print(decoded)
  decoded = decoded.split()[-1]

  flag = base64_decode(decoded)
  print(flag)
