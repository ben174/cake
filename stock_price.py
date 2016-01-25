def get_max_profit(prices):
    max_profit = None
    for i, price in enumerate(prices):
        for pointer in range(i+1, len(prices)):
            val = prices[pointer] - price
            if not max_profit:
                max_profit = val
            if val > max_profit:
                max_profit = val
    return max_profit


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
assert  get_max_profit(stock_prices_yesterday) == 6
# returns 6 (buying for $5 and selling for $11)
