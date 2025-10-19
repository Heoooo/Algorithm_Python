import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) #N가로, M세로
graph = [list(input().strip()) for _ in range(M)]

W, B = 0, 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(i, j, flag):
    cnt = 0
    que = deque()
    que.append((i,j))
    graph[i][j] = 'X'

    while que:
        y, x = que.popleft()
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if graph[ny][nx] != 'X':
                    if graph[ny][nx] == flag:
                        que.append((ny,nx))
                        graph[ny][nx] = 'X'
    return cnt

for i in range(M):
    for j in range(N):
        if graph[i][j] != 'X':
            if graph[i][j] == 'W':
                W += (bfs(i,j,'W'))**2
            elif graph[i][j] == 'B':
                B += (bfs(i,j,'B'))**2
print(W, B)

    
