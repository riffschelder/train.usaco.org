"""
ID: riff.sc1
LANG: PYTHON3
TASK: agrinet
"""
from math import inf

def main():
  with open('agrinet.in') as fin:
    num_farms = int(fin.readline())
    distances = fin.read().split()
    
  distance_between = []
  for i in range(num_farms):
    distances_from_i = []
    for j in range(num_farms):
      distances_from_i.append(int(distances[i * num_farms + j]))
    distance_between.append(distances_from_i)

  cost_to_connect = [inf for _ in range(num_farms)]
  cost_to_connect[0] = 0
  is_connected = [False for _ in range(num_farms)]
  total_cost = 0

  while True:
    farm = find_farm(cost_to_connect, is_connected)
    if farm is None:
      break
    is_connected[farm] = True
    total_cost += cost_to_connect[farm]

    for i in range(num_farms):
      if not is_connected[i] and distance_between[farm][i] < cost_to_connect[i]:
        cost_to_connect[i] = distance_between[farm][i]

  with open('agrinet.out', 'w') as fout:
    fout.write(f'{total_cost}\n')

def find_farm(cost_to_connect, is_connected):
  """
  Find the cheapest farm that's not already connected.
  Caller guarantees the two lists have the same length.
  """
  cheapest = (None, inf)  # (farm, cost)
  for (i, cost) in enumerate(cost_to_connect):
    if is_connected[i]:
      continue
    if cost_to_connect[i] < cheapest[1]:
      cheapest = (i, cost_to_connect[i])
  return cheapest[0]

main()