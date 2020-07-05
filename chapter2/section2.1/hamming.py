"""
ID: riff.sc1
LANG: PYTHON3
TASK: hamming
"""
fin = open('hamming.in')
fout = open('hamming.out', 'w')

(required_size, num_bits, min_dist) = [int(x) for x in fin.readline().split()]

solution = []

def is_good_codeword(num):
  """
  num has enough hamming distance from all codewords in `solution`.
  """
  for s in solution:
    if hamming_distance(s, num) < min_dist:
      return False
  return True

def hamming_distance(n, m):
  dist = 0
  for i in range(8):
    mask = 1 << i
    if n & mask != m & mask:
      dist += 1
  return dist

# because all solutions are bit-symmetric, a greedy algorithm will suffice.
for i in range(1 << num_bits):
  if is_good_codeword(i):
    solution.append(i)
    if len(solution) >= required_size:
      break

for i, num in enumerate(solution):
  fout.write(f'{num}')
  if i % 10 == 9 or i == len(solution) - 1:
    fout.write('\n')
  else:
    fout.write(' ')
