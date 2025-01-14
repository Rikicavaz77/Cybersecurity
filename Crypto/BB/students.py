import numpy as np

def keygen():
    key = np.random.randint(size = 1, low = 0, high = 100000000)[0]
    return key

def mixer(message, key):
    np.random.seed(key)
    code = np.random.randint(size = 1, low = 50, high = 100)[0]
    return ''.join([chr(ord(x) ^ code) for x in message])

with open("message.txt", "r") as file:
    cipher = file.read()
    print(cipher)

    """for code in range(50, 100):
        flag = ''.join([chr(ord(x) ^ code) for x in cipher])
        print(flag)

        if "spritzCTF{" in flag:
            break"""

    for key in range(128):
        flag = mixer(cipher, key)
        print(f"Key: {key}\n{flag}")

        if "spritzCTF{" in flag:
            break

