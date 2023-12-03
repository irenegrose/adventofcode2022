# map ASCII letter value onto index (1-26 for lowercase, 27 - 52 for uppercase)
def get_priority(letter):
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 26 + 1

# find an overlapping character between 2 strings
def find_item(s1, s2):
    overlap = set(list(s1)) & set(list(s2))
    return list(overlap)[0]

# find an overlapping character between 3 strings
def find_item2(s1, s2, s3):
    overlap = set(list(s1)) & set(list(s2)) & set(list(s3))
    return list(overlap)[0]


f = open('day3-input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

g = open('day3-output.txt', 'w')

result = 0
result2 = 0

for idx, line in enumerate(lines):
    # Part 1
    half = int(len(line) / 2)
    cmp1 = line[0:half]
    cmp2 = line[half:]
    item = find_item(cmp1, cmp2)
    score = get_priority(item)
    result += score
    g.write('%s | %s\n\t--> %s [%d]\n' % (cmp1, cmp2, item, score))

    # Part 2
    if idx % 3 == 0:
        g1 = lines[idx]
        g2 = lines[idx+1]
        g3 = lines[idx+2]
        badge = find_item2(g1, g2, g3)
        score = get_priority(badge)
        result2 += score
        g.write('\t--> %s [%d]\n' % (badge, score))

print('Part 1: %d' % result)
print('Part 2: %d' % result2)
g.close()
