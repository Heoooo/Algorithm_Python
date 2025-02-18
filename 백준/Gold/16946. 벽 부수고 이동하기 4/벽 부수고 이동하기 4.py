import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
zero = [[0]*M for _ in range(N)]
z_dict = { }
dy = [0,1,0,-1]
dx = [1,0,-1,0]
rs = [[0]*M for _ in range(N)]

check = [[False]*M for _ in range(N)]
idx = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not check[i][j]:
            check[i][j] = True
            que = deque()
            que.append((i, j))
            tmp = 1
            z = [(i, j)]
            while que:
                y, x = que.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < M:
                        if not check[ny][nx] and graph[ny][nx] == 0:
                            check[ny][nx] = True
                            que.append((ny, nx))
                            z.append((ny, nx))
                            tmp += 1
            for zy, zx in z:
                zero[zy][zx] = idx
            z_dict[idx] = tmp
            idx += 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            r = 1
            tmp = set()
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if 0 <= ny < N and 0 <= nx < M:
                    if zero[ny][nx] > 0:
                        tmp.add(zero[ny][nx])
            for t in tmp:
                r += z_dict[t]
            rs[i][j] = r%10

#print(zero)
#print(z_dict)
for r in rs:
    print(''.join(map(str, r)))
