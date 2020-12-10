
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
def d2p1(lines):
  sum = 0
  for l in lines:
    data = l.replace(":","").split(" ")
    data_ns = list(map(int, data[0].split("-")))
    data_c = data[1]
    data_w = data[2]
    occurences = data_w.count(data_c)
    check_occurences = (occurences >= data_ns[0]) and \
                       (occurences <= data_ns[1])
    sum += check_occurences
  return sum

@timer
def d2p2(lines):
  sum = 0
  for l in lines:
    data = l.replace(":","").split(" ")
    data_ns = list(map(int, data[0].split("-")))
    data_c  = data[1]
    data_w  = data[2]
    check_index = (data_w[data_ns[0]-1] == data_c) ^ \
                  (data_w[data_ns[1]-1] == data_c)
    sum += check_index
  return sum

with open("input.txt", "r") as f:
  data = f.readlines()
  # Run challenges
  d2p1(data)
  d2p2(data)
