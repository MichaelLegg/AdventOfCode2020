
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
    # calculate joltage difference
    nxt = chargers[i+1]
    diff = nxt-cur
    # incremnt counter for this difference
    if diff not in diff_counters:
      diff_counters[diff] = 0
    diff_counters[diff] += 1
  # our charger is always 3 + highest
  diff_counters[3] += 1
  return diff_counters[1]*diff_counters[3]

mem = {}
def search(jolt, chargers, i):
  # find next possible chargers in the next 3 chargers
  next3 = chargers[i:i+3]
  possible = tuple(filter(lambda x: x <= jolt+3, next3))

  # See if already solved for these possible
  if possible in mem:
    return mem[possible]

  # if no possible next charger, we've reached the end
  if len(possible) == 0:
    return 1

  # for each possible charger, start a new search tree using it
  s = 0
  for pi in range(len(possible)):
    jolt_nxt = possible[pi]
    s += search(jolt_nxt, chargers, i+pi+1)

  # store result
  mem[possible] = s
  return s

@timer
def d10p2(data):
  chargers = map(int, data.split("\n"))
  chargers = sorted(chargers)
  return search(0, chargers, 0)

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d10p1(data)
  d10p2(data)
