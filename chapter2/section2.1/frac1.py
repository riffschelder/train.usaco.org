"""
ID: riff.sc1
LANG: PYTHON3
TASK: frac1
"""
# This solution doesn't use float-point numbers, or list.sort().
# probably could have used a heap or something for the priority queue, but whatevs.

from math import gcd

# fractions[n][m] represents m/n.
max_denominator = 160  # problem guarantees denominator <= 160.
fractions = []
for denominator in range(max_denominator + 1):
  # 0 cannot be a denominator.
  # 0/1 is always the first element and 1/1 is always the last. Hardcode them when writing out answers.
  if denominator == 0 or denominator == 1:
    fractions.append(None)
    continue

  fractions.append([])
  for numerator in range(1, denominator):
    if gcd(numerator, denominator) == 1:
      fractions[denominator].append(numerator)

ordered_denominators = []  # denominators, 2..160 inclusive, ordered by their next smallest fraction.
for i in range(max_denominator, 1, -1):
  ordered_denominators.append(i)

def is_smaller(m, n, x, y):
  """
  returns true if m/n is smaller than x/y.
  they're guaranteed to be not equal because they're both reduced fractions.
  """
  return m * y < x * n

ordered_fractions = []  # (m, n) represents m/n.
while ordered_denominators:  # while list isn't empty.
  denominator = ordered_denominators.pop(0)
  numerator = fractions[denominator].pop(0)
  ordered_fractions.append((numerator, denominator))
  # only put the denominator back in the queue if there's more fractions to be written out.
  if fractions[denominator]:
    next_numerator = fractions[denominator][0]
    inserted = False
    for i, other_denominator in enumerate(ordered_denominators):
      other_numerator = fractions[other_denominator][0]
      if is_smaller(next_numerator, denominator, other_numerator, other_denominator):
        ordered_denominators.insert(i, denominator)
        inserted = True
        break
    if not inserted:  # this is the largest fraction in the list.
      ordered_denominators.append(denominator)

fin = open('frac1.in')
fout = open('frac1.out', 'w')
max_denominator = int(fin.readline())

fout.write('0/1\n')
for fraction in ordered_fractions:
  if fraction[1] <= max_denominator:
    fout.write(f'{fraction[0]}/{fraction[1]}\n')
fout.write('1/1\n')
