"""
ID: riff.sc1
LANG: PYTHON3
TASK: concom
"""
from collections import defaultdict

fin = open('concom.in')
fout = open('concom.out', 'w')

num_companies = 0
num_lines = int(fin.readline())
graph = defaultdict(dict)  # a: {b1: p1, b2: p2, ...} where a owns p% of each b (respectively)
for i in range(num_lines):
  (a, b, p) = [int(x) for x in fin.readline().split()]
  graph[a][b] = p
  num_companies = max(a, b, num_companies)

all_control_pairs = set()  # each element (a, b) indicates a controls b

def controls(a, b):
  # we'll discover controls as we travel through the graph. don't do repeated work.
  if (a, b) in all_control_pairs:
    return True

  controlled = set()  # set of companies that a controls
  shares = [0] * (num_companies + 1)  # shares[c] = p if a owns p% of c, transitiviely (as we discover them)
  controlled.add(a)  # a controls itself

  # discover more transitive controls
  middlemen = controlled.copy()  # we'll see if a controls more companies through these companies
  while middlemen:
    new_middlemen = set()
    for m in middlemen:
      for (c, p) in graph[m].items():
        shares[c] += p
        if shares[c] > 50 and c not in controlled:
          controlled.add(c)
          new_middlemen.add(c)
          all_control_pairs.add((a, c))
    middlemen = new_middlemen

  return (b in controlled)

for a in range(1, num_companies + 1):
  for b in range(1, num_companies + 1):
    if controls(a, b):
      all_control_pairs.add((a, b))  # probably unnecessaly since controls() already added all the discovered pairs.

answer = list(all_control_pairs)
answer.sort()
for (a, b) in answer:
  if a != b:
    fout.write(f'{a} {b}\n')


