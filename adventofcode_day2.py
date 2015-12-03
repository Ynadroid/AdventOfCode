import sys, re, decimal

def minIsL(l, w, h):
	return (l <= w and l <= h)

def minIsH(l, w, h):
	return (h <= l and h <= w)
	
def minIsW(l, w, h):
	return (w <= l and w <= h)

totalsize = 0
totalribbon = 0
	
l = 10
w = 1
h = 1

rp1 = 0
rp2 = l*w*h
sizep1 = 2*l*w + 2*w*h + 2*h*l
sizep2 = 0
if minIsL(l,w,h):
	sizep2 = l*min(w,h)
	rp1 = l+min(w,h)+l+min(w,h)
elif minIsH(l,w,h):
	sizep2 = h*min(w,l)
	rp1 = h+min(w,l)+h+min(w,l)
elif minIsW(l,w,h):
	sizep2 = w*min(l,h)
	rp1 = w+min(l,h)+w+min(l,h)
	
size = sizep1 + sizep2
ribbon = rp1 + rp2

print(size, ribbon)

inputfile = open("adventofcode_day2_input.txt");
for line in inputfile:
	line = line.rstrip()
	#print('#'+line+'#')
	lol = line.split('x')
	lul = list(map(int, lol))
	l=lul[0]
	w=lul[1]
	h=lul[2]
	#print(l,w,h)
	
	rp1 = 0
	rp2 = l*w*h
	sizep1 = 2*l*w + 2*w*h + 2*h*l
	sizep2 = 0
	if minIsL(l,w,h):
		sizep2 = l*min(w,h)
		rp1 = l+min(w,h)+l+min(w,h)
	elif minIsH(l,w,h):
		sizep2 = h*min(w,l)
		rp1 = h+min(w,l)+h+min(w,l)
	elif minIsW(l,w,h):
		sizep2 = w*min(l,h)
		rp1 = w+min(l,h)+w+min(l,h)
		
	size = sizep1 + sizep2
	totalsize = totalsize + size
	
	ribbon = rp1 + rp2
	totalribbon = totalribbon + ribbon

# Size of wrapping paper = 2*l*w + 2*w*h + 2*h*l
# Total size = [Size] + area of smallest size

# Smallest size = ? multiplication of the 2 smallest length

print("The little elves need",totalsize,"ft² of wrapping paper")
print("And",totalribbon,"ft of ribbon")
