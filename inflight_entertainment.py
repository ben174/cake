import timeit
def flight(flight_length, movie_lengths):
    if len(movie_lengths) < 2:
        return False
    elif len(movie_lengths) == 2:
        return sum(movie_lengths) == flight_length
    for index, length_a in enumerate(movie_lengths):
        remaining = (flight_length - length_a)
        if remaining in movie_lengths[index+1:]:
            return True
    return False

def old_flight(flight_length, movie_lengths):
    if len(movie_lengths) < 2:
        return False
    elif len(movie_lengths) == 2:
        return sum(movie_lengths) == flight_length
    for index, length_a in enumerate(movie_lengths):
        for length_b in movie_lengths[index+1:]:
            if length_a + length_b == flight_length:
                return True
    return False

def set_optimized(flight_length, movie_lengths):
    movie_lengths = set(movie_lengths)
    if len(movie_lengths) < 2:
        return False
    elif len(movie_lengths) == 2:
        return sum(movie_lengths) == flight_length
    for index, length_a in enumerate(movie_lengths):
        remaining = (flight_length - length_a)
        if remaining in movie_lengths:
            return True
    return False



import random
def runtest(funk):
    tries = 100
    successes = 0
    for i in xrange(tries):
        flight_length = random.randrange(90, 10000)
        movie_lengths = [random.randrange(90, 10000) for x in xrange(10000)]
        if funk(flight_length, movie_lengths):
            successes += 1
    print 'Tries:', tries, 'Successes:', successes


start_time = timeit.default_timer()
runtest(flight)
print('New way: {}'.format(timeit.default_timer() - start_time))
# start_time = timeit.default_timer()
# runtest(old_flight)
# print('Old way: {}'.format(timeit.default_timer() - start_time))
start_time = timeit.default_timer()
runtest(set_optimized)
print('Set optimized: {}'.format(timeit.default_timer() - start_time))


# assert flight(90, [10, 20, 40, 50])
# assert flight(30, [10, 20, 40, 50])
# assert flight(20, [10, 10])
# assert flight(90, [50, 20, 40])
# 
# assert not flight(90, [10, 20, 30, 50])
# assert not flight(20, [10, 20, 40, 50])
