f = open('day1-sample.txt')

lines = f.readlines()
sums = [0]
max_val = 0
max_index = 0
for line in lines:
	if len(line.strip()) == 0:
		if sums[len(sums)-1] > max_val:
			max_val = sums[len(sums)-1]
			max_index = len(sums)-1
		sums.append(0)
	else:
		sums[len(sums)-1] = sums[len(sums)-1] + int(line)


sums = sorted(sums, reverse=True)
first = sums[0]
second = sums[1]
third = sums[2]
total = first + second + third

print('Part 1: %d (carried by elf %d)' % (max_val, max_index))
print('Part 2: %d + %d + %d = %d' % (first, second, third, total))

f.close()