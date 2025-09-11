import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
DP = [[-1]*N for _ in range(M)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1

    if DP[y][x] == -1:
        DP[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if graph[ny][nx] < graph[y][x]:
                    DP[y][x] += dfs(ny, nx)
    return DP[y][x]
print(dfs(0, 0))