"""
ID: riff.sc1
LANG: PYTHON3
TASK: transform
"""

fin = open('transform.in')
fout = open('transform.out', 'w')

size = int(fin.readline()[:-1])

first_image = []
for i in range(size):
  first_image.append(fin.readline()[:-1])

second_image = []
for i in range(size):
  second_image.append(fin.readline()[:-1])

def rotate(image):
  new_image = []
  for i in range(size):
    row = ''
    for j in range(size):
      row += image[size-j-1][i]
    new_image.append(row)
  return new_image

def reflect(image):
  new_image = []
  for i in range(size):
    row = image[i][::-1]
    new_image.append(row)
  return new_image

def is_same(image_one, image_two):
  for i in range(size):
    for j in range(size):
      if image_one[i][j] != image_two[i][j]:
        return False
  return True

def get_answer(old_image, new_image):
  rotated_once = rotate(old_image)
  if is_same(rotated_once, new_image):
    return 1
  rotated_twice = rotate(rotated_once)
  if is_same(rotated_twice, new_image):
    return 2
  rotated_thrice = rotate(rotated_twice)
  if is_same(rotated_thrice, new_image):
    return 3
  reflection = reflect(old_image)
  if is_same(reflection, new_image):
    return 4
  rotated_once = rotate(reflection)
  if is_same(rotated_once, new_image):
    return 5
  rotated_twice = rotate(rotated_once)
  if is_same(rotated_twice, new_image):
    return 5
  rotated_thrice = rotate(rotated_twice)
  if is_same(rotated_thrice, new_image):
    return 5
  if is_same(old_image, new_image):
    return 6
  return 7

fout.write('{}\n'.format(get_answer(first_image, second_image)))
