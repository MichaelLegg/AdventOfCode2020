
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
def d12p1(data):
  data = data.split("\n")
  ship_x = 0
  ship_y = 0
  ship_angle = 90
  # translation functions
  angle_to_cardinal = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
  }
  move_funcs = {
    'N': lambda x,y,v: (x,y+v),
    'E': lambda x,y,v: (x+v,y),
    'S': lambda x,y,v: (x,y-v),
    'W': lambda x,y,v: (x-v,y),
  }
  for instr in data:
    action = instr[0]
    value = int(instr[1:])
    if action == 'F':
      cardinal = angle_to_cardinal[ship_angle]
      ship_x, ship_y = move_funcs[cardinal](ship_x, ship_y, value)
    elif action in set('NESW'):
      ship_x, ship_y = move_funcs[action](ship_x, ship_y, value)
    else:
      # L/R<angle>
      if action == 'L': ship_angle -= value
      if action == 'R': ship_angle += value
      ship_angle = ship_angle % 360
  return abs(ship_x) + abs(ship_y)

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d12p1(data)
