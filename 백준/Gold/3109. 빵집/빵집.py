import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

R, C = map(int, input().split()) #R은 y, C는 x
graph = [list(input().strip()) for _ in range(R)]

dy = [-1,0,1]

rs = 0
def dfs(y, x):
    if x == C-1:
        return True

    for i in range(3):
        ny = y + dy[i]
        nx = x + 1
        if 0 <= ny < R and 0 <= nx < C:
            if graph[ny][nx] != 'x':
                graph[ny][nx] = 'x'
                if dfs(ny, nx) == True:
                    return True
    return False

for i in range(R):
    if dfs(i,0) == True:
        rs += 1
print(rs)
