# Advent Of Code Day5

def numberOfVowels(text):
	count = 0
	for c in text:
		if c in 'aeiou':
			count += 1
	#if count < 3:
		#print("Vowels:",count)
	return count

def hasDoubleLetter(text):
	lastc = ''
	for c in text:
		if c == lastc:
			return True
		else:
			lastc = c
	#print("No double letter")
	return False

def hasNaughtySequences(text):
	return not ('ab' not in text and 
		'cd' not in text and 
		'pq' not in text and
		'xy' not in text)
	
def isNice(text):
	return (numberOfVowels(text) >= 3 
		and hasDoubleLetter(text) 
		and (not hasNaughtySequences(text)))


# MAIN SCRIPT
# 278 is too high

total = 0
count = 0

print("TEST")
print('ugknbfddgicrmopn',True,isNice('ugknbfddgicrmopn'),'\n')
print('aaa',True,isNice('aaa'),'\n')
print('jchzalrnumimnmhp',False,isNice('jchzalrnumimnmhp'),'\n')
print('haegwjzuvuyypxyu',False,isNice('haegwjzuvuyypxyu'),'\n')
print('dvszwmarrgswjxmb',False,isNice('dvszwmarrgswjxmb'),'\n')

print("REAL")
with open('adventofcode_day5_input.txt','r') as f:
	for input in f.readlines():
		total += 1
		input = input.rstrip()
		#print(input)
		if isNice(input):
			count += 1
			print(input,'nice','\n\n')
		#else:
			#print(input,'not nice','\n\n')
			
print("Santa has",count,"/",total,"nice strings (naughty Santa...)")
