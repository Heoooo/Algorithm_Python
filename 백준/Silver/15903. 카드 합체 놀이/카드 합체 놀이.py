import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

heap = []
for num in nums:
    heapq.heappush(heap, num)

for _ in range(K):
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)

    heapq.heappush(heap, n1+n2)
    heapq.heappush(heap, n1+n2)

print(sum(heap))