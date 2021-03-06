
from funcs.funcs import timer

@timer
def d17p1(data):
  import copy
  # dictionary where key = x,y,z and value = active/inactive
  grid3d = {}
  # load initial grid where z=0
  initial_grid = data.split("\n")
  for y in range(len(initial_grid)):
    for x in range(len(initial_grid[0])):
      grid3d[(x-1,y-1,0)] = initial_grid[y][x]

  # get min max of each dimension
  cycle_limit = 6
  while cycle_limit:
    # get 3d grid dimensions
    # front top left
    xmin = min([x[0] for x in grid3d])-1
    ymin = min([x[1] for x in grid3d])-1
    zmin = min([x[2] for x in grid3d])-1
    # back bottom right
    xmax = max([x[0] for x in grid3d])+1
    ymax = max([x[1] for x in grid3d])+1
    zmax = max([x[2] for x in grid3d])+1

    def pg():
      for z in range(zmin, zmax+1):
        print("z=",z)
        for y in range(ymin, ymax+1):
          for x in range(xmin, xmax+1):
            grid_state = grid3d.get((x,y,z), '.')
            print(f'{grid_state}', end='')
          print()
    # print initial grid
    # pg()

    grid3d_nxt = copy.deepcopy(grid3d)
    # for each cube in the 3d grid
    for z in range(zmin, zmax+1):
      for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
          grid_state = grid3d.get((x,y,z), '.')

          # count surrounding 26 grid coords
          active_count = 0
          for zi in range(-1,1+1):
            for yi in range(-1,1+1):
              for xi in range(-1,1+1):
                # dont consider current (middle) cube
                if zi == 0 and yi == 0 and xi == 0:
                  continue
                active_count += grid3d.get((x+xi, y+yi, z+zi), '.') == '#'
          # update current cube based on surrounding cubes
          if grid_state == '#' and active_count not in [2,3]:
            grid3d_nxt[(x,y,z)] = '.'
          if grid_state == '.' and active_count == 3:
            grid3d_nxt[(x,y,z)] = '#'

    # update grid with new grid
    grid3d = grid3d_nxt
    cycle_limit -= 1

  # print("\nFinal grid")
  # pg()

  # part 1 answer is count of all active cubes in the grid
  return len([x for x in grid3d if grid3d[x] == '#'])

def d17p2(data):
  import copy
  # dictionary where key = x,y,z,w and value = active/inactive
  grid3d = {}
  # load initial grid where z=0
  initial_grid = data.split("\n")
  for y in range(len(initial_grid)):
    for x in range(len(initial_grid[0])):
      grid3d[(x-1,y-1,0,0)] = initial_grid[y][x]

  # get min max of each dimension
  cycle_limit = 6
  while cycle_limit:
    # get 3d grid dimensions
    # front top left
    xmin = min([coord[0] for coord in grid3d])-1
    ymin = min([coord[1] for coord in grid3d])-1
    zmin = min([coord[2] for coord in grid3d])-1
    wmin = min([coord[3] for coord in grid3d])-1
    # back bottom right
    xmax = max([coord[0] for coord in grid3d])+1
    ymax = max([coord[1] for coord in grid3d])+1
    zmax = max([coord[2] for coord in grid3d])+1
    wmax = max([coord[3] for coord in grid3d])+1

    # print grid
    def pg():
      for w in range(wmin, wmax+1):
        for z in range(zmin, zmax+1):
          print("z=",z,"w=",w)
          for y in range(ymin, ymax+1):
            for x in range(xmin, xmax+1):
              cube = grid3d.get((x,y,z,w), '.')
              print(f'{cube}', end='')
            print()
    # print initial grid
    # print("Next iteration")
    # pg()

    grid3d_nxt = copy.deepcopy(grid3d)
    # for each cube in the 3d grid
    for w in range(wmin, wmax+1):
      for z in range(zmin, zmax+1):
        for x in range(xmin, xmax+1):
          for y in range(ymin, ymax+1):
            cube = grid3d.get((x,y,z,w), '.')
            # print((x,y,z,w))
            # count surrounding cubes
            active_count = 0
            for wi in range(-1,1+1):
              for zi in range(-1,1+1):
                for yi in range(-1,1+1):
                  for xi in range(-1,1+1):
                    # dont consider current (middle) cube
                    if wi == 0 and zi == 0 and yi == 0 and xi == 0:
                      continue
                    active_count += grid3d.get((x+xi, y+yi, z+zi, w+wi), '.') == '#'
            # update current cube based on surrounding cubes
            if cube == '#' and active_count not in [2,3]:
              grid3d_nxt[(x,y,z,w)] = '.'
            if cube == '.' and active_count == 3:
              grid3d_nxt[(x,y,z,w)] = '#'

    # update grid with new grid
    grid3d = grid3d_nxt
    cycle_limit -= 1

  # print("\nFinal grid")
  # pg()

  # part 1 answer is count of all active cubes in the grid
  return len([coord for coord in grid3d if grid3d[coord] == '#'])

with open("input.txt", "r") as f:
  data = f.read()
  # Run challenges
  d17p1(data)
  d17p2(data)
