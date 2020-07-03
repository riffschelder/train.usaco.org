"""
ID: riff.sc1
LANG: PYTHON3
TASK: crypt1
"""

fin = open('crypt1.in')
fout = open('crypt1.out', 'w')

_ = fin.readline()  # burn first line as it's not useful
digits_allowed = fin.readline().split()  # strings, not ints

 #    * * *   <-- call this number a
 # x    * *   <--                  b
 #  -------
 #    * * *   <--                  c
 #  * * *     <--                  d
 #  -------
 #  * * * *   <--                  e

possible_a = [x + y + z for x in digits_allowed for y in digits_allowed for z in digits_allowed]
possible_b = [x + y for x in digits_allowed for y in digits_allowed]

def check_digits(num, length):
  if len(str(num)) != length:
    return False
  for char in str(num):
    if char not in digits_allowed:
      return False
  return True

from itertools import product as get_product
solutions_count = 0

for a, b in get_product(possible_a, possible_b):
  if not check_digits(int(a) * int(b[0]), 3):
    continue
  if not check_digits(int(a) * int(b[1]), 3):
    continue
  if not check_digits(int(a) * int(b), 4):
    continue
  solutions_count += 1

fout.write('{}\n'.format(solutions_count))