from random import sample


def cards_sample(suits, ranks):
    deck = [str(x)+'-'+y for x in ranks for y in suits]
    return sample(deck, 4)


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [i for i in range(1, 11)] + ['Jack', 'Queen', 'King']

print(cards_sample(suits, ranks))
