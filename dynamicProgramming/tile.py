import sys

r = lambda: sys.stdin.readline().strip()
s = int(r())

def go(n):
	d[0] = 1
	d[1] = 1
	for i in range(2, n+1):
		d[i] = d[i-1]+d[i-2]
		d[i] = d[i]%10007
	return d[n]

def go_two(n):
	d[0] = 1
	d[1] = 1
	for i in range(2, n+1):
		d[i] = d[i-1]+2*d[i-2]
		d[i] = d[i]%10007
	return d[n] 

def main():
	global d
	d = [0]*1500
	print(go_two(s))

if __name__ == '__main__':
	main()
