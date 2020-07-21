"""
ID: riff.sc1
LANG: PYTHON3
TASK: zerosum
"""
from itertools import product

fin = open('zerosum.in')
fout = open('zerosum.out', 'w')
N = int(fin.read())

def create_sequence(operations):
  answer = ''
  for i, op in enumerate(operations):
    answer += str(i + 1)
    answer += op
  answer += str(N)
  return answer

def is_zero_sum(operations):
  numbers = []
  operators = []
  current_number = 1
  for i, op in enumerate(operations):
    if op == ' ':
      current_number *= 10
      current_number += i + 2
    else:
      numbers.append(current_number)
      operators.append(op)
      current_number = i + 2
  numbers.append(current_number)

  answer = numbers[0]
  for num, op in zip(numbers[1:], operators):
    if op == '+':
      answer += num
    else:
      answer -= num

  if answer == 0:
    return True
  else:
    return False

zero_sums_sequences = []
for operations in product(['+', '-', ' '], repeat=N-1):
  if is_zero_sum(operations):
    zero_sums_sequences.append(create_sequence(operations))

zero_sums_sequences.sort()
for sequence in zero_sums_sequences:
  fout.write(f'{sequence}\n')

