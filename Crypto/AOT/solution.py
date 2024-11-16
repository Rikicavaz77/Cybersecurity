def f(x):
  return x % 731

def mixer(message, x1, x2, x3):
  assert x1 != x2
  assert x1 != x3
  assert x2 != x3
  assert x1 != (x2 + x3)
  anonym1 = f(x1)
  anonym2 = f(x2 + x3)
  assert anonym1 == anonym2
  mix = "".join([chr(ord(x) ^ x1) for x in message])
  return mix

with open("message.txt", "rb") as file:
  cipher = file.read().decode('utf-8', errors='ignore')
  file.close()
  print(f"Cipher text:\n{cipher}")

  for i in range(1, 128):
    flag = mixer(cipher, i, 0, 731 + i)

    if "spritzCTF{" in flag:
      print(f"Step {i}:\n{flag}")
      break