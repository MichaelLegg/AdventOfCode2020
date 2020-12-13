
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

import math
from functools import reduce
@timer
def d13p1(data):
  data = data.split('\n')
  earliest = int(data[0])
  busses = filter(lambda x: x != 'x', data[1].split(','))
  busses = list(map(int, busses))
  # list of departing busses
  busses_departing = [False] * len(busses)
  # find gcd of bus times to increase time interval
  time_interval = reduce(lambda x,y: math.gcd(x, y), busses)
  # start waiting at bus stop at our arrival time
  time = earliest
  while True:
    for i,bus in enumerate(busses):
      busses_departing[i] = time % bus == 0
      if time % bus == 0:
        departing_bus = bus
    if any(busses_departing):
      return (time-earliest) * departing_bus
    # go to next time interval
    time += time_interval

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d13p1(data)
