"""
ID: riff.sc1
LANG: PYTHON3
TASK: skidesign
"""

fin = open('skidesign.in')
fout = open('skidesign.out', 'w')

num_hills = int(fin.readline())
heights = []
for i in range(num_hills):
  heights.append(int(fin.readline()))

def get_cost(heights):
  heights.sort()
  if heights[-1] - heights[0] <= 17:
    return 0

  min_cost = 100 * 100 * 1000 + 1  # more than the cost of reducing every hill from 100 to 0
  for i in range(heights[0], heights[-1]-16):  # -16 just in case I'm off by one the wrong way
    cost_at_i = try_cost(heights, i)
    if cost_at_i < min_cost:
      min_cost = cost_at_i
  return min_cost

def try_cost(heights, low_end):
  """
  all hill must be modified into range [low_end, low_end+17].
  """
  cost = 0
  for h in heights:
    if low_end <= h <= low_end + 17:
      continue
    if h < low_end:
      cost += (low_end - h) ** 2
    elif h > low_end + 17:
      cost += (h - low_end - 17) ** 2
  return cost

cost = get_cost(heights)
fout.write(f'{cost}\n')
