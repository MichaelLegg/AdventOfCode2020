
import pdb

def timer(func):
  import time
  import functools
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    ts = time.perf_counter()
    val = func(*args, **kwargs)
    te = time.perf_counter()
    rt = te - ts
    print(f"Finished {func.__name__:<10} {rt:.8f}s = {val}")
    return val
  return wrapper

import re
@timer
def d14p1(data):
  data = data.split("\n")
  mem = {}
  for line in data:
    if line[:4] == 'mask':
      mask = line[7:]
      mask_keep_1 = int(mask.replace('X','0'),2)
      mask_keep_0 = int(mask.replace('1','X').replace('0','1').replace('X','0'),2)
    elif line[:3] == 'mem':
      m = re.match('mem\[(\d+)\] = (\d+)', line)
      addr = int(m.group(1))
      value = int(m.group(2))
      value |= mask_keep_1
      value &= ~mask_keep_0
      mem[addr] = value
  return sum(mem.values())

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d14p1(data)
