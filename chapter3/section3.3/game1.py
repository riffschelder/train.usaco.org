"""
ID: riff.sc1
LANG: PYTHON3
TASK: game1
"""
def main():
  with open('game1.in') as fin:
    num_numbers = int(fin.readline())
    numbers = [int(x) for x in fin.read().split()]

  # best_score[i][j] is the best score for each player if player p (0 or 1)
  # plays first and the board starts with numbers[i:j+1] (i.e. i..j inclusive).
  # Only meaningful if i <= j.
  best_score = [[[-1, -1] for _ in range(num_numbers)] for _ in range(num_numbers)]
  play(best_score, numbers, 0, num_numbers-1, 0)

  with open('game1.out', 'w') as fout:
    (player_score, opponent_score) = best_score[0][num_numbers-1]
    fout.write(f'{player_score} {opponent_score}\n')

def play(best_score, numbers, left, right, player):
  if best_score[left][right][player] > -1:
    return

  opponent = 1 - player

  if left == right:
    best_score[left][right][player] = numbers[left]
    best_score[left][right][opponent] = 0
  else:
    # Take left.
    player_score_left = numbers[left]
    play(best_score, numbers, left + 1, right, opponent)
    player_score_left += best_score[left+1][right][player]
    opponent_score_left = best_score[left+1][right][opponent]

    # Take right.
    player_score_right = numbers[right]
    play(best_score, numbers, left, right - 1, opponent)
    player_score_right += best_score[left][right-1][player]
    opponent_score_right = best_score[left][right-1][opponent]

    if player_score_left > player_score_right:
      best_score[left][right][player] = player_score_left
      best_score[left][right][opponent] = opponent_score_left
    else:
      best_score[left][right][player] = player_score_right
      best_score[left][right][opponent] = opponent_score_right
    # print(f'best_score[{left}][{right}] = {best_score[left][right]}')

main()