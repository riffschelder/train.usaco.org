"""
ID: riff.sc1
LANG: PYTHON3
TASK: fence9
"""
def main():
  with open('fence9.in') as fin:
    (top_x, top_y, base_x) = [int(x) for x in fin.read().split()]

  count = 0
  # Left half.
  for height in range(1, top_y):
    x = top_x * height // top_y
    count += top_x - x

  # Right half.
  base = base_x - top_x
  for height in range(1, top_y):
    x = base * height // top_y
    count += base - x

  # We counted the "spine" twice, so we take one out.
  # This also happens to work if top_x == 0 or top_x == base_x (in which cases
  # the points on the "spine" fall on the edge and should be deducted).
  count -= top_y - 1

  with open('fence9.out', 'w') as fout:
    fout.write(f'{count}\n')

main()