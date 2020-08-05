"""
ID: riff.sc1
LANG: PYTHON3
TASK: stamps
"""

# Python is once again too slow. This solution times out, but stamps.cpp passes
# easily with an identical algorithm.

def main():
  with open('stamps.in') as fin:
    (num_stamps_allowed, _) = [int(x) for x in fin.readline().split()]
    stamp_values = [int(x) for x in fin.read().split()]

  num_stamps_needed_for = []
  # no stamps are needed to make 0.
  num_stamps_needed_for.append(0)
  
  current_target = 1
  while True:
    num_stamps_needed_for_target = get_num_stamps_needed(current_target, num_stamps_needed_for, stamp_values)
    if num_stamps_needed_for_target <= num_stamps_allowed:
      num_stamps_needed_for.append(num_stamps_needed_for_target)
    else:
      # Not possible to reach target.
      break
    current_target += 1

  with open('stamps.out', 'w') as fout:
    fout.write(f'{current_target-1}\n')

def get_num_stamps_needed(target, num_stamps_needed_for, stamp_values):
  minimum = 1000
  for value in stamp_values:
    if target - value >= 0 and num_stamps_needed_for[target-value] < minimum:
        minimum = num_stamps_needed_for[target-value]
  return minimum + 1


from time import time
start = time()
main()
print(f'{time() - start}')