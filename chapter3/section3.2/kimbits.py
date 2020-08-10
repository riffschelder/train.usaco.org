"""
ID: riff.sc1
LANG: PYTHON3
TASK: kimbits
"""
from math import comb  # Requires python >= 3.8

def main():
  with open('kimbits.in') as fin:
    (num_bits, max_ones, target) = [int(x) for x in fin.read().split()]

  answer = ''
  for _ in range(num_bits):
    # How many possibilities are there if the highest bit is 0?
    halfway = num_possibilities(num_bits - 1, max_ones)
    # Highest bit is 1 if target > number of possibilities.
    if target > halfway:
      answer += '1'
      (num_bits, max_ones, target) = (num_bits - 1, max_ones - 1, target - halfway)
    else:
      answer += '0'
      (num_bits, max_ones, target) = (num_bits - 1, max_ones, target)

  with open('kimbits.out', 'w') as fout:
    fout.write(f'{answer}\n')

def num_possibilities(num_bits, max_ones):
  """
  How many strings are there with a total of `num_bits` bits, of which at most
  'max_ones' are 1?
  Caller guarantees max_ones <= num_bits.
  """
  answer = 0
  for i in range(max_ones + 1):  # 0..max_ones inclusive.
    answer += comb(num_bits, i)
  return answer

main()