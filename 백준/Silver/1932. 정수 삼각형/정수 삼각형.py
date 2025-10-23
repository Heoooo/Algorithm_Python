import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for i in range(N)]

for i in range(N):
    dp[N-1][i] = graph[N-1][i]

for i in range(N-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j],dp[i+1][j+1]) + graph[i][j]

print(dp[0][0])