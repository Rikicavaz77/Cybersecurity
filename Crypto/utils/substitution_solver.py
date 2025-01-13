def substitution_solver(text):
  decryption_table = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "oscjwunbglaxqprvhiktzdmfey"
  )
  return text.translate(decryption_table)

cipher_text = r"KGBEYO: BNORTU{BQRGOK_TYGBYR_YPYOZEQYOY}"
print(cipher_text)

plain_text = substitution_solver(cipher_text)
print(plain_text)