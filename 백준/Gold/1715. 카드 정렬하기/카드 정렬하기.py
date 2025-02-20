import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    a = int(input())
    heap.append(a)
heapq.heapify(heap)

rs = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    rs += a+b
    heapq.heappush(heap, a+b)
print(rs)
    
    
