"""
ID: riff.sc1
LANG: PYTHON3
TASK: nuggets
"""
from math import gcd
from functools import reduce

# Frobenius number.
# I'm surprised this solution worked; we should have run out of time if 
# 2,000,000,000 was actually the limit. Maybe given the box_size < 256 restriction,
# it can be proved that the Frobenius number will never get that high.


def main():
  with open('nuggets.in') as fin:
    _ = int(fin.readline())
    box_sizes = [int(x) for x in fin.read().split()]
    box_sizes.sort()

  answer = None
  # All purchases can be made iff 1 is one of the options.
  if box_sizes[0] == 1:
    answer = 0
  # There's no bound if gcd of all options is not 1.
  box_size_gcd = reduce(gcd, box_sizes)
  if box_size_gcd > 1:
    answer = 0

  if answer is None:
    is_possible = [True]
    for i in range(1, 2000000001):
      i_is_possible = False
      for size in box_sizes:
        if i - size >= 0 and is_possible[i-size]:
          i_is_possible = True
          break
      is_possible.append(i_is_possible)
      if i_is_possible:
        if i - answer >= box_sizes[0]:
          break
      else:
        answer = i

  with open('nuggets.out', 'w') as fout:
    fout.write(f'{answer}\n')

main()