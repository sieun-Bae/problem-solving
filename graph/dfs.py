#풀어보기 https://m.blog.naver.com/wpghks7/221604689852

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#연결된 그래프 모두 탐색, 가중치가 모두 같을 경우 최단거리
def bfs(graph, start):
	visited = []
	queue = [start]

	while queue:
		#print('queue:',queue)
		n = queue.pop(0)
		#print('n:',n)
		if n not in visited:
			#print('visited:', visited)
			visited.append(n)
			queue += graph[n] - set(visited)
			#print('queue:',queue)
	return visited

#연결된 그래프 모두 탐색, 특정 조합을 뽑는 경우
def dfs(graph, start):
	visited = []
	stack = [start]

	while stack:
		#print('stack:',stack)
		n = stack.pop()
		#print('n:',n)
		if n not in visited:
			#print('visited:', visited)
			visited.append(n)
			stack += graph[n] - set(visited)
			#print('stack:', stack)
	return visited

def bfs_paths(graph, start, goal):
	queue = [(start, [start])]
	result = []

	while queue:
		n, path = queue.pop(0)
		if n == goal:
			result.append(path)
		else:
			for m in graph[n]-set(path):
				queue.append((m, path+[m]))
	return result

def dfs_paths(graph, start, goal):
	stack = [(start, [start])]
	result = []

	while stack:
		n, path = stack.pop()
		if n==goal:
			result.append(path)
		else:
			for m in graph[n] - set(path):
				stack.append((m, path+[m]))
		return result

def connected_component():
	for i in graph.keys():
		dfs(graph, i)
		component += 1
	return component

print('dfs')
print(dfs(graph, 'A'))
print('bfs')
print(bfs(graph, 'A'))