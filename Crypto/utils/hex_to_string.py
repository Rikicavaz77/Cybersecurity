def hex_to_string(text):
  return ''.join(chr(int(text[i * 2 : (i + 1) * 2], 16)) for i in range(len(text) // 2))

cipher_text = "73707269747A7B73316D706C335F6833785F336E633064316E677D"
print(cipher_text)

plain_text = hex_to_string(cipher_text)
print(plain_text)