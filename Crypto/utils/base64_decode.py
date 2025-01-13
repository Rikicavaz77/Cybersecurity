import base64

def base64_decode(text):
    return base64.b64decode(text).decode('utf-8', errors='ignore')

cipher_text = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"
print(cipher_text)

w = len(cipher_text)
print(f"Length of text: {w}")
print(f"Multiple of 4: {w % 4 == 0}", end='\n\n')

plain_text = base64_decode(cipher_text)
print(plain_text)