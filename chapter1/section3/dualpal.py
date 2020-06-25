"""
ID: riff.sc1
LANG: PYTHON3
TASK: dualpal
"""
fin = open('dualpal.in')
fout = open('dualpal.out', 'w')

def get_numbers(both_numbers):
  numbers = both_numbers.split()
  return (int(numbers[0]), int(numbers[1]))

both_numbers = fin.read()
fin.close()
(quota, minimum) = get_numbers(both_numbers)

def is_dual_pal(num):
  pal_count = 0
  for i in range(2, 11):  # 2 to 10 inclusive
    if is_pal_in_base(num, i):
      pal_count += 1
    if pal_count >= 2:
      return True
  return False

def is_pal_in_base(num, base):
  return is_palindrome(change_base(num, base))

# Copying three methods from palsquare, even though max base is 10.
def is_palindrome(s):
  return s == s[::-1]

def change_base(num, base):
  """
  takes in two integers
  returns a string
  """
  result = ''
  while num > 0:
    remainder = num % base
    result += get_symbol(remainder, base)
    num = num // base

  return result[::-1]

def get_symbol(num, base):
  """
  takes in two integers
  returns a character
  """
  if 0 <= num <= 9:
    return chr(ord('0') + num)
  else:
    return chr(ord('A') + num - 10)

count = 0
answers = []
i = minimum
while True:
  i += 1
  if count >= quota:
    break
  if is_dual_pal(i):
    answers.append(i)
    count += 1

for answer in answers:
  fout.write('{}\n'.format(answer))