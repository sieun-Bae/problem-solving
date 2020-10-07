import sys
r = lambda: sys.stdin.readline().strip()

def isValid(s):
	n = len(s)
	cnt = 0
	for x in s:
		if x == '(':
			cnt += 1
		else:
			cnt -= 1
		if cnt < 0:
			return "false.." # '(' < ')'
	if cnt == 0:
		return "true.."
	else:
		return "false.." # '(' > ')'

n = int(r())

for i in range(n):
	print(isValid(r()))