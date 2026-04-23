import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0

    heap = []
    for i in range(len(works)):
        heapq.heappush(heap, -works[i])
    
    for i in range(n):
        tmp = heapq.heappop(heap)
        tmp += 1
        heapq.heappush(heap, tmp)
    rs= 0
    for i in range(len(works)):
        rs += heap[i]**2
    print(heap)
    return rs