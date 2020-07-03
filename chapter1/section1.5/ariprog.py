"""
ID: riff.sc1
LANG: PYTHON3
TASK: ariprog
"""

fin = open('ariprog.in')
fout = open('ariprog.out', 'w')

N = int(fin.readline())  # sequence length
M = int(fin.readline())  # bisquare limit
max_bisquare = M * M * 2  # min_bisquare is 0

# we need a set of all bisquares to test if a number is a bisquare.
bisquares_set = set()
for i in range(M+1):
  for j in range(i, M+1):
    bisquare = i * i + j * j
    bisquares_set.add(bisquare)

def is_solution(start, step):
  # since larger bisquares are sparser, checking backward finds failures slightly faster.
  for num_steps in range(N-1, 0, -1):
    candidate = start + num_steps * step
    if candidate not in bisquares_set:
      return False
  # no need to check `start`; we only ever start from a bisquare.
  return True

# nothing clever here; pick two bisquares and see if there's a sequence that starts with them two.
# using a sorted list helps eliminate impossible starting pairs faster.
# this solution takes 4.913 seconds to run on USACO's grading server for N = 22 and M = 250 (juuust under limit).
bisquares_list = list(bisquares_set)
bisquares_list.sort()
solutions = []
for i, first_item in enumerate(bisquares_list[:-1]):  # first_item cannot be the largest bisquare
  for second_item in bisquares_list[i+1:]:
    step = second_item - first_item
    if first_item + (N - 1) * step > max_bisquare:
      break  # future second_items will surely be over limit as well
    if is_solution(first_item, step):
      solutions.append((first_item, step))

def flip(start_step):
  """
  output is printed in (start, step) format but sorted in dictionary order of (step, start)
  """
  (start, step) = start_step
  return (step, start)

if len(solutions) == 0:
  fout.write('NONE\n')
else:
  solutions.sort(key=flip)  # sorting takes negligible time compared to the double for-loop.
  for solution in solutions:
    fout.write(f'{solution[0]} {solution[1]}\n')