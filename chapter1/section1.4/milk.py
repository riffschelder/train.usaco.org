"""
ID: riff.sc1
LANG: PYTHON3
TASK: milk
"""

fin = open('milk.in')
fout = open('milk.out', 'w')

def get_numbers(line):
  numbers = line.split()
  return (int(numbers[0]), int(numbers[1]))

first_line = fin.readline()
(amount_needed, num_farmers) = get_numbers(first_line)

supplies = []
for i in range(num_farmers):
  line = fin.readline()
  supplies.append(get_numbers(line))

fin.close()

def get_first_number(pair):
  return pair[0]

supplies.sort(key=get_first_number)

total_cost = 0
for supply in supplies:
  amount_bought = min(amount_needed, supply[1])
  total_cost += amount_bought * supply[0]
  amount_needed -= amount_bought

  if amount_needed == 0:
    break

fout.write('{}\n'.format(total_cost))
