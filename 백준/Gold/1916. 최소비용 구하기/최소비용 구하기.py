import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N = int(input()) #도시 개수
M = int(input()) #버스 개수
edge = [[] for _ in range(N+1)] #간선 연결리스트
dist = [INF] * (N+1) #도시까지의 거리
for _ in range(M):
    s, e, w = map(int, input().split())
    edge[s].append((w,e))
start, end = map(int, input().split())

dist[start] = 0
heap = [(0,start)]
while heap:
    w, node = heapq.heappop(heap)
    if w > dist[node]:
        continue
    for next_edge in edge[node]:
        if dist[next_edge[1]] > w + next_edge[0]:
            dist[next_edge[1]] = w + next_edge[0]
            heapq.heappush(heap, (dist[next_edge[1]],next_edge[1]))

print(dist[end])