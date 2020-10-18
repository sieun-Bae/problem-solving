n, m = map(int, input().split())
a = [ list(map(int, input())) for _ in range(n) ]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

chk = [ [0]*m for _ in range(n) ]

q = [[0,0]]
chk[0][0] = 1

while q:
	x, y = q.pop(0)

	for i in range(4):
		nx = x+dx[i]
		ny = y+dy[i]

		if nx<0 or nx >= n: continue
		if ny<0 or ny >= m: continue
		if a[nx][ny] == 0: continue #벽
		if chk[nx][ny] != 0: continue #이미 방문

		chk[nx][ny] = chk[x][y]+1
		q.append([nx, ny])

print(chk[n-1][m-1])
