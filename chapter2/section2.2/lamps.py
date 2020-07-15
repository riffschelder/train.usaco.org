"""
ID: riff.sc1
LANG: PYTHON3
TASK: lamps
"""
from itertools import combinations

fin = open('lamps.in')
fout = open('lamps.out', 'w')

num_lamps = int(fin.readline())
num_button_presses = int(fin.readline())
on_lamps = [int(x) for x in fin.readline().split() if int(x) != -1]
off_lamps = [int(x) for x in fin.readline().split() if int(x) != -1]

def press_button(lamps, button):
  """
  caller guarantees `lamps` is an array of length `num_lamps` and each element is 0 or 1.
  """
  if button == 1:
    for i, _ in enumerate(lamps):
      lamps[i] = 1 - lamps[i]
  if button == 2:
    # lamps here are 0-indexed but 1-indexed in the problem, so odd/even are reversed
    for i, _ in enumerate(lamps):
      if i % 2 == 0:
        lamps[i] = 1 - lamps[i]
  if button == 3:
    for i, _ in enumerate(lamps):
      if i % 2 == 1:
        lamps[i] = 1 - lamps[i]
  if button == 4:
    for i, _ in enumerate(lamps):
      if i % 3 == 0:
        lamps[i] = 1 - lamps[i]
  return lamps

def press_buttons(lamps, buttons):
  lamps = lamps.copy()
  for button in buttons:
    press_button(lamps, button)
  return lamps

def follows_requirement(lamps, on_lamps, off_lamps):
  for i in on_lamps:
    if lamps[i-1] == 0:
      return False
  for i in off_lamps:
    if lamps[i-1] == 1:
      return False
  return True

lamps = [1] * num_lamps  # lamps repeat in cycles of six, but num_lamps <= 100 so whatever.

final_states = []
for i in range(5):
  # if a state is achievable in N button presses, it's achieveable in N + 2k button presses
  if not (i <= num_button_presses and (num_button_presses - i) % 2 == 0):
    continue
  for button_presses in combinations(range(1, 5), i):
    final_states.append(press_buttons(lamps, button_presses))

final_states = [x for x in final_states if follows_requirement(x, on_lamps, off_lamps)]
if not final_states:
  fout.write('IMPOSSIBLE\n')
else:
  final_state_strings = []
  for state in final_states:
    final_state_strings.append(''.join([str(x) for x in state]))
  final_state_strings.sort()
  for state in final_state_strings:
    fout.write(f'{state}\n')
