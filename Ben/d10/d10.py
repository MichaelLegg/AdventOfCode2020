
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

memory = {}

import copy
def search(current, chargers, i, ls):
  # ls = copy.deepcopy(ls)
  # ls.append(current)
  # find next possible chargers in the bag
  next3 = chargers[i:i+3]
  possible = tuple(filter(lambda x: x <= current+3, next3))

  # store solution to avoid redoing
  if possible in memory:
    return memory[possible]

  # if no possible next charger, we've reached the end
  if len(possible) == 0:
    return 1
  # for each possible charger, start a new search tree using it
  s = 0
  for pi in range(len(possible)):
    charger = possible[pi]
    s += search(charger, chargers, i+pi+1, ls)

  memory[possible] = s
  return s


@timer
def d10p2(data):
  chargers = map(int, data.split("\n"))
  chargers = sorted(chargers)
  result = []
  return search(0, chargers, 0, [])

def search_tr(current, chargers, i, ls):
  return 0

def go(i, current, acc, data):
  next3 = data[i:i+3]
  possible = list(filter(lambda x: x <= current+3, next3))
  if len(possible) == 0:
    return 1

  sum = 0
  for pi in range(len(possible)):
    c = possible[i]
    go(pi, c, acc, data)

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d10p1(data)
  d10p2(data)
