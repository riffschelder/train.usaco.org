"""
ID: riff.sc1
LANG: PYTHON3
TASK: combo
"""

fin = open('combo.in')
fout = open('combo.out', 'w')

max_dial = int(fin.readline()[:-1])
(a, b, c) = [int(x) for x in fin.readline().split()]
(x, y, z) = [int(x) for x in fin.readline().split()]

def get_distance(n, m):
  naive_distance = max(n, m) - min(n, m)
  complement = max_dial - naive_distance
  return min(naive_distance, complement)

def get_overlap(n, m):
  overlap = 5 - get_distance(n, m)
  if overlap < 0:
    return 0
  if overlap > max_dial:
    return max_dial
  return overlap

num_common_combos = get_overlap(a, x) * get_overlap(b, y) * get_overlap(c, z)
num_combos = 2 * min(max_dial, 5) ** 3 - num_common_combos

fout.write('{}\n'.format(num_combos))