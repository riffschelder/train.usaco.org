"""
ID: riff.sc1
LANG: PYTHON3
TASK: msquare
"""
def main():
  with open('msquare.in') as fin:
    target = tuple([int(x) for x in fin.read().split()])

  answer = None
  initial_configuration = (1, 2, 3, 4, 5, 6, 7, 8)
  if initial_configuration == target:
    answer = ''

  seen = set(initial_configuration)
  frontier = [(initial_configuration, '')]
  while answer is None:
    (old_configuration, old_sequence) = frontier.pop(0)
    for operation in 'ABC':
      new_sequence = old_sequence + operation
      new_configuration = transform(old_configuration, operation)
      if new_configuration in seen:
        continue
      if new_configuration == target:
        answer = new_sequence
      frontier.append((new_configuration, new_sequence))
      seen.add(new_configuration)

  # Problem statement guarantees an answer can be found.
  with open('msquare.out', 'w') as fout:
    fout.write(f'{len(answer)}\n')
    lines = [answer[i:i+60] for i in range(0, len(answer), 60)]
    if not lines:
      fout.write('\n')
    else:
      for line in lines:
        fout.write(f'{line}\n')


def transform(old_configuration, operation):
  """
  Caller guarantees operation == 'A' or 'B' or 'C'.
  """
  (a, b, c, d, e, f, g, h) = old_configuration
  if operation == 'A':
    return (h, g, f, e, d, c, b, a)
  elif operation == 'B':
    return (d, a, b, c, f, g, h, e)
  else:  # operation == 'C'
    return (a, g, b, d, e, c, f, h)

main()
