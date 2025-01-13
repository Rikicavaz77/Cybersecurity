def substitution_solver(text):
  decryption_table = str.maketrans(
    "!@#$%^&*()",
    "1234567890"
  )
  return text.translate(decryption_table)

def decimal_to_string(text):
  return ''.join(chr(int(c)) for c in text)

encrypted_message = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"
print(encrypted_message)

decoded = substitution_solver(encrypted_message)
print(decoded)
decoded = decoded.split(",")

flag = decimal_to_string(decoded)
print(flag)