
def timer(func):
  import time
  import functools
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    ts = time.perf_counter()
    val = func(*args, **kwargs)
    te = time.perf_counter()
    rt = te - ts
    print(f"Finished {func.__name__} in {rt:.8f}s")
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

with open("input.txt", "r") as f:
  # convert input to list of ints
  nums = list(map(int, f.readlines()))
  # Run challenges
  print(d1p1(nums))
  print(d1p2(nums))
