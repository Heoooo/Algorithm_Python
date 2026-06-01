import heapq
def solution(n, costs):
    rs = 0
    graph = [[] for _ in range(n)]
    check = [False] * n
    for cost in costs:
        graph[cost[0]].append((cost[2], cost[1]))
        graph[cost[1]].append((cost[2], cost[0]))
    
    heap = [(0,0)]

    while heap:
        w, node = heapq.heappop(heap)
        if not check[node]:
            check[node] = True
            rs += w
            for nw, next_node in graph[node]:
                if not check[next_node]:
                    heapq.heappush(heap, (nw, next_node))
    return rs