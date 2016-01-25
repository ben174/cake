

def dem(amount, dems):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    if not dems:
        return 0
    current_coin, rest_of_coins = dems[0], dems[1:]


    num_possibilities = 0
    while amount >= 0:
        num_possibilities += dem(amount, rest_of_coins)
        amount -= current_coin
    return num_possibilities





assert dem(4, [1, 2, 3]) == 4
