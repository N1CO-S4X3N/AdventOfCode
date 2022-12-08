readable_map = {
    'X': 'Rock',
    'A': 'Rock',
    'Y': 'Paper',
    'B': 'Paper',
    'Z': 'Scissors',
    'C': 'Scissors',
}
score_map = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}
win_list = [
    ('Rock', 'Scissors'),
    ('Paper', 'Rock'),
    ('Scissors', 'Paper')
]
score = 0
with open(r'C:\Users\nsa\Documents\AdventOfCode\2\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        opp, me = row.split(' ')
        opp = readable_map[opp.strip()]
        me = readable_map[me.strip()]
        if opp == me:
            score += 3
        elif (me, opp) in win_list:
            score += 6
        score += score_map[me]
        print("opp: ", opp)
        print("me: ", me)
print(score)

