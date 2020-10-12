import sys

r = lambda: sys.stdin.readline().strip()
l = lambda: sys.stdin.readline().strip('\n').split(' ')

n = int(r())
a = l()
p = [0]
for i in a:
	p.append(int(i))

d = [0]*(n+1)

for i in range(1, n+1):
	for j in range(1, i+1):
		d[i] = max(d[i], d[i-j]+int(p[j]))

print(d[n])