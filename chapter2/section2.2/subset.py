"""
ID: riff.sc1
LANG: PYTHON3
TASK: subset
"""
fin = open('subset.in')
fout = open('subset.out', 'w')
max_num = int(fin.read())

memo = {}  # dynamic programming

def count_solutions(available_numbers, target_sum):
  # sets must be made immutable (i.e. frozen) to be hashable (so that they can be dict keys).
  frozen_numbers = frozenset(available_numbers)
  if (frozen_numbers, target_sum) in memo:
    return memo[(frozen_numbers, target_sum)]

  if target_sum < 0:
    return 0

  if not available_numbers:
    if target_sum == 0:
      return 1
    else:
      return 0

  num_solutions = 0
  available_numbers = available_numbers.copy()  # so that we don't have to put things back when backtracking
  arbitrary_number = available_numbers.pop()

  num_solutions += count_solutions(available_numbers, target_sum)
  num_solutions += count_solutions(available_numbers, target_sum - arbitrary_number)
  memo[(frozen_numbers, target_sum)] = num_solutions
  return num_solutions

all_numbers = set(i + 1 for i in range(max_num))
full_sum = sum(all_numbers)

if full_sum & 1:
  fout.write('0\n')
else:
  half_sum = full_sum // 2
  # only count solutions with 1 in them (every partition has exactly one half that contains 1)
  num_solutions = count_solutions(all_numbers - {1}, half_sum - 1)
  fout.write(f'{num_solutions}\n')