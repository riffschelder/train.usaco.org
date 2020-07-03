"""
ID: riff.sc1
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in')
fout = open('gift1.out', 'w')

def get_stuff(line):
  """
  receives '200 3\n'
  returns (200, 3)
  """
  l = line.split()
  return (int(l[0]), int(l[1]))

# [:-1] removes the newline character
num_people = int(fin.readline()[:-1])
names = []  # remember order of names presented
accounts = {}
for i in range(num_people):
  name = fin.readline()[:-1]
  names.append(name)
  accounts[name] = 0

for i in range(num_people):
  giver = fin.readline()[:-1]
  (total, ways) = get_stuff(fin.readline())
  if ways != 0:
    per_person = total // ways
    leftover = total % ways

    accounts[giver] -= total
    accounts[giver] += leftover

    for j in range(ways):
      receiver = fin.readline()[:-1]
      accounts[receiver] += per_person
  
  else:
    accounts[giver] += total

for i in range(num_people):
  fout.write('{} {}\n'.format(names[i], accounts[names[i]]))