
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
def d8p1(data):
  data = data.split('\n')
  data = [line.split(" ") for line in data]
  data = [{'op': a, 'val': int(b)} for [a,b] in data]

  instr_counter = [0] * len(data)

  acculator = 0
  pc = 0 # program counter
  while 1:
    # increment this instr
    if instr_counter[pc] > 0:
      # already executed
      return acculator
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

    assert (new_pc >= 0)
    pc = new_pc % len(data)

  return 0

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d8p1(data)
