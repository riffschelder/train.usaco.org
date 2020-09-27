"""
ID: riff.sc1
LANG: PYTHON3
TASK: stall4
"""
def main():
  with open('stall4.in') as fin:
    num_cows, num_stalls = [int(x) for x in fin.readline().split()]
    preference_of = {}
    for i in range(num_cows):
      preference_of[i] = set([int(x) for x in fin.readline().split()][1:])

  answer = 0
  assignment = {}  # stall: cow
  for i in range(num_cows):
    unavailable = set()
    if vacancy_exists(i, assignment, preference_of, unavailable):
      answer += 1

  with open('stall4.out', 'w') as fout:
    fout.write(f'{answer}\n')

def vacancy_exists(cow, assignment, preference_of, unavailable):
  for stall in preference_of[cow]:
    # Make sure we're not in a scoot-loop.
    if stall in unavailable:
      continue
    # Either we're taking this stall (so another cow can't scoot over to this
    # stall), or a cow is already here and won't scoot over (so we can't take
    # this stall). Either way, we shouldn't try this stall again in recursion.
    unavailable.add(stall)
    # If the stall's not taken yet, take it.
    if stall not in assignment:
      assignment[stall] = cow
      return True
    # If the stall's occupied, see if we can make the cow there scoot over.
    # Remember we've already marked the current stall unavailable.
    elif vacancy_exists(assignment[stall], assignment, preference_of, unavailable):
      assignment[stall] = cow
      return True
  return False

main()