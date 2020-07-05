"""
ID: riff.sc1
LANG: PYTHON3
TASK: sort3
"""

fin = open('sort3.in')
fout = open('sort3.out', 'w')

length = int(fin.readline())
sequence = []
for i in range(length):
  sequence.append(int(fin.readline()) - 1)  # change numbers to 0/1/2 for easier handling

zeros = sequence.count(0)
ones = sequence.count(1)
twos = sequence.count(2)

# placement[x][y] == n means there are n y's in the x section.
placement = [[0] * 3 for _ in range(3)]

for i in range(zeros):
  placement[0][sequence[i]] += 1
for i in range(zeros, zeros + ones):
  placement[1][sequence[i]] += 1
for i in range(zeros + ones, length):
  placement[2][sequence[i]] += 1

total_swaps = 0
total_remainder = 0

def swap(x, y):
  global placement
  global total_swaps
  global total_remainder

  can_swap = min(placement[x][y], placement[y][x])
  placement[x][y] -= can_swap
  placement[y][x] -= can_swap
  total_swaps += can_swap
  total_remainder += max(placement[x][y], placement[y][x])

# direct swaps
swap(0, 1)
swap(0, 2)
swap(1, 2)

# indirect swaps
total_swaps += total_remainder // 3 * 2

fout.write(f'{total_swaps}\n')

