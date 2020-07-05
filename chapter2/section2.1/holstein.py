"""
ID: riff.sc1
LANG: PYTHON3
TASK: holstein
"""
fin = open('holstein.in')
fout = open('holstein.out', 'w')

num_vitamin_types = int(fin.readline())
vitamin_demand = tuple(int(x) for x in fin.readline().split())
num_feed_types = int(fin.readline())
feed_specs = []
for i in range(num_feed_types):
  feed_specs.append(tuple(int(x) for x in fin.readline().split()))

def is_good_enough(supply, demand):
  for sup, dem in zip(supply, demand):
    if sup < dem:
      return False
  return True

good_combinations = []
for combination in range(1, 1 << num_feed_types):  # demand cannot be 0.
  feeds_taken = [feed for i, feed in enumerate(feed_specs) if (1 << i & combination)]
  vitamin_supply = tuple(sum(contents) for contents in zip(*feeds_taken))
  if is_good_enough(vitamin_supply, vitamin_demand):
    good_combinations.append(combination)

def decode_combination(combination):
  feed_types_used = 0
  feed_types = []
  for i in range(num_feed_types):
    if combination & 1 << i:
      feed_types_used += 1
      feed_types.append(str(i + 1))
  return (feed_types_used, feed_types)

good_combinations.sort(key=decode_combination)
best_comination = good_combinations[0]
(min_num_types, feed_types) = decode_combination(best_comination)
fout.write(f'{min_num_types} {" ".join(feed_types)}\n')