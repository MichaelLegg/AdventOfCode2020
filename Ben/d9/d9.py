
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

@timer
def d9p1(data):
  numbers = list(map(int, data.split('\n')))
  data_ptr = 0
  N = 25
  while 1:
    last_n = numbers[data_ptr:data_ptr+N+1]
    target = numbers[data_ptr+N]
    found = False
    for i in last_n:
      if found: break
      for j in last_n:
        if found: break
        if i == j:
          continue
        if i+j == target:
          data_ptr += 1
          found = True
    if not found:
      return target
          
  return 0

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d9p1(data)
