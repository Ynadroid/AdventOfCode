import sys

santax = 0
santay = 0

robox = 0
roboy = 0

roboturn = False

coordlist = set()
coordlist.add((santax,santay))
print(coordlist)

inputfile = open("adventofcode_day3_input.txt");
for line in inputfile:
	line = line.rstrip()
	#line = '^v^v^v^v^v'
	#line = '^>v<'
	#line = '^v'
	for c in line:
		x = 0
		y = 0
		if c == '^':
			y = y+1
		elif c == 'v':
			y = y-1
		elif c == '>':
			x = x+1
		elif c == '<':
			x = x-1
		else:
			print("What the fuck?")
		
		if roboturn:
			robox = robox + x
			roboy = roboy + y
			if (robox,roboy) not in coordlist:
				coordlist.add((robox,roboy))
		else:
			santax = santax + x
			santay = santay + y
			if (santax,santay) not in coordlist:
				coordlist.add((santax,santay))
				
		roboturn = not roboturn

# ^ goes north, v goes south, < goes west, > goes east
	
print("Santa and Robo-Santa has visited",len(coordlist),"unique houses")
