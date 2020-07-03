"""
ID: riff.sc1
LANG: PYTHON3
TASK: friday
"""
#                 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

fin = open('friday.in')
fout = open('friday.out', 'w')

num_years = int(fin.readline()[:-1])

def is_leap_year(year):
  year += 1900
  if year % 4 != 0:
    return False
  if year % 400 == 0:
    return True
  if year % 100 == 0:
    return False
  return True

# Jan 13, 1900 is a Saturday. Sunday = 0, Monday = 1, ...
this_thirteenth = 6
d = [0, 0, 0, 0, 0, 0, 0]  # d for distribution
for i in range(num_years):
  for j in range(12):
    d[this_thirteenth] += 1
    this_thirteenth += days_in_months[j]
    if j == 1 and is_leap_year(i):  # february is days_in_month[1]
      this_thirteenth += 1
    this_thirteenth = this_thirteenth % 7

fout.write('{} {} {} {} {} {} {}\n'.format(d[6], d[0], d[1], d[2], d[3], d[4], d[5]))

