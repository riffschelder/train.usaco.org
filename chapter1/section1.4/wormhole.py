"""
ID: riff.sc1
LANG: PYTHON3
TASK: wormhole
"""

fin = open('wormhole.in')
fout = open('wormhole.out', 'w')

def get_coords(line):
  numbers = line.split()
  # coords are given in (x, y) but the program is written in (row, col)
  # +x direction is actually +col direction, so we reverse the coords here
  # this is what you get for not reading the problem statement carefully
  return (int(numbers[1]), int(numbers[0]))

def get_pairings(current_paring):
  if None not in current_paring:
    yield current_paring
    return

  first_unpaired = None
  for i, x in enumerate(current_paring):
    if x is None:
      if first_unpaired is None:
        first_unpaired = i
      else:
        current_paring[first_unpaired] = i
        current_paring[i] = first_unpaired
        yield from get_pairings(current_paring)
        current_paring[i] = None
        current_paring[first_unpaired] = None

def get_col(i_col):
  """
  gets (i, col)
  returns col
  probably could have used an itemgetter instead
  """
  return i_col[1]

def map_rights(coords):
  """
  who's to the right of whom? 
  - right_neighbor_of[i] == j, if we walk from wormhole #i to the right and land in wormhold #j. 
  - right_neighbor_of[i] is None, if wormhole #i is the rightmost wormhole in that row.
  """
  right_neighbor_of = [None] * len(coords)

  wormholes_by_row = {}  # who needs defaultdict when we can write it by hand
  for i, coord in enumerate(coords):
    row = coord[0]
    col = coord[1]
    if row not in wormholes_by_row:
      wormholes_by_row[row] = [(i, col)]
    else:
      wormholes_by_row[row].append((i, col))

  for row, wormholes in wormholes_by_row.items():
    wormholes.sort(key=get_col)
    last_wormhole = None
    for i, col in wormholes:
      if last_wormhole is not None:
        right_neighbor_of[last_wormhole[0]] = i
      last_wormhole = (i, col)
    # right neightbor of last_wormhole when we exit the loop is already None (as it should be).

  return right_neighbor_of

def has_loop(pairing):
  """
  starting from each wormhole, do we loop back to this wormhole?
  """
  for start in range(num_wormholes):
    current = start
    while current is not None:
      current = pairing[current]  # warp
      current = right_neighbor_of[current]  # walk to the right
      # if there's a loop, we eventually end up back at start
      if current == start:
        return True
      # if there's no loop, we eventually end up on the right edge, 
      # current becomes None, and while loop is broken.
  # if we end up here, while loop was broken for all starting positions.
  return False

num_wormholes = int(fin.readline()[:-1])
coords = []
for i in range(num_wormholes):
  coords.append(get_coords(fin.readline()))
right_neighbor_of = map_rights(coords)

num_pairings_with_loops = 0
for pairing in get_pairings([None] * num_wormholes):
  if has_loop(pairing):
    num_pairings_with_loops += 1

fout.write('{}\n'.format(num_pairings_with_loops))
