"""
ID: riff.sc1
LANG: PYTHON3
TASK: spin
"""
from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Wheel:
  speed : int = 0
  wedges : List[Tuple[int, int]] = field(default_factory=list)  # Ugly python.

def main():
  wheels = [Wheel() for _ in range(5)]
  with open('spin.in') as fin:
    lines = fin.readlines()
  for i, line in enumerate(lines):
    data = [int(x) for x in line.split()]
    wheels[i].speed = data[0]
    for j in range(2, len(data), 2):
      begin = data[j]
      end = begin + data[j+1]  # Possibly >= 360.
      wheels[i].wedges.append((begin, end))

  best_time = -1
  for time in range(360):
    # It might loop sooner but definitely not later.
    if wheels_are_aligned(wheels, time):
      best_time = time
      break

  with open('spin.out', 'w') as fout:
    if best_time < 0:
      fout.write('none\n')
    else:
      fout.write(f'{best_time}\n')

def wheels_are_aligned(wheels, time):
  still_possible = [True] * 360
  for wheel in wheels:
    movement = (wheel.speed * time) % 360
    is_open = [False] * 360
    for (begin, end) in wheel.wedges:
      for degree in range(begin, end+1):
        is_open[(degree + movement) % 360] = True
    for i in range(360):
      still_possible[i] &= is_open[i]
  return any(still_possible)

main()