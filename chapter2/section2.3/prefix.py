"""
ID: riff.sc1
LANG: PYTHON3
TASK: prefix
"""
fin = open('prefix.in')
fout = open('prefix.out', 'w')

all_input = fin.read().split()
dot_index = all_input.index('.')
primitives = all_input[:dot_index]
sequence = ''.join(all_input[dot_index+1:])

reachable = {}  # reachable[i] is True if sequence[:i] can be composed of primitives
reachable[0] = True
for i in range(1, len(sequence) + 1):  # [1, len(sequence)] inclusive
  reachable[i] = False
  for primitive in primitives:
    start = i - len(primitive) 
    if start < 0:  # primitive is longer than the current prefix
      continue
    if not reachable[start]:
      continue
    if sequence[start:i] == primitive:
      reachable[i] = True
      break

max_reachable = max([k for k, v in reachable.items() if v is True])
fout.write(f'{max_reachable}\n')

