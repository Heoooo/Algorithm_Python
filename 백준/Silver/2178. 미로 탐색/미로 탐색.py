import sys
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

check = [[0] * M for _ in range(N)]
que = deque()

def bfs(a, b):
    que.append((a,b))
    check[a][b] = 1
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if check[ny][nx] == 0:
                    if graph[ny][nx] == 1:
                        check[ny][nx] = check[y][x] + 1
                        que.append((ny,nx))
bfs(0, 0)
print(check[N-1][M-1])