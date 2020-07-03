"""
ID: riff.sc1
LANG: PYTHON3
TASK: milk2
"""

fin = open('milk2.in')
fout = open('milk2.out', 'w')

num_farmers = int(fin.readline()[:-1])
ranges = []

def get_times(line):
  times = line.split()
  return (int(times[0]), int(times[1]))

def add_to_range(start, stop):
  global ranges
  start_enclosure = None
  stop_enclosure = None
  for r in ranges:  # range is a keyword
    if r[0] <= start <= r[1]:
      start_enclosure = (r[0], r[1])
    if r[0] <= stop <= r[1]:
      stop_enclosure = (r[0], r[1])
  full_range = [start, stop]
  if start_enclosure is not None:
    full_range[0] = start_enclosure[0]
  if stop_enclosure is not None:
    full_range[1] = stop_enclosure[1]

  ranges = [r for r in ranges if not is_fully_enclosed(r, full_range)]
  ranges.append(full_range)

def is_fully_enclosed(small, large):
  if small[0] >= large[0] and small[1] <= large[1]:
    return True
  else:
    return False

def get_start_time(range):
  return range[0]

for i in range(num_farmers):
  (start, stop) = get_times(fin.readline())
  add_to_range(start, stop)

ranges.sort(key=get_start_time)
last_end_time = None
max_occupied = 0
max_idle = 0
for r in ranges:
  occupied = r[1] - r[0]
  if occupied > max_occupied:
    max_occupied = occupied
  if last_end_time is not None:
    idle = r[0] - last_end_time
    if idle > max_idle:
      max_idle = idle
  last_end_time = r[1]

fout.write('{} {}\n'.format(max_occupied, max_idle))