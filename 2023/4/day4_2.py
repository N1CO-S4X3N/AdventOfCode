import os
import sys


class ScratchCard():
    def __init__(self, card_id, winning_numbers, scratched_numbers, occurrance):
        self.card_id = card_id
        self.winning_numbers = winning_numbers
        self.scratched_numbers = scratched_numbers
        self.occurrance = occurrance
    
    def add_cards(self):
        for i in range(1, self.occurrance + 1):
            if i < max:
                new_cards.append(all_cards[self.card_id + i - 1])


total = 0
max = 0
all_cards = []
new_cards = []
with open(os.path.join(sys.path[0], 'real_data.txt'), 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        max = i + 1
        numbers = line.strip().split(': ')[1]
        numbers = numbers.split(' | ')
        winning =  [int(n) for n in numbers[0].split(' ') if n.isdigit()]
        own = [int(n) for n in numbers[1].split(' ') if n.isdigit()]
        occurrance = sum(element in own for element in winning)
        all_cards.append(ScratchCard(i + 1, winning, own, occurrance))

for card in all_cards:
    card.add_cards()

for new_card in new_cards:
    new_card.add_cards()

print("Total: ", len(new_cards) + len(all_cards))
