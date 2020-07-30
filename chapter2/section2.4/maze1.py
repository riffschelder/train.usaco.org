"""
ID: riff.sc1
LANG: PYTHON3
TASK: maze1
"""
fin = open('maze1.in')
fout = open('maze1.out', 'w')

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

(num_cols, num_rows) = [int(x) for x in fin.readline().split()]
maze = [[0] * num_cols for _ in range(num_rows)]

for r in range(num_rows + 1):
  horizontals = fin.readline()
  for (i, char) in enumerate(horizontals):
    if i % 2 == 0:  # it's a meaningless '+'
      continue
    c = i // 2
    if char == '-':
      if r < num_rows:
        maze[r][c] |= NORTH
      if r > 0:
        maze[r-1][c] |= SOUTH

  if r == num_rows:
    break
  verticals = fin.readline()
  for (i, char) in enumerate(verticals):
    if i % 2 == 1:  # it's a meaningless ' '
      continue
    c = i // 2
    if char == '|':
      if c < num_cols:
        maze[r][c] |= WEST
      if c > 0:
        maze[r][c-1] |= EAST

INFINITY = 10000
distance_to_exit = [[INFINITY] * num_cols for _ in range(num_rows)]
starting_points = []
for c in range(num_cols):
  if not maze[0][c] & NORTH:
    starting_points.append((0, c))
  if not maze[num_rows-1][c] & SOUTH:
    starting_points.append((num_rows-1, c))

for r in range(num_rows):
  if not maze[r][0] & WEST:
    starting_points.append((r, 0))
  if not maze[r][num_cols-1] & EAST:
    starting_points.append((r, num_cols-1))

distance = 1
cells_at_this_distance = starting_points
while cells_at_this_distance:
  neighbors = set()  # Initially had a list here and the same cell got added many, many times
  for (r, c) in cells_at_this_distance:
    distance_to_exit[r][c] = distance

  for (r, c) in cells_at_this_distance:
    walls = maze[r][c]
    if r > 0 and not walls & NORTH and distance_to_exit[r-1][c] > distance + 1:
      neighbors.add((r-1, c))
    if r < num_rows-1 and not walls & SOUTH and distance_to_exit[r+1][c] > distance + 1:
      neighbors.add((r+1, c))
    if c > 0 and not walls & WEST and distance_to_exit[r][c-1] > distance + 1:
      neighbors.add((r, c-1))
    if c < num_cols-1 and not walls & EAST and distance_to_exit[r][c+1] > distance + 1:
      neighbors.add((r, c+1))

  distance += 1
  cells_at_this_distance = list(neighbors)

fout.write(f'{distance-1}\n')
