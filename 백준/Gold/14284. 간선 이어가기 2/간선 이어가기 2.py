import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [float('inf')] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
s, t = map(int, input().split())

heap = [(0, s)]
dist[s] = 0
while heap:
    w, node = heapq.heappop(heap)
    if w > dist[node]:
        continue

    for nw, next_node in graph[node]:
        if nw + dist[node] < dist[next_node]:
            dist[next_node] = nw + dist[node]
            heapq.heappush(heap, (dist[next_node], next_node))
print(dist[t])
