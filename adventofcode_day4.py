import hashlib

input = 'ckczppom'
#input = 'abcdef'
#input = 'pqrstuv'
answer = 0
hash = ''

numberofzeros = 6

while '0'*numberofzeros != hash[:numberofzeros]:
	test = input + str(answer)
	#print(test)
	hasher = hashlib.new('md5')
	hasher.update(test.encode('utf-8'))
	hash = hasher.hexdigest()
	#print(hash,hash[:5],answer)
	answer += 1

print(test,hash,hash[:numberofzeros],answer-1)

print("LOL HELLO PYTHON!",answer-1)
