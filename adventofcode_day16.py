# Advent of Code Day 16

import re

def rule1Check(aunt):
	for comp,val in tickertape.items():
		if comp in aunt:
			if aunt[comp] != val:
				print('Aunt',num,'does not match')
				return False
	return True
	
def rule2Check(aunt):
	for comp,val in tickertape.items():
		if comp in aunt:
			if comp == 'cats' or comp == 'trees':
				if aunt[comp] <= val:
					print('Aunt',num,'does not match')
					return False
			elif comp == 'goldfish' or comp == 'pomeranians':
				if aunt[comp] >= val:
					print('Aunt',num,'does not match')
					return False
			else:
				if aunt[comp] != val:
					print('Aunt',num,'does not match')
					return False
	return True

inputPattern = re.compile('Sue ([0-9]*): (.*): ([0-9]*), (.*): ([0-9]*), (.*): ([0-9]*)')
def analyzeInputData(input):
	for inp in input:
		matches = inputPattern.match(inp)
		if matches:
			auntNumber = int(matches.group(1))
			if auntNumber not in auntSueData:
				auntSueData[auntNumber] = {}
			auntSueData[auntNumber][matches.group(2)] = int(matches.group(3))
			auntSueData[auntNumber][matches.group(4)] = int(matches.group(5))
			auntSueData[auntNumber][matches.group(6)] = int(matches.group(7))
		else:
			print('Bad input:',inp)

compounds = ['children','cats','samoyeds','pomeranians','akitas','vizslas','goldfish','trees',\
	'cars','perfumes']

tickertape = {'children': 3,'cats': 7,'samoyeds': 2,'pomeranians': 3,'akitas': 0,'vizslas': 0,'goldfish': 5,'trees': 3,'cars': 2,'perfumes': 1}

auntSueData = {}

with open('adventofcode_day16_input.txt') as f:
	input = [line.strip() for line in f]

analyzeInputData(input)
print(auntSueData)

matchingAuntSueR1 = set()
matchingAuntSueR2 = set()

for num,aunt in auntSueData.items():
	if rule1Check(aunt):
		matchingAuntSueR1.add(num)
	if rule2Check(aunt):
		matchingAuntSueR2.add(num)

print('Matching aunts:', matchingAuntSueR1, matchingAuntSueR2)
