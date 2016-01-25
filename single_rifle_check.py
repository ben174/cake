import random

def real_shuffle(left_deck, right_deck):
    total_cards = len(left_deck) + len(right_deck)
    ret = []
    for i in xrange(total_cards):
        pri_deck, alt_deck = left_deck, right_deck
        if random.choice([True, False]):
            pri_deck, alt_deck = alt_deck, pri_deck
        if pri_deck:
            ret.append(pri_deck.pop())
        else:
            ret.append(alt_deck.pop())
    return ret

def create_deck():
    suits = list('HCSD')
    vals = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split(' ')
    return [(v, s) for v in vals for s in suits]


def is_single_rifle(deck1, deck2, deck):
    for card in deck:
        if deck1 and deck1[-1] == card:
            deck1.pop()
        elif deck2 and deck2[-1] == card:
            deck2.pop()
        else:
            return False
    return True


def create_and_shuffle():
    deck = create_deck()
    shuffle_count = random.randrange(1, 4)
    single_shuffle = (shuffle_count == 1)
    deck1, deck2 = deck[0:26], deck[26:]
    original_deck1, original_deck2 = deck1[:], deck2[:]
    for i in xrange(shuffle_count):
        deck1, deck2 = deck[0:26], deck[26:]
        deck = real_shuffle(deck1, deck2)
    is_single = is_single_rifle(original_deck1, original_deck2, deck)
    print 'Shuffled {} time(s). Single Rifle? {}'.format(shuffle_count, is_single)
    return shuffle_count, is_single

for i in xrange(100):
    shuffle_count, is_single = create_and_shuffle()
    if shuffle_count == 1:
        assert is_single
    else:
        assert not is_single
