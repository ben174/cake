import random
import timeit


def builtin_merge(list1, list2):
    return sorted(list1 + list2)

def reverse_merge(list1, list2):
    ret = []
    pri_list = list1 if list1[-1] > list2[-1] else list2
    alt_list = list1 if pri_list is list2 else list2
    while True:
        if (not pri_list) or (not alt_list):
            ret.extend(pri_list[::-1] + alt_list[::-1])
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

assert reverse_merge(my_list, alices_list) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
my_list     = [1, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
assert reverse_merge(my_list, alices_list) == [1, 1, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

def merge_lists(my_list, alices_list):
    """ This was not written by me. But my solution seems to beat it. """
    # set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:

        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)

        # case: next comes from my list
        # my list must not be exhausted, and EITHER:
        # 1) alice's list IS exhausted, or
        # 2) the current element in my list is less
        #    than the current element in alice's list
        if not is_my_list_exhausted and (is_alices_list_exhausted or \
            my_list[current_index_mine] < alices_list[current_index_alices]):

            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1

        # case: next comes from alice's list
        else:
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list




list1 = sorted([random.randrange(0, 1000) for x in xrange(10000000)])
list2 = sorted([random.randrange(0, 1000) for x in xrange(10000000)])
base1 = list1[:]
base2 = list2[:]

start_time = timeit.default_timer()
baseline = builtin_merge(list1, list2)
print('Builtin: {}'.format(timeit.default_timer() - start_time))


list1 = base1[:]
list2 = base2[:]

start_time = timeit.default_timer()
ret = reverse_merge(list1, list2)
print('Reverse merge: {}'.format(timeit.default_timer() - start_time))
assert ret == baseline

list1 = base1[:]
list2 = base2[:]


start_time = timeit.default_timer()
ret = merge_lists(list1, list2)
print('Cake merge: {}'.format(timeit.default_timer() - start_time))
assert ret == baseline


