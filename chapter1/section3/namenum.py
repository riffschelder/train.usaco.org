"""
ID: riff.sc1
LANG: PYTHON3
TASK: namenum
"""
fin = open('namenum.in')
fout = open('namenum.out', 'w')
fdict = open('dict.txt')

names = fdict.read()
names = names.split()

serial_number = fin.read()[:-1]
length = len(serial_number)
names = [name for name in names if len(name) == length]

def is_good(name):
  corresponding_number = ''
  for char in name:
    corresponding_number += char_to_num(char)
  if corresponding_number == serial_number:
    return True
  else:
    return False

def char_to_num(char):
  if char in ['A', 'B', 'C']:
    return '2'
  if char in ['D', 'E', 'F']:
    return '3'
  if char in ['G', 'H', 'I']:
    return '4'
  if char in ['J', 'K', 'L']:
    return '5'
  if char in ['M', 'N', 'O']:
    return '6'
  if char in ['P', 'R', 'S']:
    return '7'
  if char in ['T', 'U', 'V']:
    return '8'
  if char in ['W', 'X', 'Y']:
    return '9'
  return '-'  # guaranteed not to match a serial number


good_names = []
for name in names:
  if is_good(name):
    good_names.append(name)

if len(good_names) == 0:
  fout.write('NONE\n')
else:
  good_names.sort()
  for name in good_names:
    fout.write('{}\n'.format(name))
