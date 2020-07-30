"""
ID: riff.sc1
LANG: PYTHON3
TASK: ttwo
"""
fin = open('ttwo.in')
fout = open('ttwo.out', 'w')

farm = fin.readlines()

is_free = []  # False iff the square is an obstacle.
farmer = None
cows = None
for r, line in enumerate(farm):
  row = []
  is_free.append(row)
  for c, square in enumerate(line.strip()):
    if square == '*':
      row.append(False)
    else:
      row.append(True)

    if square == 'F':
      farmer = (r, c, 'north')
    if square == 'C':
      cows = (r, c, 'north')

time = 0
loop = False
visited = set()
visited.add((farmer, cows))

step_in = {'north': (-1, 0), 'east': (0, 1), 'south': (1, 0), 'west': (0, -1)}
turn_from = {'north': 'east', 'east': 'south', 'south': 'west', 'west': 'north'}

def take_step(coords, step):
  return (coords[0] + step[0], coords[1] + step[1])

def square_is_okay(coords):
  (r, c) = coords
  if r >= 10 or r < 0 or c >= 10 or c < 0:
    return False
  if not is_free[r][c]:
    return False
  return True

def move(thing):
  (r, c, direction) = thing
  would_be = take_step((r, c), step_in[direction])
  if square_is_okay(would_be):
    return (would_be[0], would_be[1], direction)
  else:
    return (r, c, turn_from[direction])

while True:
  farmer = move(farmer)
  cows = move(cows)
  time += 1

  if (farmer, cows) in visited:
    loop = True
    break
  
  if farmer[0] == cows[0] and farmer[1] == cows[1]:
    break

  visited.add((farmer, cows))

if loop:
  fout.write('0\n')
else:
  fout.write(f'{time}\n')







