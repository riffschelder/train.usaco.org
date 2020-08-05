"""
ID: riff.sc1
LANG: PYTHON3
TASK: contact
"""
from collections import defaultdict

def main():
  fin = open('contact.in')
  (low, high, amount_to_print) = [int(x) for x in fin.readline().split()]

  last_pattern = ['' for _ in range(13)]  # 0..12 inclusive
  frequency_of = defaultdict(int)  # frequency_of[pattern]
  while True:
    line = fin.readline().strip()
    if not line:
      break
    for char in line:
      if char not in '01':  # Skip '\n', etc.
        continue
      for i in range(1, 13):  # 1..12 inclusive
        if low <= i <= high:  # could have used range(low, high+1), in hindsight
          last_pattern[i] = new_pattern(last_pattern[i], i, char)
          record_pattern(last_pattern[i], i, frequency_of)

  patterns_at = defaultdict(list)  # patterns_at[frequency]
  just_frequencies = set()
  for pattern, frequency in frequency_of.items():
    patterns_at[frequency].append(pattern)
    just_frequencies.add(frequency)

  just_frequencies = list(just_frequencies)
  just_frequencies.sort(reverse=True)
  print_answer(patterns_at, just_frequencies, amount_to_print)

def new_pattern(pattern, length, new_char):
  pattern = pattern + new_char
  if len(pattern) > length:
    # should only be over by 1
    pattern = pattern[1:]
  return pattern

def record_pattern(pattern, length, frequency_of):
  if len(pattern) == length:
    frequency_of[pattern] += 1

def print_answer(patterns_at, sorted_frequencies, amount_to_print):
  with open('contact.out', 'w') as fout:
    for i in range(min(amount_to_print, len(sorted_frequencies))):
      frequency = sorted_frequencies[i]
      fout.write(f'{frequency}\n')
      patterns = patterns_at[frequency]
      patterns.sort(key=length_first)
      count = 0
      for pattern in patterns[:-1]:
        fout.write(f'{pattern}')
        count += 1
        if count < 6:
          fout.write(' ')
        else:
          count = 0
          fout.write('\n')
      fout.write(f'{patterns[-1]}\n')

def length_first(pattern):
  return (len(pattern), pattern)

main()