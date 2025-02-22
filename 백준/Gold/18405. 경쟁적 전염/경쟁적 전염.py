import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

que = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            que.append((graph[i][j],i,j,0))

que.sort()
que = deque(que)
dy = [0,1,0,-1]
dx = [1,0,-1,0]

cnt = 0
while que:
    vir, y, x, time = que.popleft()
    if time == S:
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if graph[ny][nx] == 0:
                graph[ny][nx] = vir
                que.append((graph[ny][nx],ny,nx,time+1))

print(graph[X-1][Y-1])