# Advent Of Code Day5 part 2

def followProperty1(text):
	maxpos = len(text) - 3
	bpos = 0
	epos = bpos+2
	while bpos <= maxpos:
		before = text[:bpos]
		after = text[epos:]
		seq = text[bpos:epos]
		#print(text, before, seq, after)
		if seq in before or seq in after:
			return True
		bpos += 1
		epos = bpos + 2
	return False

def followProperty2(text):
	# after this position the prop 2 is unreachable
	maxpos = len(text) - 3
	pos = 0
	while pos <= maxpos:
		#print(text[pos],text[pos+2])
		if text[pos] == text[pos+2]:
			return True
		else:
			pos += 1
	return False

def isNice(text):
	return followProperty1(text) and followProperty2(text)
	
# MAIN SCRIPT

total = 0
count = 0

input = 'qjhvhtzxzqqjkmpb'
print(input, isNice(input), True)

input = 'xxyxx'
print(input, isNice(input), True)

input = 'uurcxstgmygtbstg'
print(input, isNice(input), False)

input = 'ieodomkazucvgmuy'
print(input, isNice(input), False)

print("REAL")
with open('adventofcode_day5_input.txt','r') as f:
	for input in f.readlines():
		total += 1
		input = input.rstrip()
		if isNice(input):
			count += 1
			
print("Santa has",count,"/",total,"nice strings (naughty Santa...)")
