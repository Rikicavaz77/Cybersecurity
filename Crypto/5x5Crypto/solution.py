import string

alphabet = [c for c in string.ascii_uppercase if c != 'K']
row = 5
column = 5

def get_decryption_table():
  decryption_table = [[0 for _ in range(row)] for _ in range(column)]
  for i in range(row):
    for j in range(column):
      decryption_table[i][j] = alphabet[i * 5 + j]
  return decryption_table

encrypted_message = "1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}"

decryption_table = get_decryption_table()
print(decryption_table)

encrypted_message = encrypted_message.split(",")
flag = ""
for c in encrypted_message:
  k = c.split("-")
  if len(k) == 2:
    row = int(k[0])
    column = int(k[1])
    flag += decryption_table[row - 1][column - 1]
  else:
    flag += k[0]
  
print(flag)


