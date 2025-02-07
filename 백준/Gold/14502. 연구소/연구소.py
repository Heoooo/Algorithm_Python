import sys
from collections import deque
import copy
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0

def bfs():
    que = deque()
    temp_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 2:
                que.append((i,j))
    while que:
        y,x = que.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if temp_graph[ny][nx] == 0:
                    temp_graph[ny][nx] = 2
                    que.append((ny,nx))

    global cnt
    tmp = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                tmp += 1
    cnt = max(cnt, tmp)

def wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count+1)
                graph[i][j] = 0

wall(0)
print(cnt)    