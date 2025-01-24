import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

rs = float('inf')
for i in range(3):
    DP = [[float('inf')] * 3 for _ in range(N)]

    DP[0][i] = graph[0][i]
    
    for j in range(1, N):
        DP[j][0] = min(DP[j-1][1], DP[j-1][2]) + graph[j][0]
        DP[j][1] = min(DP[j-1][0], DP[j-1][2]) + graph[j][1]
        DP[j][2] = min(DP[j-1][0], DP[j-1][1]) + graph[j][2]

    for k in range(3):
        if i != k:
            rs = min(rs, DP[N-1][k])
print(rs)

