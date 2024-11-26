import pwn 

p = pwn.process("./CrossTheBridge")
p.sendline(b"Y")
p.sendline()
p.sendline(b"L\n" * 16)
p.interactive()