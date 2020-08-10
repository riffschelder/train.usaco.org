"""
ID: riff.sc1
LANG: PYTHON3
TASK: fact4
"""
def main():
  with open('fact4.in') as fin:
    N = int(fin.read())

  last_digit = 1
  twos = 0
  fives = 0
  for i in range(1, N+1):  # 1..N inclusive.
    current = i
    while current % 2 == 0:
      current //= 2  # Don't involve float points.
      twos += 1
    while current % 5 == 0:
      current //= 5
      fives += 1
    last_digit *= current
    last_digit %= 10

  # I think we'll always have twos > fives, but I can't prove it.
  if twos > fives:
    diff = twos - fives
    for _ in range(diff):
      last_digit *= 2
      last_digit %= 10
  else:
    diff = fives - twos
    for _ in range(diff):
      last_digit *= 5
      last_digit %= 10

  with open('fact4.out', 'w') as fout:
    fout.write(f'{last_digit}\n')


main()
