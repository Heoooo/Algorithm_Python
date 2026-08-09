import heapq

def solution(n, k, enemy):
    heap = []
    cnt = 0
    for e in enemy:
        n -= e
        heapq.heappush(heap, -e)
        
        if n < 0:
            if k > 0:
                n += -heapq.heappop(heap)
                k -= 1
            else:
                return cnt
        cnt += 1
                
    return len(enemy)