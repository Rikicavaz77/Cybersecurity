def binary_to_string(text):
  return ''.join(chr(int(c, 2)) for c in text.split())

ciphertext = "yxyxxyy yxyxxxx yxyxxyx yxxyxxy yxyxyxx yxyyxyx yxxxxyy yxyxyxx yxxxyyx yyyyxy yyyyxyy yyxxyxy yyxyyyx yyxxxyy yyyxxyx yyyyxxy yyyxxxx yyyxyxx yyxyxxy yyxyyyy yyxyyyx yyxxxx yyxxxx yyxxxx yyxxxx yyxxxx yyxxxy yyyyyxy"

ciphertext = ciphertext.replace("y", "1")
ciphertext = ciphertext.replace("x", "0")
print(ciphertext)

flag = binary_to_string(ciphertext)
print(flag)