# Advent of Code Day 14

import re
from adventofcode_day14_class_reindeer import *

reindeerPattern = re.compile(\
	'(.*) can fly ([0-9]*) km/s for ([0-9]*) seconds, but then must rest for ([0-9]*) seconds.')

reindeers = []

def createReindeers(input):
	for inp in input:
		matches = reindeerPattern.match(inp)
		if matches:
			current = Reindeer(matches.group(1),int(matches.group(2)),int(matches.group(3)),int(matches.group(4)))
			reindeers.append(current)
		else:
			print('Bad input:', inp)

def winnerReindeer():
	return internalWinnerReindeer(Reindeer.getDistance)

def newWinnerReindeer():
	return internalWinnerReindeer(Reindeer.getPoints)

def internalWinnerReindeer(func, multiple = False):
	maximum = 0
	multipleWinners = []
	for r in reindeers:
		maximum = max(maximum,r.get(func))
	
	for r in reindeers:
		if r.get(func) == maximum:
			if not multiple:
				return r
			else:
				multipleWinners.append(r)
	
	return multipleWinners

def addPoints():
	for r in internalWinnerReindeer(Reindeer.getDistance,True):
		r.addOnePoint()
	
# with open('adventofcode_day14_test_input.txt') as f:
with open('adventofcode_day14_input.txt') as f:
	input = [line.strip() for line in f]

# racetime = 1000
racetime = 2503

createReindeers(input)

print(reindeers)
for i in range(racetime):
	for r in reindeers:
		r.tick()

print(reindeers)
print('Part 1 the winner is:', winnerReindeer(),'\n')

for r in reindeers:
	r.restart()

print(reindeers)
for i in range(racetime):
	for r in reindeers:
		r.tick()
	addPoints()

print(reindeers)
print('Part 2 the winner is:',newWinnerReindeer())
