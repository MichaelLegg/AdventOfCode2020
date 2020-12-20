
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
def d15p1(data):
  data = list(reversed(list(map(int, data.split(",")))))
  for i in range(len(data),2020):
    last_number = data[0]
    try:
      last_occurence = data[1:].index(last_number) +1
    except:
      last_occurence = 0

    data.insert(0, last_occurence)
  return data[0]

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d15p1(data)
