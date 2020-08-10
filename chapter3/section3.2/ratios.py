"""
ID: riff.sc1
LANG: PYTHON3
TASK: ratios
"""
from math import gcd
from functools import reduce  # For repeatedly calling gcd().

def main():
  with open('ratios.in') as fin:
    (t1, t2, t3) = [int(x) for x in fin.readline().split()]
    (a1, a2, a3) = [int(x) for x in fin.readline().split()]
    (b1, b2, b3) = [int(x) for x in fin.readline().split()]
    (c1, c2, c3) = [int(x) for x in fin.readline().split()]

  # Solve matrix:
  # a1 b1 c1     x     t1
  # a2 b2 c2  .  y  =  t2
  # a3 b3 c3     z     t3
  # then multiply (x, y, z) by some integer so that all three become positive integers.
  # Call this equation Ax = t (A is a 3x3 matrix and x and t are vectors).
  
  answer = None

  # There's no solution when det(A) = 0.
  A = ((a1, b1, c1), (a2, b2, c2), (a3, b3, c3))
  detA = get_det(A)
  if detA == 0:
    answer = 'NONE'  # != python's None
  else:
    # Cramer's Rule
    # x = detX / detA, y = detY / detA, z = detZ/detA, where X, Y, Z are 
    # matrices defined below:
    X = ((t1, b1, c1), (t2, b2, c2), (t3, b3, c3))
    Y = ((a1, t1, c1), (a2, t2, c2), (a3, t3, c3))
    Z = ((a1, b1, t1), (a2, b2, t2), (a3, b3, t3))

    detX = get_det(X)
    detY = get_det(Y)
    detZ = get_det(Z)

    multiplier = detA // reduce(gcd, [detA, detX, detY, detZ])

    # gcd() always returns a positive value, so multiplier might be negative,
    # turning a positive (detX / detA) into a negative x. We'll fix this at the end.
    x = multiplier * detX // detA
    y = multiplier * detY // detA
    z = multiplier * detZ // detA
    if x >= 0 and y >= 0 and z >= 0:
      answer = f'{x} {y} {z} {multiplier}'
    elif x <=0 and y <= 0 and z <= 0:
      answer = f'{-x} {-y} {-z} {-multiplier}'
    else:
      # Can't find an all-positive (x, y, z) solution.
      answer = 'NONE'

  with open('ratios.out', 'w') as fout:
    fout.write(f'{answer}\n')

def get_det(matrix):
  # Unpack into individual numbers.
  #           a b c
  # matrix =  d e f
  #           g h i
  # Caller guarantees all nine numbers are integers.
  ((a, b, c), (d, e, f), (g, h, i)) = matrix
  det = 0
  det += a * (e * i - f * h)
  det -= b * (d * i - f * g)
  det += c * (d * h - e * g)
  return det

main()