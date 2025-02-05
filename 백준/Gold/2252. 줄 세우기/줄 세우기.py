import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    degree[b] += 1
    graph[a].append(b)

rs = []
que = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        que.append(i)

while que:
    k = que.popleft()
    for next_node in graph[k]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            que.append(next_node)
    rs.append(k)
print(*rs)
