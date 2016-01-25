



def flight(flight_length, movie_lengths):
    if len(movie_lengths) < 2:
        return False
    elif len(movie_lengths) == 2:
        return sum(movie_lengths) == flight_length
    for index, length_a in enumerate(movie_lengths):
        for length_b in movie_lengths[index+1:]:
            if length_a + length_b == flight_length:
                return True
    return False



assert flight(90, [10, 20, 40, 50])
assert flight(30, [10, 20, 40, 50])
assert flight(20, [10, 10])
assert flight(90, [50, 20, 40])

assert not flight(90, [10, 20, 30, 50])
assert not flight(20, [10, 20, 40, 50])
