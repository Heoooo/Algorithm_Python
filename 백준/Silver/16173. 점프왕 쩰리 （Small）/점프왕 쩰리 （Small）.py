from collections import deque
dy = [1, 0]
dx = [0, 1]
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
check = [[False]*N for _ in range(N)]

que = deque()
que.append((0, 0))
check[0][0] = True
while que:
    y, x = que.popleft()
    if y == N-1 and x == N-1:
        break
    for i in range(2):
        ny = y + dy[i]*graph[y][x]
        nx = x + dx[i]*graph[y][x]
        if 0 <= ny < N and 0 <= nx < N and check[ny][nx] == False:
            check[ny][nx] = True
            que.append((ny, nx))
    
if check[N-1][N-1] == 0:
    print("Hing")
else:
    print("HaruHaru")
