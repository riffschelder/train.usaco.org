"""
ID: riff.sc1
LANG: PYTHON3
TASK: money
"""
fin = open('money.in')
fout = open('money.out', 'w')
all_information = [int(x) for x in fin.read().split()]

target_amount = all_information[1]
coin_types = all_information[2:]
num_coin_types = len(coin_types)

# memo[i][j] = N iff there are N ways to construct i money units using coin_types[j:]
memo = [[None] * num_coin_types for i in range(target_amount + 1)]

for current_coin_type in reversed(range(num_coin_types)):
  for amount in range(target_amount + 1):
    coin = coin_types[current_coin_type]

    if current_coin_type == num_coin_types - 1:  
      # base case: one coin type left.
      if amount % coin == 0:
        memo[amount][current_coin_type] = 1
      else:
        memo[amount][current_coin_type] = 0
    else:
      count = 0
      # we can be done taking this type of coin.
      count += memo[amount][current_coin_type + 1]
      # or we can take one more of this coin, if we can.
      if amount >= coin:
        count += memo[amount - coin][current_coin_type]
      memo[amount][current_coin_type] = count

answer = memo[target_amount][0]
fout.write(f'{answer}\n')