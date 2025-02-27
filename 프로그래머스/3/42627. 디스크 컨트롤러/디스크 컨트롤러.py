import heapq
def solution(jobs): 
    rt = 0   #총 반환 시간
    heap = []   #대기 큐
    jobs.sort() #작업 시작 순으로 정렬
    time = 0
    cnt = 0
    check = [False] * (len(jobs))
    
    while cnt < len(jobs):
            
        for i in range(len(jobs)):
            if jobs[i][0] <= time and not check[i]:
                heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
                check[i] = True    
                
        if heap:
            w, req = heapq.heappop(heap)  #w:소요 시간, req:작업 요청 시간, time: 현재 시간
            rt += time + w - req
            time += w
            cnt += 1
        else:
            time += 1
    
    return rt//len(jobs)
                
        
    