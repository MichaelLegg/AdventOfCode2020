
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
def d5p1(data):
  data = data.split("\n")
  largest = 0
  for line in data:
    # convert to binary
    line = line.replace("F", "0")
    line = line.replace("B", "1")
    line = line.replace("L", "0")
    line = line.replace("R", "1")
    # extract row and columns
    row = int(line[:7],2)
    col = int(line[7:11],2)
    # calculate seat id
    id = row*8+col
    print(id)
    if id > largest:
      largest = id
  return largest

@timer
def d5p2(data):
  data = data.split("\n")
  seats = []
  for line in data:
    # convert to binary
    line = line.replace("F", "0")
    line = line.replace("B", "1")
    line = line.replace("L", "0")
    line = line.replace("R", "1")
    # extract row and columns
    row = int(line[:7],2)
    col = int(line[7:11],2)
    # calculate seat id
    id = row*8+col
    seats.append(id)
  # find missing seat
  # missing seat is the missing consecutive number
  seats = sorted(seats)
  for i in range(len(seats)):
    id = seats[i]
    if seats[i+1] != id+1:
      return id+1

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d5p1(data)
  d5p2(data)
