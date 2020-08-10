"""
ID: riff.sc1
LANG: PYTHON3
TASK: butter
"""
from math import inf
from heapq import heappush, heappop

def main():
  with open('butter.in') as fin:
    (num_cows, num_pastures, num_paths) = [int(x) for x in fin.readline().split()]
    
    # Our pastures are 0-indexed, but input data is 1-indexed.
    cow_positions = []
    for _ in range(num_cows):
      cow_positions.append(int(fin.readline()) - 1)

    # Floyd-Warshall takes too long to run. Since the graph has a limited number
    # of edges, it's better to use Dijkstra's with an adjacency list.
    paths_from = [[] for _ in range(num_pastures)]
    for _ in range(num_paths):
      (a, b, length) = [int(x) for x in fin.readline().split()]
      a -= 1
      b -= 1
      paths_from[a].append((b, length))
      paths_from[b].append((a, length))

  min_total_distance = inf
  for sugar in range(num_pastures):
    distances_from_sugar_to = get_min_distance_from(sugar, paths_from, num_pastures)
    total_distance = 0
    for cow in cow_positions:
      total_distance += distances_from_sugar_to[cow]
    if total_distance < min_total_distance:
      min_total_distance = total_distance

  with open('butter.out', 'w') as fout:
    fout.write(f'{min_total_distance}\n')

def get_min_distance_from(source, paths_from, num_pastures):
  min_distance_from_source_to = [inf] * num_pastures  # As far as we've discovered.
  min_distance_found_for = [False] * num_pastures
  frontier = []
  heappush(frontier, (0, source))

  while True:
    try:  # Using the try-except block saves some time compared to an if block.
      (distance, pasture) = heappop(frontier)
      # Disregard outdated information.
      while min_distance_found_for[pasture]:
        (distance, pasture) = heappop(frontier)
    except IndexError:
      # `frontier` is empty because the graph has been fully traversed.
      break

    min_distance_from_source_to[pasture] = distance
    min_distance_found_for[pasture] = True

    for (connection, path_length) in paths_from[pasture]:
      if min_distance_found_for[connection]:
        continue
      if distance + path_length < min_distance_from_source_to[connection]:
        min_distance_from_source_to[connection] = distance + path_length
        heappush(frontier, (distance + path_length, connection))
        # Leave the old entry in the heapq; it'll be discarded when retrieved.

  return min_distance_from_source_to

main()

