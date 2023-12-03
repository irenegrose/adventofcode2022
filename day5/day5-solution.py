import re
import copy

# convert each line of input in diagram into a list
def parse_input(s):
    stack = []
    p = 0
    n = 3
    while n < len(s):
        stack.append(s[p:n])
        p += 4
        n += 4
    return stack

f = open('day5-input.txt')
lines = f.readlines()
f.close()

# build an array of arrays representing the 2d grid diagram
grid = []
for line in lines:
    if line.startswith(' 1 '):
        break
    grid.append(parse_input(line))

# transform the grid into a set of stacks that represent each vertical pile
stacks = [[] for entry in grid[0]]
for line in grid:
    for j,cell in enumerate(line):
        stacks[j].insert(0, cell)
        
# discard the top stack entries representing blank input
for s in stacks:
    while s[-1].strip() == '':
        s.pop()

stacks2 = copy.deepcopy(stacks)

g = open('day5-output.txt', 'w')

# follow the instructions to rearrange the stacks
for step in [line for line in lines if line.startswith('move')]:
    matches = re.match(re.compile('^move (\d+) from (\d+) to (\d+)$'), step)
    num_to_move = int(matches.group(1))
    src = int(matches.group(2)) - 1
    dest = int(matches.group(3)) - 1
    # Part 1
    c = 0
    while c < num_to_move:
        cell = stacks[src].pop()
        stacks[dest].append(cell)
        c += 1
    
    # Part 2
    g.write(step)
    for i,s in enumerate(stacks2):
        g.write('%d: %s\n' % (i+1,''.join(s)))
    g.write('====')
    stacks2[dest].extend(stacks2[src][-1*num_to_move:])
    c2 = 0
    while c2 < num_to_move:
        stacks2[src].pop()
        c2 += 1
    for i,s in enumerate(stacks2):
        g.write('%d: %s\n' % (i+1,''.join(s)))
        g.flush()
    g.flush()


result = []
for s in stacks:
    result.append(s[-1].replace('[', '').replace(']',''))

result2 = []
for s in stacks2:
    result2.append(s[-1].replace('[', '').replace(']', ''))

print('Part 1: %s' % ''.join(result))
print('Part 2: %s' % ''.join(result2))
g.close()
