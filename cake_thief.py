def max_duffel_bag_value(cake_tuples, capacity):
    cake_tuples = [t for t in cake_tuples if t[0] <= capacity and t[0] > 0 and t[1] > 0]
    ct_vals = []
    for ct in cake_tuples:
        ct_vals.append((ct, ct[1]/ct[0]))
    ct_vals = sorted(ct_vals, key=lambda i: i[1], reverse=True)
    value = 0
    for ct, _ in ct_vals:
        value += (capacity / ct[0]) * ct[1]
        capacity -= (capacity / ct[0]) * ct[0]
    return value


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20

assert max_duffel_bag_value(cake_tuples, capacity) == 555
 # returns 555 (6 of the middle type of cake and 1 of the last type of cake)
