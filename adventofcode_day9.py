# Advent Of Code Day 9

import re
import itertools

def calculateDistance(list):
	distance = 0
	origin = ''
	for dest in list:
		if origin != '':
			distance += paths[origin][dest]
		origin = dest
	return (distance,list)

def minInList(list_of_tuples):
	tmin = list_of_tuples[0]
	min = list_of_tuples[0][0]
	for d,l in list_of_tuples:
		if min > d:
			min = d
			tmin = (d,l)
	
	return tmin
	
def maxInList(list_of_tuples):
	tmax = list_of_tuples[0]
	max = list_of_tuples[0][0]
	for d,l in list_of_tuples:
		if max < d:
			max = d
			tmax = (d,l)
	
	return tmax
	
with open('adventofcode_day9_input.txt') as f:
# with open('adventofcode_day9_test_input.txt') as f:
	input = [line.strip() for line in f]

paths = {}
destinations = set()
# Initialize the paths
pathPattern = re.compile('(.*) to (.*) = ([0-9]{1,})')

for path in input:
	matches = pathPattern.match(path)
	if matches:
		# print(matches.group(1),'to',matches.group(2),'=',matches.group(3))
		origin = matches.group(1)
		dest = matches.group(2)
		if origin not in paths:
			paths[origin] = {}
			destinations.add(origin)
		if dest not in paths:
			paths[dest] = {}
			destinations.add(dest)
		paths[origin][dest] = int(matches.group(3))
		paths[dest][origin] = int(matches.group(3))
	else:
		print(path,'does not match')

possible_paths = itertools.permutations(destinations)

result = map(calculateDistance,possible_paths)
result_list = list(result)
print('The shortest distance is:',minInList(result_list))
print('The longest distance is:',maxInList(result_list))
