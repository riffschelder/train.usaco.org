"""
ID: riff.sc1
LANG: PYTHON3
TASK: barn1
"""

fin = open('barn1.in')
fout = open('barn1.out', 'w')

def get_numbers(line):
  return [int(x) for x in line.split()]

(max_boards, num_stalls, num_cows) = get_numbers(fin.readline())
occupied = []
for i in range(num_cows):
  occupied.append(int(fin.readline()[:-1]))
occupied.sort()  # just in case (not guaranteed by problem statement)

num_boards_used = 1
num_stalls_blocked = occupied[-1] - occupied[0] + 1

gaps = []
for i, j in zip(occupied, occupied[1:]):
  gap = j - i - 1
  if gap > 0:
    gaps.append(gap)
gaps.sort(reverse=True)

for i in range(min(max_boards - num_boards_used, len(gaps))):
  num_stalls_blocked -= gaps[i]

fout.write('{}\n'.format(num_stalls_blocked))
