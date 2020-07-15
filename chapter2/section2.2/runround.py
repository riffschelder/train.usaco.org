"""
ID: riff.sc1
LANG: PYTHON3
TASK: runround
"""
fin = open('runround.in')  # 'round' vs. 'around', why be consistent when you can be confusing.
fout = open('runround.out', 'w')
start = int(fin.read())

def is_runaround_number(num):
  s = str(num)
  touched = [False] * len(s)
  position = 0
  while True:
    if touched[position]:  # we've been here before
      break
    touched[position] = True
    position += int(s[position])
    position %= len(s)
  return all(touched) and position == 0

def all_numbers_with_unique_digits():
  for length in range(1, 10):
    digits = [x + 1 for x in range(9)]
    yield from generate_numbers_with_unique_digits('', digits, length)

def generate_numbers_with_unique_digits(current_state, digits_left, num_digits_left):
  """
  call guarantees `digits_left` is sorted.
  `digits_left` is a list of (one-digit) ints.
  `current_state` is a str.
  """
  if num_digits_left == 0:
    yield int(current_state)
    return

  for i in range(len(digits_left)):
    new_state = current_state + str(digits_left[i])
    new_digits = digits_left[:i] + digits_left[i+1:]
    yield from generate_numbers_with_unique_digits(new_state, new_digits, num_digits_left - 1)

for num in all_numbers_with_unique_digits():
  if num <= start:
    continue
  if not is_runaround_number(num):
    continue
  fout.write(f'{num}\n')
  break
