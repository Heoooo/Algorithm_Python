import heapq

def mentoring(n, arr):
    heap = []
    delay = 0
    for s, e in arr:
        if n == 0:
            k = heapq.heappop(heap)
            tmp = max(k-s, 0)
            delay += tmp
            heapq.heappush(heap, e+tmp)
        else:
            n -= 1
            heapq.heappush(heap, e)
    return delay
            

def solution(k, n, reqs):
    cs = [[] for _ in range(k)]
    for s, e, t in reqs:
        cs[t-1].append([s, (s+e)])
    
    
    rs = 0
    cnt = [1] * k
    for _ in range(n-k):
        tmp = []
        max_value = -1
        idx = -1
        for i in range(k):
            diff = mentoring(cnt[i], cs[i]) - mentoring(cnt[i]+1, cs[i])
            if max_value < diff:
                max_value = diff
                idx = i
        
        cnt[idx] += 1
    
    for i in range(k):
        rs += mentoring(cnt[i], cs[i])
    return rs
    