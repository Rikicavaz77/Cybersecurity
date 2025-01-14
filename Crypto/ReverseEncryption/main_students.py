import random

def transformation(input):
    input = list(input)
    input.append(input[0])
    input.pop(0)
    return "".join(input)

def reversed_tranformation(input):
    input = list(input)
    input.insert(0, input[-1])
    # default pos is -1, which returns the last item
    input.pop()
    return "".join(input)

def encrypt(input, seed):
    input = transformation(input)
    input = list(input)
    random.seed(seed)
    input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    input = "".join(input)
    return input

def decrypt(input, seed):
    input = list(input)
    random.seed(seed)
    input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    input = "".join(input)
    input = reversed_tranformation(input)
    return input

with open("secret.txt", "r") as file:
    cipher = ''.join(file.readlines())
    print(cipher)

    for seed in range(1, 1000):
        plaintext = decrypt(cipher, seed)
        print(f"Seed {seed}: {plaintext}")

        if "spritz" in plaintext:
            break
        