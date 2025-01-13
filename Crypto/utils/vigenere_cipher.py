def vigenere_cipher_decoder(encrypted_message, key):
  decoded = ""
  i = 0
  for c in encrypted_message:
    if c.isalpha():
      offset = 97 if c.islower() else 65
      k = ord(key[i % len(key)].lower()) - 97
      decoded += chr((ord(c) - k - offset) % 26 + offset)
      i += 1
    else:
      decoded += c
  return decoded

key = "blorpy"
encrypted_message = r"gwox{RgqssihYspOntqpxs}"

flag = vigenere_cipher_decoder(encrypted_message, key)
print(flag)
