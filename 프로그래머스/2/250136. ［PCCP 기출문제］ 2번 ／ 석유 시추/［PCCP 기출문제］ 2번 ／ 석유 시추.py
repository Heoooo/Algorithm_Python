from collections import deque, defaultdict
def solution(land):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    N = len(land)
    M = len(land[0])
    pt = defaultdict(int)
    idx = 0 #석유 땅 번호
    rs = 0
    check = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and check[i][j] == 0:
                idx += 1
                que = deque()
                que.append((i, j))
                check[i][j] = idx
                pt[idx] += 1
                while que:
                    y, x = que.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < N and 0 <= nx < M:
                            if check[ny][nx] == 0 and land[ny][nx] == 1:
                                check[ny][nx] = idx
                                que.append((ny, nx))
                                pt[idx] += 1
    
    for j in range(M):
        tmp = 0
        t = []
        for i in range(N):
            if land[i][j] == 1:
                if check[i][j] not in t:
                    t.append(check[i][j])
                    tmp += pt[check[i][j]]
        rs = max(rs, tmp)
                    
    return rs