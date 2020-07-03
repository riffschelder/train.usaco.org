"""
ID: riff.sc1
LANG: PYTHON3
TASK: milk3
"""
from __future__ import annotations  # forward class-name reference
from dataclasses import dataclass

fin = open('milk3.in')
fout = open('milk3.out', 'w')

@dataclass
class Bucket:
  capacity : int
  holding : int

  def pour_into(self, other:Bucket):
    receive_limit = other.capacity - other.holding
    transfer_amount = min(self.holding, receive_limit)
    other.holding += transfer_amount
    self.holding -= transfer_amount
    return transfer_amount

  def pour_back(self, other:Bucket, amount):
    """
    only used to undo pour_into, so not checking if `amount` overflows or overpours a bucket.
    """
    self.holding += amount
    other.holding -= amount

def search(A:Bucket, B:Bucket, C:Bucket):
  holdings = (A.holding, B.holding, C.holding)
  if holdings in visited:
    return
  visited.add(holdings)

  # try all six possible operations.
  # if we had more than three buckets, we might have needed to do something more clever.
  # but with only three buckets, it's faster to hardcode.
  amount = A.pour_into(B)
  search(A, B, C)
  A.pour_back(B, amount)

  amount = A.pour_into(C)
  search(A, B, C)
  A.pour_back(C, amount)

  amount = B.pour_into(A)
  search(A, B, C)
  B.pour_back(A, amount)

  amount = B.pour_into(C)
  search(A, B, C)
  B.pour_back(C, amount)

  amount = C.pour_into(A)
  search(A, B, C)
  C.pour_back(A, amount)

  amount = C.pour_into(B)
  search(A, B, C)
  C.pour_back(B, amount)


capacities = [int(x) for x in fin.readline().split()]
A = Bucket(capacities[0], 0)
B = Bucket(capacities[1], 0)
C = Bucket(capacities[2], capacities[2])

visited = set()
search(A, B, C)

solutions = set()
for holdings in visited:
  if holdings[0] == 0:
    solutions.add(holdings[2])

solutions = list(solutions)
solutions.sort()
fout.write('{}\n'.format(' '.join([str(s) for s in solutions])))