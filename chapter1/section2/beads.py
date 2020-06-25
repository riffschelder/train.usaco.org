"""
ID: riff.sc1
LANG: PYTHON3
TASK: beads
"""
fin = open('beads.in')
fout = open('beads.out', 'w')

num_beads = int(fin.readline()[:-1])
beads = fin.readline()[:-1]
beads_twice = beads+beads

def get_length(beads):
  front = get_front(beads)
  back = get_front(beads[::-1])
  if front + back > num_beads:
    return num_beads
  else:
    return front+back

def get_front(beads):
  color = beads[0]
  length = 0
  for bead in beads:
    if bead == color or bead == 'w':
      length += 1
    else:
      if color == 'w':
        color = bead
        length += 1
      else:
        break
  return length

max_length = 0
for i in range(num_beads):
  l = get_length(beads_twice[i:num_beads+i])
  if l > max_length:
    max_length = l

fout.write('{}\n'.format(max_length))