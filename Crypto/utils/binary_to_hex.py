def binary_to_hex(text):
  return ''.join(hex(int(text[i * 8: (i + 1) * 8], 2))[2:].upper() for i in range(len(text) // 8))

cipher_text = "01000001 01000010 01000011 01010100 01000110 01111011 00110100 00110101 01000011 00110001 00110001 01011111 00110001 00110101 01011111 01010101 00110101 00110011 01000110 01010101 01001100 01111101"
print(cipher_text)
cipher_text = ''.join(cipher_text.split())

plain_text = binary_to_hex(cipher_text)
print(plain_text)