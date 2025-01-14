import base64

def decode_b64(text):
    return base64.b64decode(text).decode('utf-8', errors='ignore')

original_data = "El Psy Congroo"
encrypted_data = "IFhiPhZNYi0KWiUcCls="
encrypted_flag = "I3gDKVh1Lh4EVyMDBFo="

encrypted_data = decode_b64(encrypted_data)
encrypted_flag = decode_b64(encrypted_flag)

key = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(original_data, encrypted_data)])
print(key)

flag = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(encrypted_flag, key)])
print(flag)