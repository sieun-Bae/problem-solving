import sys

r = lambda: sys.stdin.readline().strip()
s = int(r())

d = [0]*11

d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, 11):
	d[i] = d[i-1]+d[i-2]+d[i-3]


for i in range(s):
	n = int(r())
	print(d[n]) 
	 