"""
ID: riff.sc1
LANG: PYTHON3
TASK: shopping
"""

# Insights from post-solve analysis: 
# I solved this problem with dynamic programming, but it can also be solved as a
# shortest path problem using Dijkstra's.

from math import inf

def main():
  with open('shopping.in') as fin:
    num_special_offers = int(fin.readline())
    special_offers = []
    for _ in range(num_special_offers):
      special_offers.append(fin.readline())  # We'll process them later.

    # Renumber the products from 1 <= code <= 999 to 0 <= id <= 4.
    product_ids = {}
    amounts_needed = []
    unit_prices = []
    num_products = int(fin.readline())
    for i in range(num_products):
      (code, amount, price) = [int(x) for x in fin.readline().split()]
      product_ids[code] = i
      amounts_needed.append(amount)
      unit_prices.append(price)

    # Each item in `bundles` is in the form of bundle = [0, 0, 1, 2, ...] where
    # bundle[i] is the amount of product[i] in the bundle, where
    # i in the product id from the lookup table above.
    bundles = []
    bundle_prices = []  # bundle_prices[i] is the price of bundles[i]
    for offer in special_offers:
      offer_data = [int(x) for x in offer.split()]
      bundle_prices.append(offer_data[-1])
      bundles.append(convert_to_bundle(offer_data[1:-1], product_ids, num_products))

    # Singles can be treated as a special kind of bundle.
    for i in range(num_products):
      single_bundle = [0] * num_products
      single_bundle[i] = 1
      bundles.append(single_bundle)
      bundle_prices.append(unit_prices[i])

  memo = {}
  memo[tuple([0] * num_products)] = 0  # Recursion base case.
  answer = get_best_price(amounts_needed, bundles, bundle_prices, memo)
  with open('shopping.out', 'w') as fout:
    fout.write(f'{answer}\n')

def get_best_price(amounts_needed, bundles, bundle_prices, memo):
  amounts_needed_tuple = tuple(amounts_needed)
  if amounts_needed_tuple in memo:
    return memo[amounts_needed_tuple]
  
  min_price = inf
  for bundle, bundle_price in zip(bundles, bundle_prices):
    remaining_amounts = subtract_bundle(bundle, amounts_needed)
    if all(x >= 0 for x in remaining_amounts):
      remaining_price = get_best_price(remaining_amounts, bundles, bundle_prices, memo)
      if bundle_price + remaining_price < min_price:
        min_price = bundle_price + remaining_price

  memo[amounts_needed_tuple] = min_price
  return min_price

def subtract_bundle(bundle, amounts_needed):
  """
  Caller guarantees both arrays are the same length.
  """
  return [(y - x) for (x, y) in zip(bundle, amounts_needed)]
    
def convert_to_bundle(offer_data, product_ids, num_products):
  bundle = [0] * num_products
  for i in range(0, len(offer_data), 2):
    code = offer_data[i]
    amount = offer_data[i+1]
    try:
      bundle[product_ids[code]] = amount
    except KeyError:
      # Offer contains a product we don't want to buy, and we're not allowed to
      # buy extra items, so we can't use this offer.
      # Unclear from the problem statement if this is allowed to happen.
      return [0] * num_products
  return bundle

main()