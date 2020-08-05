"""
ID: riff.sc1
LANG: PYTHON3
TASK: inflate
"""

# Python is simply too slow for this problem. This program times out on the
# USACO grader on the larger test cases, while inflate.cpp (included in the
# repo) passes easily using an identical algorithm.
#
# I've tried to optimize this python program even at the cost of readability,
# and it still takes too long to run. If there's a clever trick I haven't
# thought of, please let me know.

def main():
  fin = open('inflate.in')
  (total_time, num_problems) = [int(x) for x in fin.readline().split()]

  # memo[t] is the best score achievable in t time.
  memo = [0 for _ in range(total_time + 1)]
  for _ in range(num_problems):
    (points, minutes) = [int(x) for x in fin.readline().split()]
    for t in range(minutes, total_time + 1):
      if memo[t] < memo[t-minutes] + points:
        memo[t] = memo[t-minutes] + points

  with open('inflate.out', 'w') as f:
    f.write(f'{memo[total_time]}\n')

main()
