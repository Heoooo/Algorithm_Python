N = int(input())
graph = [[0]*N for _ in range(N)]
K = int(input())
time = 0
direction = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]
for _ in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
L = int(input())
cmds = []
for _ in range(L):
    a, b = map(str, input().split())
    cmds.append((a, b))
graph[0][0] = 2
tail = [(0,0)]
y,x = 0, 0
while True:
    time += 1
                
    ny = y + dy[direction]
    nx = x + dx[direction]
    if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] != 2:
        if graph[ny][nx] == 0: #사과가 아닐 시 
            graph[ny][nx] = 2
            ty, tx = tail.pop(0)
            graph[ty][tx] = 0
            tail.append((ny, nx))
        elif graph[ny][nx] == 1: #사과 먹을 시 
            graph[ny][nx] = 2
            tail.append((ny, nx))
    else:
        break
    for cmd in cmds:
        if time == int(cmd[0]):
            if cmd[1] == 'D':
                direction = (direction+1) % 4
            elif cmd[1] == 'L':
                direction = (direction-1) % 4
            cmds.pop(0)
    y = ny
    x = nx
print(time)

            