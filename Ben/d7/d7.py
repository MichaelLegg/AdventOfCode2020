
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


def traverse_bag_until_sg(bags, bag_lut, bag_type, depth=0):
  # print(" "*depth, bag_type, bags)
  if 'shiny gold' in bags:
    # this bag contains atleast 1 sg bag in, so return yes
    return 1

  # iterate through this bags contents
  has_sg = 0
  for bag_type,bag_count in bags.items():
    # recursively search through each bag
    has_sg |= traverse_bag_until_sg(bag_lut[bag_type], bag_lut, bag_type, depth+1)
  # return if this bag has subbags with shiny gold
  return has_sg

@timer
def d7p1(data):
  import re
  # Dictonary containing 'bag_name': {
  #  'subbag_name': <count>
  # }
  bag_lut = {}
  
  for line in data.split('\n'):
    # extract bag name
    bag_name = re.search(r'(\w+ \w+) bags contain', line).group(1)
    # extract bag contents
    bag_contents = re.findall(r'(\d \w+ \w+)', line)
    # structure into dictionary
    bag_contents = {b[2:]: int(b[0]) for b in bag_contents}
    # add to all bags lut
    bag_lut[bag_name] = bag_contents

  sum = 0
  for bag,contents in bag_lut.items():
    bag_has_sg = traverse_bag_until_sg(contents, bag_lut, bag)
    if bag_has_sg:
      print("Bag containing sg:", bag, contents)
      sum += 1
  return sum

@timer
def d7p2(data):
  return 0

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d7p1(data)
  d7p2(data)
