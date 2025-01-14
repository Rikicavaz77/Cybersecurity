#!/usr/bin/env python3
import random
import sys
import time

"""cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

msg = input('Your message: ').encode('ASCII')
key = [random.randrange(256) for _ in msg]
c = [m ^ k for (m, k) in zip(msg + cur_time, key + [0x88]*len(cur_time))]

with open(sys.argv[1], "wb") as f:
    f.write(bytes(c))"""

with open('top_secret', 'rb') as f:
  cipher_text = f.read()
  print(cipher_text)
  
  for i in range(16, 20):
    cur_time_length = i

    cur_time = [chr(m ^ k) for (m, k) in zip(cipher_text[-cur_time_length:], [0x88]*cur_time_length)]
    cur_time = ''.join(cur_time).encode('ASCII')
    print(cur_time)
    random.seed(cur_time)

    key = [random.randrange(256) for _ in range(len(cipher_text) - cur_time_length)]
    
    flag = ''.join(chr(m ^ k) for (m, k) in zip(cipher_text[:-cur_time_length], key))
    print(flag)

    if "flag" in flag:
      break
    