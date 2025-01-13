qwerty_keyboard_lower = [
  ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
  ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']'],
  ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", '\\'],
  ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '\\'],
]
qwerty_keyboard_upper = [
  ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'],
  ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|'],
  ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"'],
  ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
]

def find_row(c):
  for row_lower, row_upper in zip(qwerty_keyboard_lower, qwerty_keyboard_upper):
    if c in row_lower:
      return row_lower
    elif c in row_upper:
      return row_upper
  return None

def keyboard_shift_cipher_decoder(text, shift):
  decoded = ""
  for c in text:
    row = find_row(c)
    if row is not None:
      decoded += row[(row.index(c) - shift) % len(row)]
  return decoded

encrypted_message = "BUH'tdy,|Bim5y~Bdt76yQ"

for i in range(5):
  flag = keyboard_shift_cipher_decoder(encrypted_message, i)
  print(f"Step {i}:\n{flag}")

  if "CTF" in flag:
    break


