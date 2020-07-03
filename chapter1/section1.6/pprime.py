"""
ID: riff.sc1
LANG: PYTHON3
TASK: pprime
"""

fin = open('pprime.in')
fout = open('pprime.out', 'w')

(low, high) = [int(x) for x in fin.readline().split()]
prime_numbers = [2, 3]

def is_prime(num):
  for prime in prime_numbers:
    if prime * prime > num:
      break
    if num % prime == 0:
      return False
  return True

def all_numbers(length):
  """
  assuming length >= 1, generates all numbers from 10000... to 99999....
  """
  start = 1 * (10 ** (length - 1))
  stop = (10 ** length) - 1
  for i in range(start, stop + 1):
    yield i

def palindromes():
  # all single digit numbers are palindromes. easier to hard-code.
  for i in range(1, 10):
      yield i

  # this should yield all palindromes in ascending order.
  for length in range(2, 10):
    for front_half in all_numbers(length // 2):
      front_half_str = str(front_half)
      back_half_str = front_half_str[::-1]
      if length % 2 == 0:
        yield int(front_half_str + back_half_str)
      else:
        for middle_digit in range(0, 10):
          yield int(front_half_str + str(middle_digit) + back_half_str)

# generate all necessary primes
for num in range(5, int(high ** 0.5) + 1):
  if is_prime(num):
    prime_numbers.append(num)

for num in palindromes():
  if num < low:
    continue
  if num > high:
    break
  if is_prime(num):
    fout.write(f'{num}\n')