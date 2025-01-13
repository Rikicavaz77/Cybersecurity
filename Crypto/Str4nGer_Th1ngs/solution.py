import base64
import string
import urllib.parse
from re import findall

def get_morse_code_dict():
  return {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
  }

def morse_decode(text):
  morse_code_dict = { value: key for (key, value) in get_morse_code_dict().items() }
  return ''.join(morse_code_dict.get(c, c) for c in text.split())

def base64_decode(text):
  return base64.b64decode(text).decode('utf-8', errors='ignore')

def hex_to_string(text):
  return ''.join(chr(int(text[i * 2 : (i + 1) * 2], 16)) for i in range(len(text) // 2))

def substitution_solver(text):
  decryption_table = str.maketrans(
    string.ascii_lowercase,
    "nopxrstuvwzyjabcdefghiqklm"
  )
  return text.lower().translate(decryption_table)

with open('cyphertext.txt', 'r') as file:
  cipher_text = file.read().strip()
  file.close()
  print(f"Cipher text:\n{cipher_text}", end='\n\n')

  blocks = cipher_text.split("\n")
  first_block = blocks[0]
  second_block = blocks[1]

  first_step = morse_decode(first_block)
  print(first_step, end='\n\n')

  w = len(second_block)
  print(f"Length of second block: {w}")
  print(f"Multiple of 4: {w % 4 == 0}", end='\n\n')
  second_step = base64_decode(second_block)
  print(second_step, end='\n\n')

  mini_blocks = second_step.split("\n\n")
  first_mini_block = mini_blocks[0]
  second_mini_block = mini_blocks[1]
  third_mini_block = mini_blocks[2]

  third_step = substitution_solver(first_mini_block)
  print(third_step, end='\n\n')

  fourth_step = urllib.parse.unquote(second_mini_block)
  print(fourth_step, end='\n\n')

  coordinates = ' '.join(fourth_step.split()[:2])
  print(f"Coordinates: {coordinates}", end='\n\n')
  
  encrypted_flag = ' '.join(fourth_step.split()[2:])
  print(encrypted_flag)
  encrypted_flag = findall(r"\d+|[ {’}]", encrypted_flag)
  alphabet = list(string.ascii_lowercase)
  #decryption_dict = { str(alphabet.index(c) + 1): c for c in alphabet }
  #flag = ''.join(decryption_dict.get(c, c) for c in encrypted_flag)
  flag = ''.join(alphabet[int(c) - 1] if c.isdigit() else c for c in encrypted_flag)
  print(f"Flag: {flag}", end='\n\n')

  fifth_step = hex_to_string(third_mini_block)
  print(fifth_step, end='\n\n')
  fifth_step = fifth_step[::-1]
  print(fifth_step)
