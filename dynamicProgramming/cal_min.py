import sys

#top-down
def go(n):
	global d
	if n == 1:
		return 0
	if d[n] > 0:
		return d[n]
	d[n] = go(n-1) + 1 # -1연산의 값을 일단 메모해두고
	if n%2 == 0:
		temp = go(n//2) + 1
		if d[n] > temp:
			d[n] = temp # 2로 나눈 연산의 값이 작으면 그 값으로 대체
	if n%3 == 0:
		temp = go(n//3) + 1
		if d[n] > temp:
			d[n] = temp
	return d[n]

#bottom-up
def go_dp(n):
	global d
	d[1] = 0
	for i in range(2, n+1):
		d[i] = d[i-1]+1
		if i%2==0 and d[i] > d[i//2]+1:
			d[i] = d[i//2]+1
		if i%3==0 and d[i] > d[i//3]+1:
			d[i] = d[i//3]+1

r = lambda: sys.stdin.readline().strip()
n = int(r())

def main():
	global d
	d = [0]*pow(10, 6)


	print(go(10))

if __name__ == '__main__':
	main()'''