"""
ID: riff.sc1
LANG: PYTHON3
TASK: fence
"""
from collections import defaultdict

def main():
  with open('fence.in') as fin:
    num_fences = int(fin.readline())
    fences = defaultdict(list)  # {1: [2, 3], ...}
    for _ in range(num_fences):
      (a, b) = [int(x) for x in fin.readline().split()]
      fences[a].append(b)
      fences[b].append(a)

  intecsections_with_odd_degrees = []
  for (intersection, connections) in fences.items():
    # Sort the connections so we always pop() the lowest-numbered one.
    connections.sort(reverse=True)
    if len(connections) % 2 == 1:
      intecsections_with_odd_degrees.append(intersection)

  start = None
  # Problem statement guarantees a solution, so there's either 0 or 2
  # intersections with odd degrees.
  if len(intecsections_with_odd_degrees) > 0:  # i.e. == 2
    start = min(intecsections_with_odd_degrees)
  else:
    start = min(fences)  
  
  visited = [start]
  path = []
  current = start
  while True:
    # `next` is a keyword in python, so I'm calling it `next_up` instead.
    if fences[current]:
      next_up = fences[current].pop()
      fences[next_up].remove(current)
      visited.append(next_up)
      current = next_up
    else:
      path.append(visited.pop())
      if visited:
        current = visited[-1]
      else:
        break

  # reversed(path) is also a legal path, and because we've always picked the
  # lowest-numbered connection at every choice, it'll actually be the correctly
  # ordered path the problem required.
  with open('fence.out', 'w') as fout:
    for intersection in reversed(path):
      fout.write(f'{intersection}\n')

main()