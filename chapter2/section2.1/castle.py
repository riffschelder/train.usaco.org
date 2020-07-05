"""
ID: riff.sc1
LANG: PYTHON3
TASK: castle
"""
from __future__ import annotations
from dataclasses import dataclass

fin = open('castle.in')
fout = open('castle.out', 'w')
(num_cols, num_rows) = [int(x) for x in fin.readline().split()]

@dataclass
class Module:
  # coordinates
  row : int
  col : int

  # neighbors
  north : Module = None
  east  : Module = None
  south : Module = None
  west  : Module = None

  # all modules in the same "room" has the same primary module
  primary : Module = None
  room_size : int = 0

# this double for-loop could be a one-liner but I'm bad at list comprehensions.
castle = []
for i in range(num_rows):
  castle.append([])
  for j in range(num_cols):
    castle[i].append(Module(row=i, col=j))

for i in range(num_rows):
  data = [int(x) for x in fin.readline().split()]
  for j, walls in enumerate(data):
    if not walls & 1:
      castle[i][j].west = castle[i][j-1]
    if not walls & 2:
      castle[i][j].north = castle[i-1][j]
    if not walls & 4:
      castle[i][j].east = castle[i][j+1]
    if not walls & 8:
      castle[i][j].south = castle[i+1][j]

def set_primary(module, primary):
  """
  sets all modules in the room to a single primary module.
  returns room size.
  """
  module.primary = primary
  room_size = 1
  if module.east is not None and module.east.primary is None:
    room_size += set_primary(module.east, primary)
  if module.south is not None and module.south.primary is None:
    room_size += set_primary(module.south, primary)
  if module.west is not None and module.west.primary is None:
    room_size += set_primary(module.west, primary)
  if module.north is not None and module.north.primary is None:
    room_size += set_primary(module.north, primary)
  if module is primary:
    module.room_size = room_size
  return room_size

for i in range(num_rows):
  for j in range(num_cols):
    if castle[i][j].primary is None:
      castle[i][j].room_size = set_primary(castle[i][j], castle[i][j])

primary_modules = []
size_of_largest_room = 0
for i in range(num_rows):
  for j in range(num_cols):
    module = castle[i][j]
    if module.primary is module:
      primary_modules.append(module)
      if module.room_size > size_of_largest_room:
        size_of_largest_room = module.room_size
    else:
      module.room_size = module.primary.room_size
num_rooms = len(primary_modules)

wall_breaks = []  # (module, wall, new_room_size)
# only consider north and east walls (every south/west wall has a north/east counterpart).
for i in range(num_rows):
  for j in range(num_cols):
    module = castle[i][j]
    if module.north is None and i > 0:
      north_neighbor = castle[i-1][j]
      if north_neighbor.primary is not module.primary:
        wall_breaks.append((module, 'N', module.room_size + north_neighbor.room_size))
    if module.east is None and j < num_cols - 1:
      east_neighbor = castle[i][j+1]
      if east_neighbor.primary is not module.primary:
        wall_breaks.append((module, 'E', module.room_size + east_neighbor.room_size))

def tiebreak(wall_break):
  (module, wall, new_room_size) = wall_break
  # first sort by new room size
  A = new_room_size
  # then farthest to the west (smallest col, so taking negation here)
  B = -module.col
  # then farthest to the south
  C = module.row
  # then N before 'E'
  D = 0
  if wall == 'N':
    D = 1
  return (A, B, C, D)

wall_breaks.sort(key=tiebreak, reverse=True)
best_wall_break = wall_breaks[0]

fout.write(f'{num_rooms}\n')
fout.write(f'{size_of_largest_room}\n')
fout.write(f'{best_wall_break[2]}\n')
# evil 1-based numbering...
fout.write(f'{best_wall_break[0].row + 1} {best_wall_break[0].col + 1} {best_wall_break[1]}\n')
