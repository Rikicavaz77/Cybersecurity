import base64
import binascii

def base64_decode(text):
    return base64.b64decode(text).decode('utf-8', errors='ignore')

with open('flag.txt', 'r') as f:
  encrypted_message = f.read()
  print(encrypted_message)

  decoded = encrypted_message
  for i in range(50):
    try:
      decoded = base64_decode(decoded)
      print(f"Step {i}:\n{decoded}")
    except binascii.Error:
      break