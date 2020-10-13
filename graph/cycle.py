a = map(int, input().split())

def dfs(x):
	if c[x] == 1:
		return
	c[x] = 1
	dfs(a[x])

def dfs_bu(x):
	while c[x] == 0:
		c[x] = 1
		x = a[x]

ans = 0
for i in range(1, n+1):
	if c[i] == 0:
		dfs(i)
		ans += 1

