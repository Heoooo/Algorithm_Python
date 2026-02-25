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

heap = [(0, 1)]
dist[1] = 0

while heap:
    w, node = heapq.heappop(heap)
    if w > dist[node]:
        continue
    for nw, next_node in graph[node]:
        cost = dist[node] + nw
        if cost < dist[next_node]:
            dist[next_node] = cost
            heapq.heappush(heap, (dist[next_node], next_node))

print(dist[N])
