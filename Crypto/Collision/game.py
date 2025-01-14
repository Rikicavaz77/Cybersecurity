import random
import datetime

#decrypt the following
ciphertext = "SU[@TYWFSB;qnaq`Vfijmczchfw:>3:w7{"

def XOR(text, seed):
    #set the seed to allow reproducibility
    random.seed(seed)
    return ''.join([chr(ord(x)^random.randint(0,10)) for x in text])

def h(x, y = 123):
    z = x
    while z >= y:
        z = z - y
    return z

def encrypt(text):
    year = datetime.date.today().year
    cipher = XOR(text, h(year))
    return cipher

def decrypt(text, seed):
    if seed <=10000:
        raise Exception(f"Not so easy! The value {seed} cannot be accepted")

    plaintext = XOR(text, h(seed))
    return plaintext

"""year = datetime.date.today().year
original_seed = year - 123 * (year // 123)
z = original_seed
while z < 10000:
    z = z + 123
seed = z
print(seed)

year = datetime.date.today().year
original_seed = year - 123 * (year // 123)
offset = (10000 - original_seed) // 123 + 1
seed = original_seed + (123 * offset)
print(seed)"""

year = datetime.date.today().year
offset = (10000 - year) // 123 + 1
seed = year + (123 * offset)
print(seed)

flag = decrypt(ciphertext, seed)
print(flag)





