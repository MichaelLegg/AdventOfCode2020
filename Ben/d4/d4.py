
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

# Valid if all these fields are present:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
@timer
def d4p1(data):
  sum = 0
  req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  passports = data.split("\n\n")
  for p in passports:
    p = p.replace("\n"," ")
    p = p.split(" ")
    fields = [f[:3] for f in p]
    # check all req fields are present
    valid = [f in fields for f in req_fields]
    sum += all(valid)
  return sum

@timer
def d4p2(data):
  sum = 0
  req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  passports = data.split("\n\n")
  for p in passports:
    # Extract fields
    p = p.replace("\n"," ")
    p = p.split(" ")
    fields = [f[:3] for f in p]
    values = [f[4:] for f in p]
    fv = dict(zip(fields, values))

    # check all required fields are present
    valid = [f in fields for f in req_fields]
    if not all(valid):
      continue

    # is passport valid
    valid = 1
    # start of value checks
    # check values are valid
    valid &= len(fv['pid']) == 9
    valid &= 1910 <= int(fv["byr"]) <= 2020
    valid &= 2010 <= int(fv["iyr"]) <= 2020
    valid &= 2020 <= int(fv["eyr"]) <= 2030
    # if cm, 150 <= h <= 193
    # if in, 59  <= h <= 76
    valid &= (fv['hgt'][-2:] == "cm" and 150 <= int(fv['hgt'][:-2]) <= 193) or \
             (fv['hgt'][-2:] == "in" and  59 <= int(fv['hgt'][:-2]) <= 76)
    valid &= (fv['hcl'][0] == '#') and \
             (len(fv['hcl'][1:]) == 6) and \
             all([('0' <= c <= '9') or ('a' <= c <= 'f') for c in fv['hcl'][1:]])
    valid &= fv['ecl'] in ['amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth']
    sum += valid
  return sum

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d4p1(data)
  d4p2(data)
