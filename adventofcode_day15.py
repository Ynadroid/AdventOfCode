# Advent of Code Day 15

import re
import itertools

ingredientPattern = re.compile(\
	'(.*): capacity (-?[0-9]*), durability (-?[0-9]*), flavor (-?[0-9]*), texture (-?[0-9]*), calories (-?[0-9]*)')

ingredientsprops = {'capacity':{},'durability':{},'flavor':{},'texture':{},'calories':{}}
proportions = {}
ingredientslist = []

def calculateScore(caloriessystem = False):
	total = 1
	totalcal = 1
	scoredict = {}
	for k,v in ingredientsprops.items():
		scoredict[k] = 0
		for name,prop in proportions.items():
			scoredict[k] += prop * v[name]
		if scoredict[k] < 0:
			scoredict[k] = 0
	
	#print(scoredict)
	
	for k,v in scoredict.items():
		if k != 'calories':
			total *= v
		elif caloriessystem:
			totalcal *= v
	
	#print(proportions,total)
	if totalcal == 500:
		print('Cal:', proportions, scoredict, total, totalcal)
	elif caloriessystem:
		total = 0
	return total

def checkProportions():
	total = 0
	for p,v in proportions.items():
		total += v
	
	return total == 100
	
def registerIngredients(input):
	for inp in input:
		matches = ingredientPattern.match(inp)
		if matches:
			ingname = matches.group(1)
			ingredientsprops['capacity'][ingname] = int(matches.group(2))
			ingredientsprops['durability'][ingname] = int(matches.group(3))
			ingredientsprops['flavor'][ingname] = int(matches.group(4))
			ingredientsprops['texture'][ingname] = int(matches.group(5))
			ingredientsprops['calories'][ingname] = int(matches.group(6))
			
			proportions[ingname] = 0
			ingredientslist.append(ingname)
		else:
			print('Bad input:', inp)

# with open('adventofcode_day15_test_input.txt') as f:
with open('adventofcode_day15_input.txt') as f:
	input = [line.strip() for line in f]

registerIngredients(input)
print(ingredientsprops,'\n')

recipes = itertools.combinations_with_replacement(ingredientslist,100)

maxscore = 0
maxscorep2 = 0
for r in recipes:
	for ing in r:
		proportions[ing] += 1
	if not checkProportions():
		print('invalid proportions')
		break
	maxscore = max(maxscore,calculateScore())
	maxscorep2 = max(maxscorep2,calculateScore(True))
	for ing in r:
		proportions[ing] = 0

print('High score:',maxscore)
print('High score for calories system:',maxscorep2)
