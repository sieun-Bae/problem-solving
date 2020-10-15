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

def sieveOfEratosthenes(): # False: 지워진 것 (소수가 아닌 것), True: 지워지지 않음 (소수)
	p = list()
	c = list(range(0, 101))
	for i in range(2, 101):
		if c[i]:
			p.append(i)
			j = i*i #정수 overflow 막기 위해 i*2로 하기도
			while j<=100:
				c[j] = False
				j += i
	print(p)

def goldbach():
	p = list()
	c = list(range(0, 1000001))
	
	for i in range(2, 1000001):
		if c[i]:
			p.append(i)
			j = i+i #정수 overflow 막기 위해 i*2로 하기도
			while j<=1000000:
				c[j] = False
				j += i
	while True:
		n = int(input())
		if n==0:
			break
		for i in range(1, len(p)):
			if c[n-p[i]]:
				print(n,"=",p[i],"+",n-p[i])
				break

goldbach()