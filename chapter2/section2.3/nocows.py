"""
ID: riff.sc1
LANG: PYTHON3
TASK: nocows
"""
fin = open('nocows.in')
fout = open('nocows.out', 'w')
(num_total_cows, tree_height) = [int(x) for x in fin.read().split()]

# answer[(c, h)] is the solution to this problem when there are c cows and the
# required tree is h tall.
answer = {}
# memo[(c, h)] is sum(answer[(c, i)]) for 0 <= i <= h. keeping track of this
# allows us to avoid repeated summations of the same numbers that come up in the algorithm.
memo = {}

# base cases
answer[(1, 1)] = 1  # there's one way to put one cow in a 1-tall tree.
answer[(1, 0)] = 0  # there's no way to put one cow in a 0-tall tree.
for i in range(2, num_total_cows + 1):
  answer[(i, 1)] = 0  # there's no way to put more than one cow in a 1-tall tree.
  answer[(i, 0)] = 0  # or a 0-tall tree.

for i in range(1, num_total_cows + 1):
  memo[(i, 0)] = 0  # == answer[(i, 0)]
  memo[(i, 1)] = answer[(i, 1)]  # == answer[(i, 0)] + answer[(i, 1)]

# fill up the rest of the table
for height in range(2, tree_height + 1):
  for num_cows in range(1, num_total_cows + 1):
    count = 0
    # if we have more cows than there are nodes in a tree, there can't be a solution.
    # keep the count at 0 and skip straight to populating `answer` and `memo`.
    # this saves a fraction of a tenth of a second but brings the run time of the
    # (c = 199, h = 99) test case under the 1s cutoff (from 1.027 secs to 0.998 secs).
    #
    # incorporating an important insight from the post-solve analysis:
    # there are no solutions when num_cows is even.
    # this cuts runtime in half and brings the 0.998-sec solution to 0.525 secs.
    # (the "more cows than spots in the tree" check is therefore no longer necessary,
    # but I'm keeping it here for posterity.)
    if num_cows <= 2 ** height - 1 and num_cows % 2 == 1:
      for num_cows_left in range(1, num_cows - 1):  # [1, num_cows - 2] inclusive
        # each side must have at least one cow
        num_cows_right = (num_cows - 1) - num_cows_left
        
        # we'll do the equivalent of this, but without the repeated arithmetic.
        ##
        ## # one side has to be of height height - 1. suppose it's the left side.
        ## # if the right side is shorter, swapping sides is also a valid solution.
        ## for height_right in range(1, height - 1):  
        ##   count += answer[(num_cows_left, height_left)] * answer[(num_cows_right, height_right)] * 2
        ## # if the right side is also of height height - 1, don't double count.
        ## height_right = height - 1
        ## count += answer[(num_cows_left, height_left)] * answer[(num_cows_right, height_right)]
        count += answer[(num_cows_left, height - 1)] * (memo[(num_cows_right, height - 1)] + memo[(num_cows_right, height - 2)])
    answer[(num_cows, height)] = count
    memo[(num_cows, height)] = memo[(num_cows, height-1)] + count

final_answer = answer[(num_total_cows, tree_height)]
fout.write(f'{final_answer % 9901}\n')