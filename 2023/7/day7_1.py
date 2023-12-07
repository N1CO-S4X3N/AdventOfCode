import os
import sys


class Hand():
    def __init__(self, bet, cards, nbr_of_each):
        self.bet = bet
        self.cards = cards
        self.nbr_of_each = nbr_of_each


card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
highest_cards = []
one_pairs = []
two_pairs = []
three_of_a_kinds = []
full_houses = []
four_of_a_kinds = []
five_of_a_kinds = []
hands = []
nbr_of_each = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        newline = line.split()
        for value in card_values:
            for card in newline[0]:
                if card == value:
                    nbr_of_each[card] += 1
        hands.append(Hand(int(newline[1]), [c for c in newline[0]], nbr_of_each))
        nbr_of_each = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
        
for hand in hands:
    count = [n for n in hand.nbr_of_each.values() if n != 0]
    count.sort(reverse=True)
    if count[0] == 5:
        five_of_a_kinds.append(hand)
    elif count[0] == 4:
        four_of_a_kinds.append(hand)
    elif count[0] == 3:
        if count[1] == 2:
            full_houses.append(hand)
        else:
            three_of_a_kinds.append(hand)
    elif count[0] == 2:
        if count[1] == 2:
            two_pairs.append(hand)
        else:
            one_pairs.append(hand)
    else:
        highest_cards.append(hand)


five_of_a_kinds.sort(key=lambda t: [card_values.index(c) for c in t.cards])
four_of_a_kinds.sort(key=lambda t: [card_values.index(c) for c in t.cards])
full_houses.sort(key=lambda t: [card_values.index(c) for c in t.cards])
three_of_a_kinds.sort(key=lambda t: [card_values.index(c) for c in t.cards])
two_pairs.sort(key=lambda t: [card_values.index(c) for c in t.cards])
one_pairs.sort(key=lambda t: [card_values.index(c) for c in t.cards])
highest_cards.sort(key=lambda t: [card_values.index(c) for c in t.cards])

price = 0
rank = 1
for t in highest_cards:
    price += t.bet * rank
    rank += 1
for t in one_pairs:
    price += t.bet * rank
    rank += 1
for t in two_pairs:
    price += t.bet * rank
    rank += 1
for t in three_of_a_kinds:
    price += t.bet * rank
    rank += 1
for t in full_houses:
    price += t.bet * rank
    rank += 1
for t in four_of_a_kinds:
    price += t.bet * rank
    rank += 1
for t in five_of_a_kinds:
    price += t.bet * rank
    rank += 1

print("Final rank: ", rank)
print("Total Price: ", price)