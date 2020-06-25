"""
ID: riff.sc1
LANG: PYTHON3
TASK: palsquare
"""

fin = open('palsquare.in')
fout = open('palsquare.out', 'w')

base = int(fin.read()[:-1])
fin.close()

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

answers = []
for i in range(1, 301):  # 1 thru 300 inclusive
  square = i * i
  if(is_palindrome(change_base(square, base))):
    answers.append((change_base(i, base), change_base(square, base)))

for answer in answers:
  fout.write('{} {}\n'.format(answer[0], answer[1]))
