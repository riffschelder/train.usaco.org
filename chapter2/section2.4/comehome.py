"""
ID: riff.sc1
LANG: PYTHON3
TASK: comehome
"""
from collections import defaultdict
from math import inf

fin = open('comehome.in')
fout = open('comehome.out', 'w')

num_paths = int(fin.readline())
paths_from = defaultdict(list)
for _ in range(num_paths):
  (source, target, distance) = fin.readline().split()
  distance = int(distance)
  paths_from[source].append((target, distance))
  paths_from[target].append((source, distance))

distance_from_barn_to = {'Z': 0}
shortest_found = set()

def next_pasture():
  min_distance = inf
  pasture = None
  for (target, distance) in distance_from_barn_to.items():
    if target in shortest_found:
      continue
    if distance < min_distance:
      min_distance = distance
      pasture = target

  return pasture

while True:
  source = next_pasture()
  if not source:
    break

  shortest_found.add(source)
  for (target, distance) in paths_from[source]:
    if (target not in distance_from_barn_to or 
        distance_from_barn_to[source] + distance < distance_from_barn_to[target]):
      distance_from_barn_to[target] = distance_from_barn_to[source] + distance

min_distance = inf
pasture = None
for (target, distance) in distance_from_barn_to.items():
  if 'A' <= target <= 'Y' and distance < min_distance:
    min_distance = distance
    pasture = target

fout.write(f'{pasture} {min_distance}\n')


