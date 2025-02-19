import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
#0이 아닌 지점부터 bfs()탐색 시작->끊기면 한 덩어리
#bfs()탐색 시 0이라면 check배열 += 1 후에 graph에서 check 값 빼기
#while로 반복 덩어리가 두 개가 되거나 graph 모든 값이 0일시 종료
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(i, j):
    que = deque()
    que.append((i, j))
    check[i][j] = 0
    while que:
        y, x = que.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if check[ny][nx] == -1:
                    if graph[ny][nx] != 0:
                        que.append((ny, nx))
                        check[ny][nx] = 0
                    else:
                        check[y][x] += 1

rs = 0
while True:
    cnt = 0
    check = [[-1]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and check[i][j] == -1:
                bfs(i, j)
                cnt += 1
    if cnt >= 2:
        print(rs)
        break
    
    if cnt == 0:
        print(0)
        break

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                graph[i][j] = max(0, graph[i][j] - check[i][j])
    rs += 1
    
