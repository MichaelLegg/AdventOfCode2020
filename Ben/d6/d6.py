
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
def d6p1(data):
  data = data.split("\n\n")
  sum = 0
  for group in data:
    group = group.replace("\n", "")
    # create a unique set of all answers
    qs = set(group)
    # append how many unique answered questions
    sum += len(qs)
  return sum

@timer
def d6p2(data):
  data = data.split("\n\n")
  sum = 0
  for group in data:
    # split answers into per person
    people = group.split("\n")
    # keep track of questions counted, to avoid recounting
    counted = set()
    # for each question list a person answered
    for qa in people:
      # for each question in list
      for q in qa:
        # if we've not counted this answer
        if q not in counted:
          # if everyone has answered this question
          sum += group.count(q) == len(people)
        counted.add(q)
  return sum

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d6p1(data)
  d6p2(data)
