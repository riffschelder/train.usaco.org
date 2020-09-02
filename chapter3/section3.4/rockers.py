"""
ID: riff.sc1
LANG: PYTHON3
TASK: rockers
"""
full_disk_capacity = 0
num_songs = 0
song_lengths = []
memo = {}

def main():
  global full_disk_capacity, num_songs, song_lengths

  with open('rockers.in') as fin:
    (num_songs, full_disk_capacity, num_disks) = [int(x) for x in fin.readline().split()]
    song_lengths = [int(x) for x in fin.readline().split()]

  answer = cram(0, num_disks, full_disk_capacity)

  with open('rockers.out', 'w') as fout:
    fout.write(f'{answer}\n')

def cram(current_song, num_disks, first_disk_capacity):
  global memo

  if current_song >= num_songs:
    return 0
  if (current_song, num_disks, first_disk_capacity) in memo:
    return memo[(current_song, num_disks, first_disk_capacity)]

  current_song_length = song_lengths[current_song]

  # Option 1: skip this song.
  answer_1 = cram(current_song + 1, num_disks, first_disk_capacity)
  
  # Option 2: put current song on the first disk (if there's enough room left).
  answer_2 = 0
  if current_song_length <= first_disk_capacity:
    answer_2 = 1 + cram(current_song + 1, num_disks, first_disk_capacity - current_song_length)

  # Option 3: put the current song on a new disk.
  answer_3 = 0
  if num_disks >= 2 and current_song_length <= full_disk_capacity:
    answer_3 = 1 + cram(current_song + 1, num_disks - 1, full_disk_capacity - current_song_length)

  answer = max(answer_1, answer_2, answer_3)
  memo[(current_song, num_disks, first_disk_capacity)] = answer
  return answer

main()