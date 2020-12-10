
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

def run_cpu(data):
  instr_counter = [0] * len(data)
  acculator = 0
  pc = 0 # program counter
  while 1:
    # if instr executed previously, return
    if instr_counter[pc] > 0: 
      return (False, acculator)
    instr_counter[pc] += 1
    # get new instruction
    instr = data[pc]
    new_pc = pc + 1

    # decode and execute instr
    if instr['op'] == 'nop':
      pass
    elif instr['op'] == 'acc':
      acculator += instr['val']
    elif instr['op'] == 'jmp':
      new_pc = pc + instr['val']

    # If reached end of program, success
    if new_pc == len(data)-1:
      return (True, acculator)

    pc = new_pc % len(data)

@timer
def d8p1(data):
  data = data.split('\n')
  data = [line.split(" ") for line in data]
  data = [{'op': a, 'val': int(b)} for [a,b] in data]
  # run cpu on instructions
  (halted,acc) = run_cpu(data)
  return acc

@timer
def d8p2(data):
  data = data.split('\n')
  data = [line.split(" ") for line in data]
  data = [{'op': a, 'val': int(b)} for [a,b] in data]
  # find all address for nop and jmp instructions
  all_nops = [i for i in range(len(data)) if data[i]['op'] == 'nop']
  all_jmps = [i for i in range(len(data)) if data[i]['op'] == 'jmp']
  nops_jmps = all_nops + all_jmps
  # change 1 nop, then run cpu to see if it halts
  import copy
  for i in nops_jmps:
    new_data = copy.deepcopy(data)
    # swap nop for jmp or jmp for nop
    new_data[i]['op'] = 'jmp' if data[i]['op'] == 'nop' else 'nop'
    # run cpu on new instruction list
    success,acc = run_cpu(new_data)
    if success:
      return acc

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d8p1(data)
  d8p2(data)
