MOVES = {
    'A': 0, # rock
    'X': 0, # rock
    'B': 1, # paper
    'Y': 1, # paper
    'C': 2, # scissors
    'Z': 2  # scissors
}
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

def get_outcome1(a, b):
    if MOVES[a] == MOVES[b]:
        return 3 # draw 
    elif MOVES[b] == (MOVES[a] + 1) % 3:
        return 6 # win
    else:
        return 0 # loss

def get_bscore(a, outcome):
    if outcome == DRAW:
        return MOVES[a] # copy opponent's move for a draw
    elif outcome == WIN:
        return (MOVES[a] + 1) % 3
    else:
        return (MOVES[a] + 2) % 3

def get_outcome2(outcome):
    if outcome == DRAW:
        return 3
    elif outcome == WIN:
        return 6
    else:
        return 0

f = open('day2-input.txt', 'r')
g = open('day2-output.txt', 'w')
lines = f.readlines()
f.close()

part_1_score = 0
part_2_score = 0

for line in lines:
    cur = line.strip().split(' ')
    a, b = cur[0], cur[1]   
    part_1_score += get_outcome1(a, b) + (MOVES[b] + 1)
    part_2_score += get_outcome2(b) + (get_bscore(a, b) + 1)
    debug = str(cur).replace('A', 'Rock').replace('X', 'Rock') \
                    .replace('B', 'Paper').replace('Y', 'Paper') \
                    .replace('C', 'Scissors').replace('Z', 'Scissors')
    g.write('%s\n\t--> %d, %d\n' % (debug, get_outcome1(a,b), MOVES[b]))
    g.write('\t--> %d, %d\n' % (get_outcome2(b), get_bscore(a,b) + 1))

print('Part 1: %d' % part_1_score)
print('Part 2: %d' % part_2_score)

g.close()


