"""
ID: riff.sc1
LANG: PYTHON3
TASK: fracdec
"""
def main():
  with open('fracdec.in') as fin:
    # n for numerator, d for denominator
    (n, d) = [int(x) for x in fin.read().split()]

  # simulate long division.
  answer = str(n // d)
  answer += '.'
  if n % d == 0:
    answer += '0'
  else:
    answer += get_decimal(n % d, d)

  with open('fracdec.out', 'w') as fout:
    LINE_LENGTH = 76
    lines = [answer[i:i+LINE_LENGTH] for i in range(0, len(answer), LINE_LENGTH)]
    answer = '\n'.join(lines)
    fout.write(f'{answer}\n')

def get_decimal(n, d):
  """
  Caller guarantees 0 < n < d.
  """
  decimals = []
  remainders = []
  remainders_seen = set()  # For faster lookup.
  loop = True

  while n not in remainders_seen:
    remainders.append(n)
    remainders_seen.add(n)
    n *= 10
    decimals.append(str(n // d))
    n %= d
    if n == 0:
      loop = False
      break

  if loop:
    first_occurance = remainders.index(n)
    return ''.join(decimals[:first_occurance]) + '(' + ''.join(decimals[first_occurance:]) + ')'
  else:
    return ''.join(decimals)

main()