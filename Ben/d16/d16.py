
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
def d16p1(data):
  data = data.split("\n")
  nearby = False
  rules = []
  invalid_nums = []
  for line in data:
    if not nearby:
      if line[0:5] == "class":
        m = re.match("(\d+)-(\d+) or (\d+)-(\d+)", line[7:])
        r1 = (int(m.group(1)), int(m.group(2))+1)
        r2 = (int(m.group(3)), int(m.group(4))+1)
        rules.append(range(r1[0], r1[1]))
        rules.append(range(r2[0], r2[1]))
        continue

      if line[0:3] == "row":
        m = re.match("(\d+)-(\d+) or (\d+)-(\d+)", line[5:])
        r1 = (int(m.group(1)), int(m.group(2))+1)
        r2 = (int(m.group(3)), int(m.group(4))+1)
        rules.append(range(r1[0], r1[1]))
        rules.append(range(r2[0], r2[1]))
        continue

      if line[0:4] == "seat":
        m = re.match("(\d+)-(\d+) or (\d+)-(\d+)", line[6:])
        r1 = (int(m.group(1)), int(m.group(2))+1)
        r2 = (int(m.group(3)), int(m.group(4))+1)
        rules.append(range(r1[0], r1[1]))
        rules.append(range(r2[0], r2[1]))
        continue

    if line[:5] == "nearb":
      nearby = True
      continue

    if nearby:
      vals = list(map(int, line.split(',')))
      for num in vals:
        valid = False
        for rule in rules:
          valid_nums = list(rule)
          if num in valid_nums:
            valid = True
            # print(num, "in", valid_nums)
        if not valid:
          invalid_nums.append(num)
          print(num, "not valid")

  return sum(invalid_nums)

@timer
def d16p2(data):
  return 0

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d16p1(data)
  d16p2(data)
