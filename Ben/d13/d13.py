
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

import math
from functools import reduce
@timer
def d13p2(data):
  data = data.split('\n')
  earliest = int(data[0])
  busses = data[1].split(',')
  busses = list(map(lambda x: int(x) if x != 'x' else x, busses))
  busses_idx = [i if busses[i] != 'x' else 'x' for i in range(len(busses))]
  # busses = list(zip(busses, busses_idx))
  busses_notx = list(filter(lambda bus: bus != 'x', busses))
  busses_idx_notx = list(filter(lambda bus: bus != 'x', busses_idx))
  # list of departing busses
  busses_departing = [False] * len(busses_notx)
  # find gcd of bus times to increase time interval
  time_interval = reduce(lambda x,y: math.gcd(x, y), busses_notx)

  window_len = len(busses)
  bus_window_matches = [
    [t == busses_idx_notx[b] for t in range(window_len)] for b,bus in enumerate(busses_idx_notx)
  ]
  
  # bus window
  window = [
    [False for t in range(window_len)] for b,bus in enumerate(busses_idx_notx)
  ]

  # start waiting at bus stop at our arrival time
  time = 0#earliest
  bus_window_counters = [0 for _ in busses_idx_notx]
  counter = 0
  answer = 0
  first = True
  while True:
    # print("time:", time)
    for i,bus in enumerate(busses_notx):
      if bus == 'x': continue
      busses_departing[i] = time % bus == 0
      # on first bus depart, reset counters
      
      window[i][counter] = time % bus == 0

    anded = [
      [bus_window_matches[b][i] and window[b][i] for i in range(window_len)] for b,bus in enumerate(busses_idx_notx)
    ]
    if anded == bus_window_matches:
      return answer

    if busses_departing[0]:
      answer = time
      bus_window_counters = [0 for _ in busses_idx_notx]
      counter = 0

    counter += 1
    counter %= window_len+1

      # window[i][bus_window_counters[i]] = time % bus == 0

      # bus_window_counters[i] += 1
      # bus_window_counters[i] %= busses_idx_notx[i]+1
    


    # go to next time interval
    time += time_interval

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d13p1(data)
  d13p2(data)
