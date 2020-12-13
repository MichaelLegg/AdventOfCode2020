
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
  # count surrounding seats
  look_nw = (x-1, y-1)
  look_nn = (x,y-1)
  look_ne = (x+1,y-1)
  look_ww = (x-1,y)
  look_ee = (x+1,y)
  look_sw = (x-1,y+1)
  look_ss = (x,y+1)
  look_se = (x+1,y+1)
  # check if coords in inside the grid and are empty
  count_occup += ((0<=look_nw[0]<w) and (0<=look_nw[1]<h)) and (all_seats[look_nw[1]][look_nw[0]] == '#')
  count_occup += ((0<=look_nn[0]<w) and (0<=look_nn[1]<h)) and (all_seats[look_nn[1]][look_nn[0]] == '#')
  count_occup += ((0<=look_ne[0]<w) and (0<=look_ne[1]<h)) and (all_seats[look_ne[1]][look_ne[0]] == '#')
  count_occup += ((0<=look_ww[0]<w) and (0<=look_ww[1]<h)) and (all_seats[look_ww[1]][look_ww[0]] == '#')
  count_occup += ((0<=look_ee[0]<w) and (0<=look_ee[1]<h)) and (all_seats[look_ee[1]][look_ee[0]] == '#')
  count_occup += ((0<=look_sw[0]<w) and (0<=look_sw[1]<h)) and (all_seats[look_sw[1]][look_sw[0]] == '#')
  count_occup += ((0<=look_ss[0]<w) and (0<=look_ss[1]<h)) and (all_seats[look_ss[1]][look_ss[0]] == '#')
  count_occup += ((0<=look_se[0]<w) and (0<=look_se[1]<h)) and (all_seats[look_se[1]][look_se[0]] == '#')
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
      if not (0 <= new_x < len(seats[0]) and 0 <= new_y < len(seats)):
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
