"""
ID: riff.sc1
LANG: PYTHON3
TASK: ditch
"""
from math import inf

kMaxNodes = 200

def main():
  with open('ditch.in') as fin:
    num_edges, num_nodes = [int(x) for x in fin.readline().split()]
    graph = [[0 for _ in range(kMaxNodes)] for _ in range(kMaxNodes)]
    source = 0
    sink = num_nodes - 1
    for _ in range(num_edges):
      a, b, capacity = [int(x) for x in fin.readline().split()]
      # From problem statement: 
      # "Note however, that there can be more than one ditch between two intersections."
      # I debugged for hours before I realized my mistake. Hours. For this.
      graph[a-1][b-1] += capacity

  initial = sum(graph[sink])  # Might not be 0.

  while True:
    path = find_path(graph, source, sink)
    if path is None:
      break
    augment_graph(graph, path)

  answer = sum(graph[sink]) - initial
  with open('ditch.out', 'w') as fout:
    fout.write(f'{answer}\n')

def find_path(graph, source, sink):
  """
  Dijkstra's where "distance" = max throughput from source to this node.
  """
  prev = [None for _ in range(kMaxNodes)]
  prev[source] = source

  throughput = [0 for _ in range(kMaxNodes)]
  throughput[source] = inf

  visited = set()
  frontier = set([source])
  while True:
    if not frontier:
      break

    # Pick the node in frontier with max throughput.
    # Could have used a heap.
    max_throughput = (None, -inf)
    for node in frontier:
      if throughput[node] > max_throughput[1]:
        max_throughput = (node, throughput[node])

    current = max_throughput[0]
    frontier.remove(current)
    visited.add(current)
    if current == sink:
      break

    current_throughput = max_throughput[1]
    for i in range(kMaxNodes):
      if min(graph[current][i], current_throughput) > throughput[i]:
        throughput[i] = min(graph[current][i], current_throughput)
        prev[i] = current
        frontier.add(i)

  if sink not in visited:
    return None

  path = [sink]
  while True:
    if path[0] == source:
      break
    path.insert(0, prev[path[0]])
  return path

def augment_graph(graph, path):
  # Find bottleneck.
  bottleneck = inf
  for (a, b) in zip(path, path[1:]):
    if graph[a][b] < bottleneck:
      bottleneck = graph[a][b]

  # Modify graph.
  for (a, b) in zip(path, path[1:]):
    graph[a][b] -= bottleneck
    graph[b][a] += bottleneck

main()