"""
ID: riff.sc1
LANG: PYTHON3
TASK: numtri
"""

fin = open('numtri.in')
fout = open('numtri.out', 'w')

height = int(fin.readline())
best_sums = [int(fin.readline())]  # reads first number

for i in range(1, height):
  numbers = [int(x) for x in fin.readline().split()]
  new_best_sums = []
  for j, num in enumerate(numbers):
    if j == 0:  # first number
      new_best_sums.append(numbers[0] + best_sums[0])
    elif j + 1 == len(numbers):  # last number
      new_best_sums.append(numbers[j] + best_sums[j-1])
    else:
      new_best_sums.append(numbers[j] + max(best_sums[j-1], best_sums[j]))
  best_sums = new_best_sums

fout.write(f'{max(best_sums)}\n')
