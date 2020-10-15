import math

def prime(n):
	if n<2:
		return False
	for i in range(2, n): #or (2, n/2)
		if n%i==0:
			return False
	return True

def prime_root(n):
	if n<2:
		return False
	for i in range(2, int(math.pow(n, 0.5))):
		if n%i==0:
			return False
	return True

def sieveOfEratosthenes():
	p = list()
	c = list(range(0, 101))
	print(c)
	for i in range(2, 101):
		if c[i]:
			p.append(i)
			j = i*i #정수 overflow 막기 위해 i*2로 하기도
			while j<=100:
				c[j] = False
				j += i
	print(p)

sieveOfEratosthenes()