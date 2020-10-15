#10 -> b 진법

def tentob():
	n, b = map(int, input().split())
	ans = ''

	while n>0:
		r = n%b
		ans += str(r)

		n = n//b

	print(''.join(reversed(ans))) #list(ans), ans.reverse, ''.join(ans)

def btoten():
	ans = 0
	s = input()
	b = int(input())

	for i in range(0, len(s)):
		ans = ans*b + int(s[i])

	print(ans)

def minustwo(n):
	if n==0:
		return
	if n%2 == 0:
		minustwo(-(n//2))
		print('0')
	else:
		if n>0:
			minustwo(-(n//2))
		else:
			minustwo((-n+1)//2)
		print('1')

if __name__ == '__main__':
	minustwo(-7)