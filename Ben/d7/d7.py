
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

bag_lut = {}
  
@timer
def d7p1(data):
  import re
  # Dictonary containing 'bag_name': {
  #  'subbag_name': <count>
  # }
  for line in data.split('\n'):
    # extract bag name
    bag_name = re.search(r'(\w+ \w+) bags contain', line).group(1)
    # extract bag contents
    bag_contents = re.findall(r'(\d \w+ \w+)', line)
    # structure into dictionary
    bag_contents = {b[2:]: int(b[0]) for b in bag_contents}
    # add to all bags lut
    bag_lut[bag_name] = bag_contents

  # recursively traverse bags in search of shiny gold
  sum = 0
  for bag,contents in bag_lut.items():
    bag_has_sg = traverse_bag_until_sg(contents, bag_lut, bag)
    if bag_has_sg:
      # print("Bag containing sg:", bag, contents)
      sum += 1
  return sum

def count_bags(bags, bag_lut, bag_type, depth=0):
  print(" "*depth, bag_type, bags)
  if bags == {}:
    return 1

  # iterate through this bags contents
  num_bags = 1
  for bag_type,bag_count in bags.items():
    num_bags += bag_count * count_bags(bag_lut[bag_type], bag_lut, bag_type, depth+1)
  return num_bags

@timer
def d7p2(data):
  # how many bags inside a shiny gold bag
  bag = bag_lut['shiny gold']
  return count_bags(bag, bag_lut, 'shiny gold') -1

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d7p1(data)
  d7p2(data)
