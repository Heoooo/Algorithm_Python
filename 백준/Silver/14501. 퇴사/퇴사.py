N = int(input())
graph = []
for _ in range(N):
    a, b = map(int, input().split())
    graph.append((a, b))
DP = [0] * (N+1)
for i in range(N-1, -1,-1):
    if i + graph[i][0] > N:
        DP[i] = DP[i+1]
    else:
        DP[i] = max(DP[i+1], DP[i+graph[i][0]] + graph[i][1])
print(DP[0])
