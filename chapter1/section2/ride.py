"""
ID: riff.sc1
LANG: PYTHON3
TASK: ride
"""

def get_product(line):
  product = 1
  for char in line:
    if char == '\n':
      break
    product *= (ord(char) - ord('A') + 1)
  return product

fin = open('ride.in')
fout = open('ride.out', 'w')

first_line = fin.readline()
second_line = fin.readline()
fin.close()

first_line_product = get_product(first_line)
second_line_product = get_product(second_line)

if first_line_product % 47 == second_line_product % 47:
  fout.write('GO\n')
else:
  fout.write('STAY\n')

fout.close()