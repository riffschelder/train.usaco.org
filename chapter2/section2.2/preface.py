"""
ID: riff.sc1
LANG: PYTHON3
TASK: preface
"""
from collections import defaultdict

fin = open('preface.in')
fout = open('preface.out', 'w')
max_page = int(fin.read())

def get_partial(unit, one, five, ten):
  partial = ''
  if unit >= 5:
    if unit == 9:
      partial += (one + ten)
    else:
      partial += five
      unit -= 5
      partial += one * unit
  else:
    if unit == 4:
      partial += (one + five)
    else:
      partial += one * unit

  return partial

def get_roman_numeral(num):
  thousands = num//1000
  num = num % 1000
  hundreds = num // 100
  num = num % 100
  tens = num // 10
  ones = num % 10

  numeral = ''
  numeral += 'M' * thousands
  numeral += get_partial(hundreds, 'C', 'D', 'M')
  numeral += get_partial(tens, 'X', 'L', 'C')
  numeral += get_partial(ones, 'I', 'V', 'X')

  return numeral


letters_count = defaultdict(int)

for i in range(max_page):
  roman_numeral = get_roman_numeral(i+1)
  for letter in roman_numeral:
    letters_count[letter] += 1

ordered_letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
for letter in ordered_letters:
  if letters_count[letter] > 0:
    fout.write(f'{letter} {letters_count[letter]}\n')

