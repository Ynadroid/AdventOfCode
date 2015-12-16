# Advent of Code Day 13

import itertools
import re

def constructHappinessTable(input):
	inputPattern = re.compile('(.*) would (gain|lose) ([0-9]*) happiness units by sitting next to (.*)\.')
	for inp in input:
		matches = inputPattern.match(inp)
		if matches:
			#print(matches.groups())
			# grp1 = Name
			# grp2 = + or -
			# grp3 = value
			# grp4 = Name
			guest1 = matches.group(1)
			guest2 = matches.group(4)
			
			happiness = int(matches.group(3))
			sign = matches.group(2)
			
			if 'lose' in sign:
				happiness = -happiness
			
			if guest1 not in guestslist:
				guestslist.add(guest1)
			if guest1 not in happinesstable:
				happinesstable[guest1] = {}
			
			happinesstable[guest1][guest2] = happiness
		else:
			print('Bad input:',inp)

def countHappinessOfArrangement(guests):
	totalhappiness = 0
	pos = 0
	while pos < len(guests):
		if pos != len(guests)-1:
			totalhappiness += (happinesstable[guests[pos]][guests[pos+1]] + happinesstable[guests[pos+1]][guests[pos]])
		pos += 1
	totalhappiness += (happinesstable[guests[0]][guests[len(guests)-1]] + happinesstable[guests[len(guests)-1]][guests[0]])
	
	#print(guests, totalhappiness)
	return totalhappiness

guestslist = set()
happinesstable = {}

with open('adventofcode_day13_input.txt') as f:
	input = [line.strip() for line in f]

constructHappinessTable(input)

happinesstable['ME'] = {}
for g in guestslist:
	happinesstable['ME'][g] = 0
	happinesstable[g]['ME'] = 0

guestslist.add('ME')

print(guestslist)
#print(happinesstable)

combinaisons = itertools.permutations(guestslist)

highesthappiness = 0
for c in combinaisons:
	highesthappiness = max(highesthappiness,countHappinessOfArrangement(c))

print('Highest happiness is:',highesthappiness)
