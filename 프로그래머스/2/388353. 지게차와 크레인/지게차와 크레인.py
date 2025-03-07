from collections import deque
dy = [0,1,0,-1]
dx = [1,0,-1,0]           

def solution(storage, requests):
    
    def update():
        check = [[False] * M for _ in range(N)]
        que = deque()
        que.append((0, 0))
        check[0][0] = True
        while que:
            y, x = que.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not check[ny][nx]:
                    if graph[ny][nx] == '0':
                        que.append((ny, nx))
                        check[ny][nx] = True
                    elif graph[ny][nx] == '1':
                        check[ny][nx] = True
                        que.append((ny, nx))
                        graph[ny][nx] = '0'

                    
                    
    N = len(storage)+2
    M = len(storage[0])+2
    graph = [['0']*M for _ in range(N)]
    
    for i in range(1, N-1):
        for j in range(1, M-1):
            graph[i][j] = storage[i-1][j-1] #0 Padding
    
    for request in requests:
        if len(request) == 1:   #지게차
            tmp = []
            alph = request[0]
            for i in range(1, N-1):
                for j in range(1, M-1):
                    if graph[i][j] == alph:
                        for k in range(4):
                            ny = i + dy[k]
                            nx = j + dx[k]
                            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == '0':    #만약 외부와 연결될 경우(지게차가 들어올 수 있음)
                                tmp.append((i, j))
                                break
            for ti, tj in tmp:
                graph[ti][tj] = '0'
            update()
        
        else:
            alph = request[0]
            for i in range(1, N-1):
                for j in range(1, M-1):
                    if graph[i][j] == alph:
                        graph[i][j] = '1'
            update()
        

        rs = 0
        for i in range(1, N-1):
            for j in range(1, M-1):
                if graph[i][j] != '0' and graph[i][j] != '1':
                    rs += 1                                                                                      
                                
    return rs
            
    