"""
ID: riff.sc1
LANG: PYTHON3
TASK: heritage
"""
def main():
  with open('heritage.in') as fin:
    in_order = fin.readline().strip()
    pre_order = fin.readline().strip()

  post_order = get_post_order(in_order, pre_order)
  with open('heritage.out', 'w') as fout:
    fout.write(f'{post_order}\n')

def get_post_order(in_order, pre_order):
  root = pre_order[0]
  root_index = in_order.find(root)  # root's index in in_order

  in_order_left = in_order[:root_index]
  in_order_right = in_order[root_index+1:]

  pre_order_left = pre_order[1:root_index+1]
  pre_order_right = pre_order[root_index+1:]

  # Only recurse if there's a tree to recurse on.
  post_order_left = ''
  if in_order_left:
    post_order_left = get_post_order(in_order_left, pre_order_left)
  post_order_right = ''
  if in_order_right:
    post_order_right = get_post_order(in_order_right, pre_order_right)
  return post_order_left + post_order_right + root

main()