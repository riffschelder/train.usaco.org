"""
ID: riff.sc1
LANG: PYTHON3
TASK: humble
"""
from heapq import heappush, heappop, heappushpop

def main():
  with open('humble.in') as fin:
    (num_primes, target) = [int(x) for x in fin.readline().split()]
    primes = [int(x) for x in fin.readline().split()]

  # 1 is explicitly not a humble number but it gives us a starting point.
  humble_numbers = [1]
  # Every new humble number is the product of a prime and an existing humble number.
  # Use a heap to find the smallest new humble number.
  # Each item is (new_humble_number, prime, index_of_old_humble_number)
  candidates = []
  for prime in primes:
    heappush(candidates, (prime, prime, 0))

  # Each loop produces a new humble number.
  for i in range(target):
    (next_humble_number, prime, index) = heappop(candidates)
    # Don't produce the same humble number twice.
    while next_humble_number <= humble_numbers[-1]:
      (next_humble_number, prime, index) = (
        heappushpop(candidates,
                    (humble_numbers[index+1] * prime, prime, index+1)))
    humble_numbers.append(next_humble_number)
    heappush(candidates, (humble_numbers[index+1] * prime, prime, index+1))
    
  with open('humble.out', 'w') as fout:
    fout.write(f'{humble_numbers[-1]}\n')

main()