from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicken = []
home = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append((i,j))
        elif graph[i][j] == 1:
            home.append((i,j))
            
rs = float('inf')
check = [False] * len(chicken)
def back(idx, cnt, arr):
    global rs
    if cnt == M:
        rs = min(bfs(arr), rs)
        return

    for i in range(idx, len(chicken)):
        if check[i] == False:
            check[i] = True
            back(i+1, cnt+1, arr + [chicken[i]])
            check[i] = False

def bfs(arr):
    tmp = 0
    for hy, hx in home:
        t = float('inf')
        for cy, cx in arr:
            dist = abs(hy-cy) + abs(hx-cx)
            t = min(dist, t)
        tmp += t
    return tmp
    
back(0, 0,[])
print(rs)
