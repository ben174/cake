


def condense_meeting_times(ranges):
    ret = {}
    for rangex in ranges:
        for rangey in ranges:
            f = consolidate_times(rangex, rangey)
            print f
    print ret


def consolidate_times(time1, time2):
    if time1[0] >= time2[0] :
        time1, time2 = time2, time1
    if time1[1] < time2[0]:
        return time1, time2
    min_start = min(time1[0], time2[0])
    max_end = max(time1[1], time2[1])
    return (min_start, max_end)



print consolidate_times((1, 3), (2, 4))
print consolidate_times((0, 1), (3, 5))


ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print ranges
print condense_meeting_times(ranges) == [(0, 1), (3, 8), (9, 12)]

