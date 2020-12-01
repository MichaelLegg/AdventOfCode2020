
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
def d1p1(nums):
  for n1 in nums:
    for n2 in nums:
      if n1 == n2:
        continue
      #print("Trying", n1, n2, n1+n2)
      if n1 + n2 == 2020:
        #print("found", n1*n2)
        return n1*n2

@timer
def d1p2(nums):
  for n1 in nums:
    for n2 in nums:
      # skip any impossible solutions
      if (n1+n2) >= 2020:
        continue
      for n3 in nums:
        if (n1 == n2) or (n2 == n3):
          continue
        if (n1 + n2 + n3) == 2020:
          #print("found", n1, n2, n3)
          return n1*n2*n3

@timer
def d1p2h(nums):
  hm = {}
  for n1 in list(nums):
    for n2 in list(nums):
      # skip any impossible solutions
      if (n1+n2) >= 2020:
        continue
      if n1 == n2: 
        continue
      # add possible solution to hashmap
      key = (n1,n2)
      if key not in hm: 
        hm[key] = n1+n2
  # Add each input to remaining possible intermediate sums in hashmap
  for n3 in list(nums):
    for (n1,n2),s in hm.items():
      if (s+n3) == 2020:
        return n1*n2*n3


with open("input.txt", "r") as f:
  # convert input to list of ints
  nums = list(map(int, f.readlines()))
  # Run challenges
  d1p1(nums)
  d1p2(nums)
  d1p2h(nums)
