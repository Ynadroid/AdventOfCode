# Advent of Code Day 11

def increment(numeric_string, pos = -1):
	if pos < 0:
		pos = len(numeric_string)-1
	
	numeric_string[pos] += 1
	
	if numeric_string[pos] > 25:
		numeric_string[pos] = 0
		return increment(numeric_string, pos-1)
	
	return numeric_string

def stringToNumericArray(string):
	result = []
	for c in string:
		result.append(posinalphabet[c])
	return result
	
def numericArrayToString(array):
	result = []
	for n in array:
		result.append(letterpos[n])
	return ''.join(result)

def checkPasswordRule1(array):
	pos = 0
	while pos < len(array)-2:
		if array[pos+2] - array[pos+1] == 1 and array[pos+1] - array[pos] == 1:
			return True
		else:
			pos += 1
	return False

def checkPasswordRule2(string):
	return ('i' not in string and 'o' not in string and 'l' not in string)

def checkPasswordRule3(array):
	pos = 0
	count = 0
	while pos < len(array)-1:
		if array[pos] == array[pos+1]:
			count += 1
			pos += 1
		pos += 1
		
	return (count >= 2)
	
def checkPassword(array):
	rule1 = checkPasswordRule1(array)
	rule2 = checkPasswordRule2(numericArrayToString(array))
	rule3 = checkPasswordRule3(array)
	#print(rule1, rule2, rule3)
	return (rule1 and rule2 and rule3)

def generatePassword(string):
	oldpassword = string
	array = stringToNumericArray(oldpassword)
	if checkPassword(array):
		array = increment(array)
	
	while not checkPassword(array):
		array = increment(array)
	
	return numericArrayToString(array)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
posinalphabet = {}
letterpos = {}

pos = 0
for letter in alphabet:
	posinalphabet[letter] = pos
	letterpos[pos] = letter
	pos += 1

oldpassword = 'hepxcrrq'
newpassword = generatePassword(oldpassword)
print('Next password from '+oldpassword+' is:',newpassword)

oldpassword = newpassword
newpassword = generatePassword(oldpassword)
print('Next password from '+oldpassword+' is:',newpassword)
