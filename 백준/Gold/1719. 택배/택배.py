import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
path = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)
    path[a][b] = b
    path[b][a] = a

for i in range(1, n+1):
    graph[i][i] = 0

for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]
                path[start][end] = path[start][mid]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print('-', end= ' ')
        else:
            print(path[i][j], end=' ')
    print()