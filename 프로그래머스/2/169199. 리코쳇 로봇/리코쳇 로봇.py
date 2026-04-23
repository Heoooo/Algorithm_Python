from collections import deque
def solution(board):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                starty = i
                startx = j
            if board[i][j] == 'G':
                endy = i
                endx = j
    check = [[False]*len(board[0]) for _ in range(len(board))]
    check[starty][startx] = True
    que = deque([(starty, startx, 0)])
    rs = 0
    while que:
        y, x, cnt = que.popleft()
        if y == endy and x == endx:
            return cnt
        
        for k in range(4):
            ny = y
            nx = x
            while True:
                ny += dy[k]
                nx += dx[k]
                if not(0 <= ny < len(board) and 0 <= nx < len(board[0])) or board[ny][nx] == 'D':
                    ny -= dy[k]
                    nx -= dx[k]
                    break
            
            if check[ny][nx] == False:
                check[ny][nx] = True
                que.append((ny, nx, cnt+1))
    return -1
                        
        
    