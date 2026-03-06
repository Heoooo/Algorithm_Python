import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

wc = []
vc = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            wc.append((i, j))
        elif graph[i][j] == 2:
            vc.append((i, j))
            
rs = 0

def bfs():
    que = deque()
    tmp_graph = [row[:] for row in graph]
    for y, x in vc:
        que.append((y, x))

    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if tmp_graph[ny][nx] == 0:
                    tmp_graph[ny][nx] = 2
                    que.append((ny, nx))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 0:
                cnt += 1
    return cnt


for comb in combinations(wc, 3):
    for y, x in comb:
        graph[y][x] = 1
    rs = max(rs, bfs())
    for y, x in comb:
        graph[y][x] = 0

print(rs)