def caesar_cipher_encoder(plain_text, shift):
    result = ''
    for c in plain_text:
        if c.isalpha():     # check if the character is a letter
            offset = 65 if c.isupper() else 97
            # - offset: normalizes the position of alphabetic characters in the range 0-25
            result += chr((ord(c) - offset + shift) % 26 + offset)
        else:
            result += c
    return result

def caesar_cipher_decoder(cipher_text, shift):
    result = ''
    for c in cipher_text:
        if c.isalpha():     # check if the character is a letter
            offset = 65 if c.isupper() else 97
            # - offset: normalizes the position of alphabetic characters in the range 0-25
            result += chr((ord(c) - offset - shift) % 26 + offset)
        else:
            result += c
    return result

input = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"

for i in range(1, 26):
    decoded = caesar_cipher_decoder(input, i)
    print(f"Step={i}\t{decoded}")