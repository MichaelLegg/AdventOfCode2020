
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

    # check all required fields are present
    valid = [f in fields for f in req_fields]
    if not all(valid):
      continue

    # Extract values into correct data types
    values = [f[4:] for f in p]
    fv = dict(zip(fields, values))
    fv['byr'] = int(fv['byr'])
    fv['iyr'] = int(fv['iyr'])
    fv['eyr'] = int(fv['eyr'])

    # is passport valid
    valid = 1

    # start of value checks
    # hgt might be in cm or inches, and convert to int
    if 'cm' in fv['hgt']:
      fv['hgt'] = fv['hgt'].split('c')
      fv['hgt'][0] = int(fv['hgt'][0])
    elif 'in' in fv['hgt']:
      fv['hgt'] = fv['hgt'].split('i')
      fv['hgt'][0] = int(fv['hgt'][0])
    else:
      # no unit provided, so its invalid
      valid = 0

    # check values are valid
    valid &= len(fv['pid']) == 9
    valid &= (fv["byr"] >= 1910) and (fv["byr"] <= 2002)
    valid &= (fv["iyr"] >= 2010) and (fv["iyr"] <= 2020)
    valid &= (fv["eyr"] >= 2020) and (fv["eyr"] <= 2030)
    if "m" in fv["hgt"]: # cm
      valid &= (fv["hgt"][0] >= 150) and (fv["hgt"][0] <= 193)
    elif "n" in fv["hgt"]: # in
      valid &= (fv["hgt"][0] >= 59) and (fv["hgt"][0] <= 76)
    else:
      continue

    # check hcl value
    if not (fv['hcl'][0] == '#'):
      continue
    valid &= len(fv['hcl'][1:]) == 6
    for c in fv['hcl'][1:]:
      valid &= (c >= '0' and c <= '9') or (c >= 'a' and c <= 'f')
    
    # check ecl value
    req_ecl = ['amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth']
    if fv['ecl'] not in req_ecl:
      continue
    
    sum += valid
  return sum

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d4p1(data)
  d4p2(data)
