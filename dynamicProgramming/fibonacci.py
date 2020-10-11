import numpy as np
def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)

# top-down N개의 칸*1칸을 채우는 복잡도 => O(N)
def fibonacci_dp(n):
	global memo
	if n <= 1:
		return n 
	else:
		if memo[n] > 0:
			return memo[n]
		memo[n] = fibonacci_dp(n-1) + fibonacci_dp(n-2)
		#print(memo)
		return memo[n]

# bottom-up
def fibonacci_dp_bu(n):
	global d
	d[0] = 0
	d[1] = 1
	for i in range(2, n+1):
		d[i] = d[i-1] + d[i-2]
	return d[n]

def main():
	global memo, d
	memo = np.zeros(shape = 100)
	d = np.zeros(shape = 100)

	print(fibonacci(10))
	print(fibonacci_dp(10))
	print(fibonacci_dp_bu(10))

if __name__ == '__main__':
	main()