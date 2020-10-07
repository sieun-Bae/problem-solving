import sys
r = lambda: sys.stdin.readline().strip()

n = int(r())

stack = []

for k in range(n):
	command = r()
	if command[:4] == 'push':
		num = int(command[4:])
		stack.append(num)
	elif command == 'top':
		if len(stack) > 0:
			print(stack[-1])
		else:
			print(-1)
	elif command == 'size':
		print(len(stack))
	elif command == 'empty':
		if len(stack) == 0:
			print('true')
		else:
			print('stack is not empty...')
	elif command == 'pop':
		if len(stack) > 0:
			print(stack.pop())
		else:
			print(-1)