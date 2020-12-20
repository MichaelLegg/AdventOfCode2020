
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
  data = list(map(int, data.split(",")))
  # spoken_number: turn_it_was_last_spoken 
  hm_lastspoken = {}

  # prefill last spoken tracker with starting data
  for i in range(len(data)-1):
    hm_lastspoken[data[i]] = i

  # start on the last starting number
  last_number = data[-1]
  turn = len(data)-1

  # iterate over future turns
  for i in range(N-len(data)):
    # if already spoken this number, find the difference
    # between current turn and the turn it was last spoken
    if last_number in hm_lastspoken:
      nxt_num = turn - hm_lastspoken[last_number]
    else:
      # have not spoken yet, so next number is 0
      nxt_num = 0

    # record that we've spoken this number on this turn
    hm_lastspoken[last_number] = turn
    # move to next number
    last_number = nxt_num
    turn += 1
  return last_number

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
