"""
ID: riff.sc1
LANG: PYTHON3
TASK: sprime
"""
fin = open('sprime.in')
fout = open('sprime.out', 'w')

def is_prime(num):
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True

superprime_length = int(fin.readline())
superprimes = [2, 3, 5, 7]  # one-digit superprimes

for i in range(2, superprime_length + 1):
  new_superprimes = []
  for prime in superprimes:
    for last_digit in range(10):
      if is_prime(prime * 10 + last_digit):
        new_superprimes.append(prime * 10 + last_digit)
  superprimes = new_superprimes

superprimes.sort()
for prime in superprimes:
  fout.write(f'{prime}\n')

