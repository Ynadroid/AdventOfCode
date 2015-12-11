# Advent of Code Day 8

def countCharacters(string):
	pos = 0
	count = 0
	inString = False
	oneBackSlash = False
	hexaCharacter = False
	while pos < len(string):
		c = string[pos]
		if c == '"' and not inString:
			inString = True
			pos += 1
			continue
		if inString:
			if hexaCharacter:
				pos += 2
				hexaCharacter = False
				continue
			
			if c == '\\':
				oneBackSlash = True
				pos += 1
				continue
			elif oneBackSlash and c == 'x':
				hexaCharacter = True
				pos += 1
				continue
				
			if oneBackSlash:
				count += 1
				pos += 1
				oneBackSlash = False
				continue
			
			count += 1
			pos += 1
	print(count)
	return count-1

with open('adventofcode_day8_test_input.txt') as f:
#with open('adventofcode_day8_input.txt') as f:
	input = [line.strip() for line in f]

charofcodecount = 0
charcount = 0

for string in input:
	print(string)
	charofcodecount += len(string)
	charcount += countCharacters(string)

print("Total characters of code count:",charofcodecount)
print("Total characters count:",charcount)
