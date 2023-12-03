def get_section(section_bounds):
    min_bound = int(section_bounds[0])
    max_bound = int(section_bounds[1]) + 1
    return set(range(min_bound, max_bound))


f = open('day4-input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

g = open('day4-output.txt', 'w')

count = 0
count2 = 0
for line in lines:
    section1 = line.split(',')[0].split('-')
    section2 = line.split(',')[1].split('-')
    set1 = get_section(section1)
    set2 = get_section(section2)
    overlap = len(set1 & set2)
    if overlap == len(set1) or overlap == len(set2):
        count += 1
        g.write('%s\n' % line)

    if overlap > 0:
        count2 += 1
        
print('Part 1: %d' % count)
print('Part 2: %d' % count2)
g.close()
