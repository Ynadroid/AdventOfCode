# Advent of Code Day 18

def constructGrid(input):
	x = 0
	y = 0
	for line in input:
		lightsgrid.append([])
		for light in line:
			if light == '#':
				lightsgrid[x].append(1)
			elif light == '.':
				lightsgrid[x].append(0)
			else:
				print('Wrong input')
			y += 1
		x += 1
		y = 0

def gridToString():
	tostring = ''
	for line in lightsgrid:
		for light in line:
			if light > 0:
				tostring += '#'
			else:
				tostring += '.'

		tostring += '\n'
	return tostring
	
def anyGridToString(anygrid):
	tostring = ''
	for line in anygrid:
		for light in line:
			if light > 0:
				tostring += '#'
			else:
				tostring += '.'

		tostring += '\n'
	return tostring

def countOnNeighbors(x,y):
	count = 0
	for cy in range(y-1,y+2):
		if cy >= 0 and cy < len(lightsgrid[x]):
			for cx in range(x-1,x+2):
				if cx >= 0 and cx < len(lightsgrid):
					if not (cx == x and cy == y):
						count += lightsgrid[cx][cy]
	return count

def defineNewState(x,y):
	if lightsgrid[x][y] == 1:
		# light is on
		onNeighbors = countOnNeighbors(x,y)
		if onNeighbors == 2 or onNeighbors == 3:
			return 1
		else:
			return 0
	elif lightsgrid[x][y] == 0:
		# light is off
		if 3 == countOnNeighbors(x,y):
			return 1
		else:
			return 0
	
def doOneStep():
	newlightsgrid = []
	for x in range(0,len(lightsgrid)):
		newlightsgrid.append([])
		for y in range(0,len(lightsgrid[x])):
			newlightsgrid[x].append(defineNewState(x,y))
	return newlightsgrid

def countOnLights():
	count = 0
	for x in range(0,len(lightsgrid)):
		for y in range(0,len(lightsgrid[x])):
			count += lightsgrid[x][y]
	
	return count
	
lightsgrid = []

with open('aoc_day18_input.txt') as f:
# with open('aoc_day18_test_input.txt') as f:
	input = [line.strip() for line in f]
	
constructGrid(input)
print(gridToString())

for step in range(0,100):
	lightsgrid = doOneStep()
	# print(gridToString())

print('There are',countOnLights(),'lights on')