from collections import Counter
import string

with open('challenge.txt', 'r') as file:
  cipher_text = file.read()

  freq = Counter(cipher_text.split())
  freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  print(freq_sorted)

  print(cipher_text)

  freq = Counter(cipher_text)
  freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  print(freq_sorted)

  decryption_dict = {
    # IT'S
    'X': 'i',
    'S': 't',
    'D': 's',
    # the
    'A': 'h',
    'L': 'e',
    # SO
    'E': 'o',
    # HAS
    'H': 'a',
    # PIRATES
    'M': 'p',
    'P': 'r',
    # HAD
    'Y': 'd',
    # NARRATOR
    'O': 'n',
    # SPOKE
    'Q': 'k',
    # POWER
    'C': 'w',
    # WORLD
    'U': 'l',
    # WEARING
    'W': 'g',
    # UPON
    'R': 'u',
    # JOURNEY
    'G': 'j',
    'N': 'y',
    # OF
    'V': 'f',
    # FAME
    'K': 'm',
    # BY
    'F': 'b',
    # DROVE
    'B': 'v',
    # COUNTLESS
    'Z': 'c',
    # SPRITZ
    'T': 'z'
  }

  flag = ''.join(decryption_dict.get(c, c) for c in cipher_text)
  print(flag)

  freq = Counter(flag.split())
  freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  print(freq_sorted)

  alphabet = list(string.ascii_uppercase)
  is_alphabet_complete = True

  for a in alphabet:
    if a not in decryption_dict:
      print(a)
      is_alphabet_complete = False
  
  print(is_alphabet_complete)
