readable_map = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
}
score_map = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}
win_map = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}
score = 0
with open(r'C:\Users\nsa\Documents\AdventOfCode\2\items2.txt', 'r', encoding='utf-8') as file:
    item = ''
    for row in file:
        print('row: ', repr(row))
        opp, me = row.split(' ')
        me = me.strip()
        opp = readable_map[opp]
        print('opp: ', opp)
        print('me: ', repr(me))
        if me == 'X':
            item = win_map[opp]
        elif me == 'Y':
            score += 3
            item = opp
        elif me == 'Z':
            score += 6
            item = [k for k, v in win_map.items() if v == opp][0]
        score += score_map[item]
print(score)

