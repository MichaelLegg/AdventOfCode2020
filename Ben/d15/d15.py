
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

def nth_number(data, N):
  data = list(reversed(list(map(int, data.split(",")))))
  for i in range(len(data),N):
    last_number = data[0]
    try:
      last_occurence = data[1:].index(last_number) +1
    except:
      last_occurence = 0

    data.insert(0, last_occurence)
  return data[0]

@timer
def d15p1(data):
  return nth_number(data, 2020)

@timer
def d15p2(data):
  return nth_number(data, 30000000)

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d15p1(data)
  d15p2(data)
