from collections import deque
def solution(maps):
    def bfs(i, j):
        que = deque()
        tmp = int(maps[i][j])
        check[i][j] = True
        que.append((i, j))
        while que:
            y, x = que.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if not check[ny][nx] and maps[ny][nx] != 'X':
                        check[ny][nx] = True
                        tmp += int(maps[ny][nx])
                        que.append((ny, nx))
        return tmp
            
    N = len(maps)
    M = len(maps[0])
    check = [[False]*M for _ in range(N)]
    
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    rs = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not check[i][j]:
                tmp = bfs(i, j)
                rs.append(tmp)
    
    if len(rs) == 0:
        return [-1]
    else:
        rs.sort()
        return rs
                
    
                