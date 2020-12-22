
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

import re
def get_range(line):
  m = re.match("(\w+[ ]*[\w+]*): (\d+)-(\d+) or (\d+)-(\d+)", line)
  if not m:
    return None
  line_type = m.group(1)
  r1 = (int(m.group(2)), int(m.group(3))+1)
  r2 = (int(m.group(4)), int(m.group(5))+1)
  r1 = range(r1[0], r1[1])
  r2 = range(r2[0], r2[1])
  return (line_type,r1,r2, [], [])

@timer
def d16p1(data):
  data = data.split("\n")
  rules = []
  invalid_nums = []
  line_nxt_nearby = False
  for line in data:
    # append all rules into a big list
    #   rule = tuple(type, range1, range2, possible columns, impossible columns)
    if line[:4] in ['row:', 'seat', 'class']:
      line_data = get_range(line)
      if line_data:
        rules.append(line_data)

    if line[:5] == "nearb":
      line_nxt_nearby = True
      continue

    if line_nxt_nearby:
      ticket_vals = list(map(int, line.split(',')))
      for num in ticket_vals:
        valid = False
        for (rule_name, r1, r2, _, _) in rules:
          if num in r1 or num in r2:
            valid = True
        # if number not valid for any rule
        if not valid:
          invalid_nums.append(num)

  # answer is the sum of all invalid numbers in nearby tickets
  return sum(invalid_nums)


@timer
def d16p2(data):
  data = data.split("\n")
  rules                = []
  line_nxt_your_ticket = False
  line_nxt_nearby      = False

  for line in data:
    # append all rules into a big list
    #   rule = tuple(type, range1, range2, possible columns, impossible columns)
    line_data = get_range(line)
    if line_data:
      rules.append(line_data)

    if line[:6] == "your t":
      line_nxt_your_ticket = True
      continue

    # get your ticket
    if line_nxt_your_ticket:
      your_ticket_numbers = list(map(int, line.split(',')))
      line_nxt_your_ticket = False
    
    # get nearby ticket
    if line[:6] == "nearby":
      line_nxt_nearby = True
      continue

    # go through each nearby ticket and determine possible rules
    if line_nxt_nearby:
      # split line into list of numbers
      vals = list(map(int, line.split(',')))
      # skip if a number is not valid for atleast 1 rule
      for col,num in enumerate(vals):
        valid = False
        for (rule_type, r1, r2, possible, impossible) in rules:
          if num in r1 or num in r2:
            valid = True
            continue
        # number is valid for atleast 1 rule
        if valid:
          # find which possible and impossible number columns this rule applies to
          for (rule_type, r1, r2, possible, impossible) in rules:
            if num in r1 or num in r2:
              # this column is valid for this rule and not invalid for others
              if col not in impossible and col not in possible:
                possible.append(col)
            else:
              # number not valid for this rule
              if col in possible:
                possible.remove(col)
              if col not in impossible:
                impossible.append(col)
              continue

  # basically a suduko solver
  #   if rules only have 1 possible column, use that column 
  #   and prevent that column being used in others rules (res_list)
  # Requires atleast 1 rule with only 1 possible column to start working
  res_list = []
  resolved = False
  while not resolved:
    # extract possible columns from rule tuple
    assignments = [possible for (a,b,c,possible,i) in rules]
    # resolved if all rules have exactly 1 possible column
    resolved = all([len(p) == 1 for p in assignments])
    # for each rule
    for (rule_type, r1, r2, possible, impossible) in rules:
      # if only 1 possible columns, it must be that column 
      if len(possible) == 1:
        # say this column has been resolved, 
        #   so other rules dont use it as a possible column
        res_list.append(possible[0])
        possible = possible[0]
        continue
      # remove already resolved columns from this rules possible columns
      for res in res_list:
        if res in possible:
          possible.remove(res)

  # extract the departing rules
  departing_rules = [(t,b,c,p,i) for (t,b,c,p,i) in rules if t[0:6] == "depart"]

  # Use the resolved departing rule's column to index
  #   your ticket numbers array
  answer = 1
  for (a,b,c,p,i) in departing_rules:
    # Answer is product of our numbers indexed by departing rules column
    answer *= your_ticket_numbers[p[0]]
  return answer

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d16p1(data)
  d16p2(data)
