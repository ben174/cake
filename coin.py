

def dem(amount, dems):
    print amount
    print dems
    dems = set(sorted(dems))
    for dem in dems:
        print dem


assert len(dem(4, [1, 2, 3])) == 4
