
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
def d3p1(lines):
  width = len(lines[0])-1
  height = len(lines)
  sum = 0
  x = 0
  y = 0
  while 1:
    x += 3
    x = x % width
    y += 1
    if y > height-1:
      return sum
    sum += (lines[y][x] == '#')

def traverse_slope(slope, right, down):
  width = len(slope[0])-1
  height = len(slope)
  sum = 0
  x = 0
  y = 0
  while 1:
    x += right
    x = x % width
    y += down
    if y > height-1:
      return sum
    sum += (slope[y][x] == '#')

@timer
def d3p2(slope):
  sum =  traverse_slope(slope, 1, 1)
  sum *= traverse_slope(slope, 3, 1)
  sum *= traverse_slope(slope, 5, 1)
  sum *= traverse_slope(slope, 7, 1)
  sum *= traverse_slope(slope, 1, 2)
  return sum

with open("input.txt", "r") as f:
  data = f.readlines()
  # Run challenges
  d3p1(data)
  d3p2(data)
