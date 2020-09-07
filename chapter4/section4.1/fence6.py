"""
ID: riff.sc1
LANG: PYTHON3
TASK: fence6
"""

# No clever tricks needed. A simple search will do.
#
# The post-solve analysis suggests we convert the input into a graph (creating
# verticies where segments intersect). For each edge, we remove it from the
# graph and find the shortest path between its two endpoints. The shortest loop
# containing this edge is necessarily this shortest path plus the edge itself.
#
# This solution does none of that. I don't know if it runs slower, but it sure
# is a lot easier to code.

from math import inf

def main():
  with open('fence6.in') as fin:
    num_segments = int(fin.readline())
    segments = {}  # (length, connections_left, connections_right)
    for i in range(num_segments):
      segment_id, segment_length, _, _ = [int(x) for x in fin.readline().split()]
      connections_left = [int(x) for x in fin.readline().split()]
      connections_right = [int(x) for x in fin.readline().split()]
      segments[segment_id] = (segment_length, tuple(connections_left), tuple(connections_right))

  answer = inf
  for segment_id in segments:
    min_perimeter = find_min_perimeter(segment_id, segments)
    if min_perimeter < answer:
      answer = min_perimeter

  with open('fence6.out', 'w') as fout:
    fout.write(f'{answer}\n')

def find_min_perimeter(segment_id, segments):
  """
  Returns the length of the smallest loop containing segment_id.
  """
  visited = set()
  min_perimeter = [inf]  # Lists are mutable and can be shared across recursions.
  search(segment_id, segment_id, 1, 0, min_perimeter, visited, segments)
  return min_perimeter[0]

def search(start_id, current_id, search_direction, length_so_far, min_perimeter, visited, segments):
  if current_id in visited:
    # If we're back where we started, check if we've found a smaller loop.
    if current_id == start_id:
      if length_so_far < min_perimeter[0]:
        min_perimeter[0] = length_so_far
    # Either way, stop recursing.
    return

  visited.add(current_id)
  current_length = segments[current_id][0]
  neighbors = segments[current_id][search_direction]
  for neighbor in neighbors:
    if current_id in segments[neighbor][1]:
      direction = 2
    else:
      direction = 1
    search(start_id, neighbor, direction, length_so_far + current_length, min_perimeter, visited, segments)
  visited.remove(current_id)

main()