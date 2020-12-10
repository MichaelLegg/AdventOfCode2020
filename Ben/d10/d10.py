
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
def d10p1(data):
  chargers = map(int, data.split("\n"))
  chargers = [0]+sorted(chargers)
  # store count of differences in dictionary
  diff_counters = {}
  for i in range(len(chargers)):
    cur = chargers[i]
    if i == len(chargers)-1: 
      continue
    nxt = chargers[i+1]
    diff = nxt-cur
    # incremnt counter for this difference
    if diff not in diff_counters:
      diff_counters[diff] = 0
    diff_counters[diff] += 1
  # our charger is always 3 + highest
  diff_counters[3] += 1
  return diff_counters[1]*diff_counters[3]

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d10p1(data)
