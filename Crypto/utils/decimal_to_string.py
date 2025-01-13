def decimal_to_string(text):
  return ''.join(chr(int(c)) for c in text)

cipher_text = [67, 84, 70, 123, 83, 116, 97, 114, 95, 46, 95, 87, 97, 114, 115, 95, 46, 95, 70, 111, 114, 95, 46, 95, 76, 105, 102, 101, 125]
print(cipher_text)

plain_text = decimal_to_string(cipher_text)
print(plain_text)