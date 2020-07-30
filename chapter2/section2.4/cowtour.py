"""
ID: riff.sc1
LANG: PYTHON3
TASK: cowtour
"""
fin = open('cowtour.in')
fout = open('cowtour.out', 'w')

num_pastures = int(fin.readline())
coords = []
for _ in range(num_pastures):
  (x, y) = [int(x) for x in fin.readline().split()]
  coords.append((x, y))

is_connected = []
for _ in range(num_pastures):
  is_connected.append([(True if x == '1' else False) for x in fin.readline().strip()])

infinity = 1000000
distance = [[infinity] * num_pastures for _ in range(num_pastures)]

fields = []  # a field is a collection of connected pastures
field_of = [None] * num_pastures  # pasture i is in field `field_of[i]`

def populate_field(pasture, field_id, field):
  field_of[pasture] = field_id
  field.add(pasture)
  for i in range(num_pastures):
    if is_connected[pasture][i] and field_of[i] is None:
      populate_field(i, field_id, field)

for i in range(num_pastures):
  if field_of[i] is None:
    field_id = len(fields)
    new_field = set()
    populate_field(i, field_id, new_field)
    fields.append(new_field)

def euclidean_distance(i, j):
  (xi, yi) = coords[i]
  (xj, yj) = coords[j]
  return ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5

for i in range(num_pastures):
  for j in range(num_pastures):
    if i == j:
      distance[i][j] = 0
    if is_connected[i][j]:
      distance[i][j] = euclidean_distance(i, j)

for k in range(num_pastures):
  for i in range(num_pastures):
    for j in range(i):
      if distance[i][j] > distance[i][k] + distance[k][j]:
        distance[i][j] = distance[i][k] + distance[k][j]
        distance[j][i] = distance[i][k] + distance[k][j]

diameter = [-1] * len(fields)
for i in range(num_pastures):
  farthest_from_i = max([d for d in distance[i] if d < infinity])
  if diameter[field_of[i]] < farthest_from_i:
    diameter[field_of[i]] = farthest_from_i

smallest_diameter = infinity
for i in range(num_pastures):
  farthest_from_i = max([d for d in distance[i] if d < infinity])
  for j in range(num_pastures):
    if field_of[i] == field_of[j]:
      continue
    farthest_from_j = max([d for d in distance[j] if d < infinity])
    new_diameter = max(euclidean_distance(i, j) + farthest_from_i + farthest_from_j,
                       diameter[field_of[i]],
                       diameter[field_of[j]])
    if new_diameter < smallest_diameter:
      smallest_diameter = new_diameter

fout.write('{:.6f}\n'.format(smallest_diameter))
