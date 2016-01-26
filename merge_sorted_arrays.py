
def merge_lists(list1, list2):
    ret = []
    pri_list = list1 if list1[-1] > list2[-1] else list2
    alt_list = list1 if pri_list is list2 else list2
    while True:
        if not pri_list:
            ret.extend(alt_list)
            break
        if not alt_list:
            ret.extend(pri_list)
            break
        if pri_list[-1] > alt_list[-1]:
            item = pri_list.pop()
        else:
            item = alt_list.pop()
        ret.append(item)
    ret = ret[::-1]
    return ret




my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

assert merge_lists(my_list, alices_list) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
my_list     = [1, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
assert merge_lists(my_list, alices_list) == [1, 1, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
