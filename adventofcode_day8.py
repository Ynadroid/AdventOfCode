# Advent of Code Day 8

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
