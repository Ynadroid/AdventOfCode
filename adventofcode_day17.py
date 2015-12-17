# Advent of Code Day 17

import itertools

def hasSufficientSize(liters,iterable):
	if sum(iterable) == liters:
		return 1
	else:
		return 0

def curry_HasSufficientSize(liters):
	return lambda it: hasSufficientSize(liters,it)

with open('adventofcode_day17_input.txt') as f:
# with open('adventofcode_day17_test_input.txt') as f:
	input = [int(line.strip()) for line in f]

eggnog = 150
# eggnog = 25

print('Part 1')

numberofcomb = sum(sum(map(curry_HasSufficientSize(eggnog),c)) for c in \
	(itertools.combinations(input,r) for r in range(1,len(input)+1)))
print('You have',numberofcomb,'combinations to store',eggnog,'liters of eggnog')

print('Part 2')

for r in range(1,len(input)+1):
	numberofcomb = sum(map(curry_HasSufficientSize(eggnog),itertools.combinations(input,r)))
	if numberofcomb > 0:
		print(r,'containers are sufficient to store',eggnog,'liters and there are',numberofcomb,'ways to do it')
		break
