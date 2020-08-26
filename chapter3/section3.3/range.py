"""
ID: riff.sc1
LANG: PYTHON3
TASK: range
"""

# This solution is too slow, but I believe it's correct.

def main():
  with open('range.in') as fin:
    farm_size = int(fin.readline())
    farm = []
    for _ in range(farm_size):
      farm.append(fin.readline().strip())

  # squares_of_size[n] is a 2D boolean array. squares_of_size[n][i][j] is True
  # iff the n by n square whose top-left corner is (i, j) is good for grazing.
  squares_of_size = {}
  size_two_squares = [[True for _ in range(farm_size - 1)] 
                            for _ in range(farm_size - 1)]
  squares_of_size[2] = size_two_squares

  for i in range(farm_size):
    for j in range(farm_size):
      if farm[i][j] == '0':
        invalidate(size_two_squares, i, j)

  for size in range(3, farm_size + 1):  # 3 .. farm_size inclusive
    bigger_squares = [[True for _ in range(farm_size - size + 1)] 
                            for _ in range(farm_size - size + 1)]
    squares_of_size[size] = bigger_squares
    smaller_squares = squares_of_size[size - 1]

    # Build 3x3 squares from 2x2 squares, etc.
    for i in range(farm_size - size + 2):  # farm_size - (size - 1) + 1
      for j in range(farm_size - size + 2):
        if not smaller_squares[i][j]:
          invalidate(bigger_squares, i, j)

  with open('range.out', 'w') as fout:
    for size in range(2, farm_size + 1):  # 2 .. farm_size inclusive
      num_good_squares = count_good_squares(squares_of_size[size])
      if num_good_squares > 0:
        fout.write(f'{size} {num_good_squares}\n')

def count_good_squares(squares):
  answer = 0
  for row in squares:
    answer += row.count(True)
  return answer

def invalidate(squares, row, col):
  size = len(squares)
  for i in range(row - 1, row + 1):  # (row - 1) .. row inclusive
    for j in range(col - 1, col + 1):
      if 0 <= i < size and 0 <= j < size:
        squares[i][j] = False

from time import time
start = time()
main()
print(f'{time() - start}')