# Advent of Code Day 7
import re
import struct
from adventofcode_day7_class_wire import *

def isNumericValue(text):
	numericValuePattern = re.compile('[0-9]{1,}')
	return numericValuePattern.match(text) != None

commandPattern = re.compile('((((.*) )?(AND|LSHIFT|NOT|OR|RSHIFT) )?(.*)) -> (.*)')

with open('adventofcode_day7_input_p2.txt') as f:
# with open('adventofcode_day7_input.txt') as f:
# with open('adventofcode_day7_test_input.txt') as f:
	input = [line.strip() for line in f]

# Reading all commands to create all the wires
# command = 'x AND y -> z'
for command in input:
	matches = commandPattern.match(command)
	if matches:
		# print(command,' - ',matches.groups())
		if matches.group(4):
			createWire(matches.group(4))
		createWire(matches.group(6))
		createWire(matches.group(7))
	else:
		print(command,'- No match')

print("Created",len(Wire.AllWires),"Wires")

print(len(input))
processedAtLeastOneCmd = True
while len(input) > 0 and processedAtLeastOneCmd:
	processedAtLeastOneCmd = False
	for command in input:
		matches = commandPattern.match(command)
		if matches:
			#print(command,matches.groups())
			dstWire = Wire.AllWires[matches.group(7)]
			# Direct signal assigation
			if matches.group(4) == None and isNumericValue(matches.group(6)):
				dstWire.signal = int(matches.group(6))
				print('Assigned signal', dstWire.signal, 'to Wire', dstWire.name)
				processedAtLeastOneCmd = True
				input.remove(command)
			# Wire to Wire assignation
			elif matches.group(4) == None and matches.group(6) != None and matches.group(5) == None:
				print('Direct wire to wire assignation')
				print(command,' - ',matches.groups())
				srcWire = Wire.AllWires[matches.group(6)]
				if srcWire.signalDefined():
					dstWire.signal = srcWire.signal
					print('Assigned Wire',srcWire.name,srcWire.signal,'to',dstWire.name)
				else:
					print('No signal in Wire',srcWire.name,'yet')
			elif matches.group(5) != None and matches.group(4) == None:
				src2 = matches.group(6)
				if isNumericValue(src2):
					srcsignal2 = int(src2)
				else:
					srcsignal2 = Wire.AllWires[src2].signal
					
				if srcsignal2 != None:
					dstWire.signal = ~srcsignal2
					dstWire.signal &= 0x0000FFFF
					print('Assigned Wire',src2,'not',srcsignal2,'to',dstWire.name,dstWire.signal)
					processedAtLeastOneCmd = True
					input.remove(command)
				else:
					print('NOT',src2,srcsignal2)
			# Generic case for bitwise operations
			elif matches.group(5) != None:
				op = matches.group(5)
				src1 = matches.group(4)
				src2 = matches.group(6)
				
				# define signal sources
				srcsignal1 = 0
				srcsignal2 = 0
				
				if isNumericValue(src1):
					srcsignal1 = int(src1)
				else:
					srcsignal1 = Wire.AllWires[src1].signal
					
				if isNumericValue(src2):
					srcsignal2 = int(src2)
				else:
					srcsignal2 = Wire.AllWires[src2].signal
				
				if op == 'AND':
					if srcsignal1 != None and srcsignal2 != None:
						dstWire.signal = srcsignal1 & srcsignal2
						print('Assigned Wire',src1,srcsignal1,'and',src2,srcsignal2,'to',dstWire.name,dstWire.signal)
						processedAtLeastOneCmd = True
						input.remove(command)
					else:
						print('AND',src1,srcsignal1,'and',src2,srcsignal2)
				elif op == 'OR':
					if srcsignal1 != None and srcsignal2 != None:
						dstWire.signal = srcsignal1 | srcsignal2
						print('Assigned Wire',src1,srcsignal1,'or',src2,srcsignal2,'to',dstWire.name,dstWire.signal)
						processedAtLeastOneCmd = True
						input.remove(command)
					else:
						print('OR',src1,srcsignal1,'and',src2,srcsignal2)
				else:
					if op == 'RSHIFT':
						if srcsignal1 != None:
							dstWire.signal = srcsignal1 >> srcsignal2
							dstWire.signal &= 0x0000FFFF
							processedAtLeastOneCmd = True
							input.remove(command)
						else:
							print('RSHIFT',src1,srcsignal1)
					elif op == 'LSHIFT':
						print(srcsignal1,srcsignal2)
						if srcsignal1 != None:
							dstWire.signal = srcsignal1 << srcsignal2
							dstWire.signal &= 0x0000FFFF
							processedAtLeastOneCmd = True
							input.remove(command)
						else:
							print('LSHIFT',src1,srcsignal1)
					else:
						print('Unknown command')
			else:
				print('WTF?', command)
		else:
			print('Invalid command in list')
			break

	if not processedAtLeastOneCmd:
		print('Will not continue as no command could be executed')
print(len(input))

for command in input:
	print(command)
	

#for w in Wire.AllWires:
	#print(Wire.AllWires[w].name,Wire.AllWires[w].signal)

finalWire = Wire.AllWires['a']
print('Wire',finalWire.name,'has signal',finalWire.signal)
