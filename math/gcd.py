a, b = map(int, input().split())

gcd = 1
def loop():
	for i in range(2, min(a,b)):
		if a%i == 0 and b%i == 0:
			gcd = i

def gcd():
	if b==0:
		return a
	else:
		return gcd(b, a%b)
def gcd_loop():
	while b!=0:
		r = a%b
		a = b
		b = r
	return a 

print(gcd)