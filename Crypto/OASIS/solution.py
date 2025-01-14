from collections import Counter
import string

with open("ciphertext.txt", "r") as file:
  cipher_text = file.read().lower()

  freq = Counter(cipher_text.split())
  freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  print(freq_sorted)

  print(cipher_text)

  freq = Counter(cipher_text)
  freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  print(freq_sorted)

  decryption_dict = {
    # I'M
    'a': 'i',
    'b': 'm',
    # A
    't': 'a',
    # IT
    'g': 's',
    'h': 't',
    # IN
    'm': 'n',
    # THE
    'v': 'h',
    'i': 'e',
    # SUMMERTINE
    'r': 'u',
    'n': 'r',
    # SAID
    'y': 'd',
    # GUESS
    'l': 'g',
    # CAN'T
    'z': 'c',
    # IF
    'w': 'f',
    # WAITING
    'k': 'w',
    # MORE
    'd': 'o',
    # JUST
    's': 'j',
    # I'LL
    'p': 'l',
    # BE
    'j': 'b',
    # MY
    'u': 'y',
    # CRAZY
    'c': 'z',
    # GIVE
    'o': 'v',
    # STOP
    'e': 'p',
    # BLACK
    'f': 'k',
  }

  flag = ''.join(decryption_dict.get(c, c) for c in cipher_text)
  print(flag)

  freq = Counter(flag.split())
  freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  print(freq_sorted)

  alphabet = list(string.ascii_lowercase)
  is_alphabet_complete = True
  
  for a in alphabet:
    if a not in decryption_dict:
      print(a)
      is_alphabet_complete = False
    
  print(is_alphabet_complete)

  for a in alphabet:
    if a in decryption_dict:
      print(decryption_dict.get(a,a).upper(), end='')