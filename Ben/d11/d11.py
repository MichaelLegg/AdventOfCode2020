
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
  count_empty = 0
  count_occup = 0
  w = len(all_seats[0])
  h = len(all_seats)
  # count surrounding seats
  idx_tl = (x-1, y-1)
  idx_tt = (x,y-1)
  idx_tr = (x+1,y-1)
  idx_ll = (x-1,y)
  idx_rr = (x+1,y)
  idx_bl = (x-1,y+1)
  idx_bb = (x,y+1)
  idx_br = (x+1,y+1)
  count_empty += 1 if 0<=idx_tl[0]<w and 0<=idx_tl[1]<h and all_seats[idx_tl[1]][idx_tl[0]] == 'L' else 0
  count_empty += 1 if 0<=idx_tt[0]<w and 0<=idx_tt[1]<h and all_seats[idx_tt[1]][idx_tt[0]] == 'L' else 0
  count_empty += 1 if 0<=idx_tr[0]<w and 0<=idx_tr[1]<h and all_seats[idx_tr[1]][idx_tr[0]] == 'L' else 0
  count_empty += 1 if 0<=idx_ll[0]<w and 0<=idx_ll[1]<h and all_seats[idx_ll[1]][idx_ll[0]] == 'L' else 0
  count_empty += 1 if 0<=idx_rr[0]<w and 0<=idx_rr[1]<h and all_seats[idx_rr[1]][idx_rr[0]] == 'L' else 0
  count_empty += 1 if 0<=idx_bl[0]<w and 0<=idx_bl[1]<h and all_seats[idx_bl[1]][idx_bl[0]] == 'L' else 0
  count_empty += 1 if 0<=idx_bb[0]<w and 0<=idx_bb[1]<h and all_seats[idx_bb[1]][idx_bb[0]] == 'L' else 0
  count_empty += 1 if 0<=idx_br[0]<w and 0<=idx_br[1]<h and all_seats[idx_br[1]][idx_br[0]] == 'L' else 0
  count_occup += 1 if 0<=idx_tl[0]<w and 0<=idx_tl[1]<h and all_seats[idx_tl[1]][idx_tl[0]] == '#' else 0
  count_occup += 1 if 0<=idx_tt[0]<w and 0<=idx_tt[1]<h and all_seats[idx_tt[1]][idx_tt[0]] == '#' else 0
  count_occup += 1 if 0<=idx_tr[0]<w and 0<=idx_tr[1]<h and all_seats[idx_tr[1]][idx_tr[0]] == '#' else 0
  count_occup += 1 if 0<=idx_ll[0]<w and 0<=idx_ll[1]<h and all_seats[idx_ll[1]][idx_ll[0]] == '#' else 0
  count_occup += 1 if 0<=idx_rr[0]<w and 0<=idx_rr[1]<h and all_seats[idx_rr[1]][idx_rr[0]] == '#' else 0
  count_occup += 1 if 0<=idx_bl[0]<w and 0<=idx_bl[1]<h and all_seats[idx_bl[1]][idx_bl[0]] == '#' else 0
  count_occup += 1 if 0<=idx_bb[0]<w and 0<=idx_bb[1]<h and all_seats[idx_bb[1]][idx_bb[0]] == '#' else 0
  count_occup += 1 if 0<=idx_br[0]<w and 0<=idx_br[1]<h and all_seats[idx_br[1]][idx_br[0]] == '#' else 0
  return count_empty, count_occup

@timer
def d11p1(data):
  import copy
  # seats = data.split("\n")
  w = 10
  last_seats = data.split("\n")
  stable = False
  while not stable:
    print()
    new_seats = copy.deepcopy(last_seats)
    for y,row in enumerate(last_seats):
      row = list(row)
      for x,seat in enumerate(row):
        # count surrounding seats
        if last_seats[y][x] == '.': 
          continue
        count_empty, count_occup = adj_count(x, y, last_seats)
        if last_seats[y][x] == 'L' and count_occup == 0:
          row[x] = '#'
        elif last_seats[y][x] == '#' and count_occup >= 4:
          row[x] = 'L'

      row = "".join(row)
      new_seats[y] = row
    print("\n".join(new_seats))
    # stable when last current seats == last seats
    stable = new_seats == last_seats
    last_seats = new_seats

  return "".join(last_seats).count('#')

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d11p1(data)
