import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [float('inf')] * (N+1)
prev = [0] * (N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start, end):
    dist = [float('inf')] * (N+1)
    heap = [(0, 1)]
    dist[1] = 0
    while heap:
        w, node = heapq.heappop(heap)

        if w > dist[node]:
            continue

        for nw, next_node in graph[node]:
            if node == start and next_node == end:
                continue
            if nw + dist[node] < dist[next_node]:
                dist[next_node] = nw + dist[node]
                heapq.heappush(heap, (dist[next_node], next_node))
                prev[next_node] = node
    return dist[N]

heap = [(0, 1)]
dist[1] = 0
while heap:
    w, node = heapq.heappop(heap)

    if w > dist[node]:
        continue

    for nw, next_node in graph[node]:
        if nw + dist[node] < dist[next_node]:
            dist[next_node] = nw + dist[node]
            heapq.heappush(heap, (dist[next_node], next_node))
            prev[next_node] = node

tmp = []
k = N
while True:
    if k == 1:
        break
    tmp.append((prev[k], k))
    k = prev[k]

rs = 0
for start, end in tmp:
    rs = max(rs, dijkstra(start, end))
print(rs)
