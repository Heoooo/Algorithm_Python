from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    sy, se = 0, 0
    ey, ee = 0, 0
    check = [[-1] * M for _ in range(N)]
    
    que = deque()
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'L':
                check[i][j] = 0
                que.append((i, j))
            if maps[i][j] == 'S':
                sy = i
                se = j
            if maps[i][j] == 'E':
                ey = i
                ee = j
                
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if check[ny][nx] == -1 and maps[ny][nx] != 'X':
                    check[ny][nx] = check[y][x] + 1
                    que.append((ny, nx))
                    
    if check[sy][se] == -1 or check[ey][ee] == -1:
        return -1
    else:
        return check[sy][se] + check[ey][ee]
        