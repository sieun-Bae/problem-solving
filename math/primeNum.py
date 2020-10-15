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

print(prime_root(499))