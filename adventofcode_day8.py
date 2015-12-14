# Advent of Code Day 8

import codecs

def countCharacters(string):
	#print('----- counting',string)
	pos = 0
	count = 0
	inString = False
	oneBackSlash = False
	hexaCharacter = False
	while pos < len(string):
		c = string[pos]
		if c == '"' and not inString:
			#print('Entering in string')
			inString = True
			pos += 1
			continue
		if inString:
			if hexaCharacter:
				#print('Hexa not counted', pos, pos+2)
				pos += 2
				count += 1
				hexaCharacter = False
				oneBackSlash = False
				continue
			
			if c == '\\' and not oneBackSlash:
				#print('Backslash counted')
				oneBackSlash = True
				pos += 1
				continue
			elif oneBackSlash and c == 'x':
				#print('Hexa detected')
				hexaCharacter = True
				pos += 1
				continue
				
			if oneBackSlash:
				#print('Counting backslash',c)
				count += 1
				pos += 1
				oneBackSlash = False
				continue
			elif c == '"':
				#print('End of string')
				pos += 1
				continue
			
			#print('Normal counting',c,pos,count)
			count += 1
			pos += 1
	#print(count)
	return count

def addAndCountCharacters(string):
	pos = 0
	addedString = []
	addedString.append('"')
	while pos < len(string):
		c = string[pos]
		if c == '"':
			addedString.append('\\'+c)
		elif c == '\\':
			if string[pos+1] == '"':
				addedString.append('\\\\'+c)
				addedString.append(string[pos+1])
				pos += 1
			elif string[pos+1] == 'x':
				addedString.append('\\'+c)
				addedString.append(string[pos+1])
				addedString.append(string[pos+2])
				addedString.append(string[pos+3])
				pos += 3
			elif string[pos+1] == '\\':
				addedString.append('\\'+c)
				addedString.append('\\'+string[pos+1])
				pos += 1
		else:
			addedString.append(c)
		pos += 1
	addedString.append('"')
	
	finalString = ''.join(addedString)
	#print(finalString,len(finalString))
	return (finalString,len(finalString))

# with open('adventofcode_day8_test_input.txt') as f:
with open('adventofcode_day8_input.txt') as f:
	input = [line.strip() for line in f]

charofcodecount = 0
charcount = 0

for string in input:
	print(string, ',', len(string), ',', countCharacters(string))
	charofcodecount += len(string)
	charcount += countCharacters(string)

print("Total characters of code count:",charofcodecount)
print("Total characters count:",charcount)
print("Problem part 1 answer:",charofcodecount-charcount)

charofcodecountp2 = 0
addedcharcount = 0

for string in input:
	reencoding = addAndCountCharacters(string)
	print(string, ',', len(string), ',',reencoding[0], ',', reencoding[1])
	charofcodecountp2 += len(string)
	addedcharcount += reencoding[1]

print("Total characters of code count:",charofcodecountp2)
print("Total added characters count:",addedcharcount)
print("Problem part 2 answer:",addedcharcount-charofcodecountp2)
