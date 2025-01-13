with open('CTF_1.pdf', 'rb') as f:
  input1 = f.read()

with open('CTF_2.txt', 'rb') as f1:
  input2 = f1.read()
  
  flag = bytes([c ^ k for c, k in zip(input1, input2)])
  print(flag)

with open('output.pdf', 'wb') as f2:
    f2.write(flag)