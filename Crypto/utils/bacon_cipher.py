def get_baconian_code_dict():
  return {
    "A": "aaaaa",
    "B": "aaaab",
    "C": "aaaba",
    "D": "aaabb",
    "E": "aabaa",
    "F": "aabab",
    "G": "aabba",
    "H": "aabbb",
    "I": "abaaa",
    "J": "abaaa",
    "K": "abaab",
    "L": "ababa",
    "M": "ababb",
    "N": "abbaa",
    "O": "abbab",
    "P": "abbba",
    "Q": "abbbb",
    "R": "baaaa",
    "S": "baaab",
    "T": "baaba",
    "U": "baabb",
    "V": "baabb",
    "W": "babaa",
    "X": "babab",
    "Y": "babba",
    "Z": "babbb"
  }

def bacon_cipher_decoder(text):
  baconian_code_dict = { value: key for (key, value) in get_baconian_code_dict().items() }
  decoded = ''.join(baconian_code_dict.get(text[i * 5: (i + 1) * 5], "")  for i in range(len(text) // 5))
  return decoded.replace("J", "I").replace("V", "U")

encrypted_message = "ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB"

flag = bacon_cipher_decoder(encrypted_message.lower())
print(flag)
