
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
  for n in nums:
    for m in nums:
      if n == m:
        continue
      #print("Trying", n, m, n+m)
      if n + m == 2020:
        #print("d1p1 =", n*m)
        return n*m

@timer
def d1p2(nums):
  for n in nums:
    for m in nums:
      for p in nums:
        if n == m or m == p:
          continue
        #print("Trying", n, m, n+m)
        if n + m + p == 2020:
          #print("Found! mul =", n*m*p)
          return n*m*p

@timer
def d1p2h(nums):
  hm = {}
  for n in list(nums):
    for m in list(nums):
      key = (n,m)
      if n == m: 
        continue
      if key not in hm: 
        hm[key] = n+m

  i = 0
  for k,v in hm.items():
    n = nums[i%len(nums)]
    if (v+n) == 2020:
      return k[0]*k[1]*n
    i += 1


with open("input.txt", "r") as f:
  # convert input to list of ints
  nums = list(map(int, f.readlines()))
  # Run challenges
  d1p1(nums)
  d1p2(nums)
  d1p2h(nums)
