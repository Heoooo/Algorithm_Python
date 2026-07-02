def solution(maze):
    global rs
    N = len(maze)
    M = len(maze[0])
    
    check_r = [[False] * M for _ in range(N)]
    check_b = [[False] * M for _ in range(N)]
    
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    rs = 999999
    
    ry, rx = 0, 0
    by, bx = 0, 0
    
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                ry = i
                rx = j
            if maze[i][j] == 2:
                by = i
                bx = j
    
    check_r[ry][rx] = True
    check_b[by][bx] = True
    
    def back(ry, rx, by, bx, cnt):
        global rs
        
        if cnt >= rs:
            return
        
        if maze[ry][rx] == 3 and maze[by][bx] == 4:
            rs = min(rs, cnt)
            return 
        
        if maze[ry][rx] == 3:
            r_dir = [4]
        else:
            r_dir = [0,1,2,3]
        
        if maze[by][bx] == 4:
            b_dir = [4]
        else:
            b_dir = [0,1,2,3]
            
        for i in r_dir:
            for j in b_dir:
                if i == 4:
                    nry = ry
                    nrx = rx
                else:
                    nry = ry + dy[i]
                    nrx = rx + dx[i]
                    
                if j == 4:
                    nby = by
                    nbx = bx
                else:
                    nby = by + dy[j]
                    nbx = bx + dx[j]
                
                if not (0 <= nry < N and 0 <= nrx < M) or maze[nry][nrx] == 5:
                    continue
                if not (0 <= nby < N and 0<= nbx < M) or maze[nby][nbx] == 5:
                    continue
                    
                if i != 4 and check_r[nry][nrx]:
                    continue
                if j != 4 and check_b[nby][nbx]:
                    continue
                
                if nry == nby and nrx == nbx:
                    continue
                    
                if nry == by and nrx == bx and nby == ry and nbx == rx:
                    continue
                    
                check_r[nry][nrx] = True
                check_b[nby][nbx] = True
                
                back(nry, nrx, nby, nbx, cnt+1)
                check_r[nry][nrx] = False
                check_b[nby][nbx] = False
    
    back(ry, rx, by, bx, 0)
    if rs == 999999:
        return 0
    else:
        return rs
        