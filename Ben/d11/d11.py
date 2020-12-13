
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

def adj_count(x, y, all_seats):
  count_occup = 0
  w = len(all_seats[0])
  h = len(all_seats)
  # surrounding seats
  look_nw = lambda x,y: (x-1, y-1)
  look_nn = lambda x,y: (x,y-1)
  look_ne = lambda x,y: (x+1,y-1)
  look_ww = lambda x,y: (x-1,y)
  look_ee = lambda x,y: (x+1,y)
  look_sw = lambda x,y: (x-1,y+1)
  look_ss = lambda x,y: (x,y+1)
  look_se = lambda x,y: (x+1,y+1)
  directions = [look_nw, look_nn, look_ne, look_ww, look_ee, look_sw, look_ss, look_se]
  count_occup = 0
  # look in each direction
  for look in directions:
    new_x, new_y = look(x, y)
    # if that seat if occupied, count it
    count_occup += ((0<=new_x<w) and (0<=new_y<h)) and (all_seats[new_y][new_x] == '#')
  return count_occup

@timer
def d11p1(data):
  import copy
  # seats = data.split("\n")
  w = 10
  last_seats = data.split("\n")
  stable = False
  while not stable:
    new_seats = copy.deepcopy(last_seats)
    for y,row in enumerate(last_seats):
      row = list(row)
      for x,seat in enumerate(row):
        # count surrounding seats
        if seat == '.': 
          continue
        count_occup = adj_count(x, y, last_seats)
        if seat == 'L' and count_occup == 0:
          row[x] = '#'
        elif seat == '#' and count_occup >= 4:
          row[x] = 'L'
      row = "".join(row)
      new_seats[y] = row
    # stable when last current seats == last seats
    stable = new_seats == last_seats
    last_seats = new_seats
  return "".join(last_seats).count('#')

def seat_visible(x, y, seats):
  w = len(seats[0])
  h = len(seats)
  look_nw = lambda x,y: (x-1, y-1)
  look_nn = lambda x,y: (x,y-1)
  look_ne = lambda x,y: (x+1,y-1)
  look_ww = lambda x,y: (x-1,y)
  look_ee = lambda x,y: (x+1,y)
  look_sw = lambda x,y: (x-1,y+1)
  look_ss = lambda x,y: (x,y+1)
  look_se = lambda x,y: (x+1,y+1)
  directions = [look_nw, look_nn, look_ne, look_ww, look_ee, look_sw, look_ss, look_se]
  count_occup = 0
  # For each looking direction, loop through grid in that direction until sight blocked
  for look in directions:
    new_x, new_y = x, y
    sight_blocked = False
    # keep looping through grid in that direction until sight blocked
    while not sight_blocked:
      # Move to seat in current looking direction 'look'
      new_x,new_y = look(new_x,new_y)
      # if outside grid, stop looking
      if not ((0 <= new_x < w) and (0 <= new_y < h)):
        break
      looking_at_seat = seats[new_y][new_x]
      # if current seat is empty or occupied
      sight_blocked = looking_at_seat == '#' or looking_at_seat == 'L'
      count_occup += looking_at_seat == '#'
  return count_occup

@timer
def d11p2(data):
  import copy
  last_seats = data.split("\n")
  # Keep iterating while the seats haven't settled
  stable = False
  while not stable:
    # print()
    new_seats = copy.deepcopy(last_seats)
    for y,row in enumerate(last_seats):
      # split row into list for easy editing
      row = list(row)
      for x,seat in enumerate(row):
        # if not a seat, skip it
        if seat == '.': 
          continue
        # count surrounding seats
        count_occup = seat_visible(x, y, last_seats)
        if seat == '#' and count_occup >= 5:
          row[x] = 'L'
        elif seat == 'L' and count_occup == 0:
          row[x] = '#'
      # rebuilt row array (list to string)
      row = "".join(row)
      new_seats[y] = row
    # print("\n".join(new_seats))
    # stable when last current seats == last seats
    stable = new_seats == last_seats
    last_seats = new_seats
  return "".join(last_seats).count('#')

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d11p1(data)
  d11p2(data)
