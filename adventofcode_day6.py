# Advent of Code Day 6

import re

def turnOn(x,y):
	if not lightgrid[x][y]:
		toggleLight(x,y)
	
def turnOff(x,y):
	if lightgrid[x][y]:
		toggleLight(x,y)

def toggleLight(x,y):
	global turnoffcount
	global turnoncount
	if lightgrid[x][y]:
		#print(x,',',y,'turned off')
		turnoffcount += 1
	else:
		#print(x,',',y,'turned on')
		turnoncount += 1
	
	lightgrid[x][y] = not lightgrid[x][y]

def applyCommand(cmd, bx, by, ex, ey):
	for x in range(bx,ex+1):
		for y in range(by,ey+1):
			cmd(x,y)

def commandInterpreter(commandtext):
	commandPattern = re.compile('((turn (on|off))|(toggle)) ([0-9]{1,3}),([0-9]{1,3}) through ([0-9]{1,3}),([0-9]{1,3})')
	matches = commandPattern.match(commandtext)
	if matches:
		cmd = ''
		#print(matches.groups())
		if matches.group(2) or matches.group(4):
			cmd = matches.group(1)
		#print('Command is:',cmd)
		bx = int(matches.group(5))
		by = int(matches.group(6))
		ex = int(matches.group(7))
		ey = int(matches.group(8))
		
		if cmd == 'toggle':
			applyCommand(toggleLight,bx,by,ex,ey)
		elif cmd == 'turn on':
			applyCommand(turnOn,bx,by,ex,ey)
		elif cmd == 'turn off':
			applyCommand(turnOff,bx,by,ex,ey)
		else:
			print("WTF?")
	else:
		print("Bad command syntax")

def countLitLights():
	count = 0
	for x in range(1000):
		for y in range(1000):
			if lightgrid[x][y]:
				count += 1
	print(count, "lights are lit");

# grid initialization
turnoncount = 0
turnoffcount = 0
lightgrid = []
for x in range(1000):
	lightgridcolumn = []
	for y in range(1000):
		lightgridcolumn.append(False)
	lightgrid.append(lightgridcolumn)

#commandInterpreter('turn on 0,0 through 999,999')
#countLitLights()

#commandInterpreter('toggle 0,0 through 999,0')
#countLitLights()

#commandInterpreter('turn off 499,499 through 500,500')
#countLitLights()

cmdcount = 0
with open('adventofcode_day6_input.txt','r') as f:
	for input in f.readlines():
		input = input.rstrip()
		commandInterpreter(input)
		cmdcount += 1

countLitLights()
print('Processed',cmdcount,'commands')
print('Turned on',turnoncount,'times')
print('Turned off',turnoffcount,'times')
