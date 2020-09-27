"""
ID: riff.sc1
LANG: PYTHON3
TASK: job
"""

# This works, but it'll be hard to explain without a whiteboard.
# Lots of inefficiencies here too, but the inputs are small enough.

def main():
  with open('job.in') as fin:
    num_jobs, num_machines_a, num_machines_b = [int(x) for x in fin.readline().split()]
    processing_times = [int(x) for x in fin.read().split()]

  processing_times_a = processing_times[:num_machines_a]
  processing_times_b = processing_times[num_machines_a:]

  num_a_jobs_done_by_time = get_num_jobs_done_by_time(processing_times_a, num_jobs)
  num_b_jobs_done_by_time = get_num_jobs_done_by_time(processing_times_b, num_jobs)
  dependency = [num_jobs - x for x in num_b_jobs_done_by_time][::-1][1:]

  earliest_overlap = len(num_a_jobs_done_by_time)
  for i in range(len(num_a_jobs_done_by_time)):
    if overlap_ok(num_a_jobs_done_by_time, dependency, i):
      earliest_overlap = i
      break

  time_all_a_jobs_done = len(num_a_jobs_done_by_time) - 1
  time_all_b_jobs_done = earliest_overlap + len(dependency)

  with open('job.out', 'w') as fout:
    fout.write(f'{time_all_a_jobs_done} {time_all_b_jobs_done}\n')
  
def get_num_jobs_done_by_time(processing_times, num_jobs):
  num_jobs_done_by_time = [0]
  time = 1
  while True:
    num_jobs_done = 0
    for duration in processing_times:
      num_jobs_done += time // duration
    if num_jobs_done > num_jobs:
      num_jobs_done = num_jobs
    num_jobs_done_by_time.append(num_jobs_done)
    if num_jobs_done >= num_jobs:
      break
    time += 1
  return num_jobs_done_by_time

def overlap_ok(num_a_jobs_done_by_time, dependency, start_time):
  for i in range(len(dependency)):
    time = start_time + i
    if time < len(num_a_jobs_done_by_time):
      if num_a_jobs_done_by_time[time] < dependency[i]:
        return False
    else:
      break
  return True

main()