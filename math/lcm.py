def gcd(x, y):
	if y==0:
		return x
	else:
		return gcd(y, x%y)

def main():
	a, b = map(int, input().split())
	g = gcd(a, b)
	l = a*b/g #g*(a/g)*(b/g)
	print(l)