from collections import deque
def solution(n, results):
    graph = [[] for _ in range(n+1)]
    prev = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    outdegree = [0] * (n+1)
    
    for a, b in results:
        graph[a].append(b)
        prev[b].append(a)
        
    
    for i in range(1, n+1):
        check = [False] * (n+1)
        que = deque()
        que.append(i)
        check[i] = True
        cnt = 0
        while que:
            node = que.popleft()
            for next_node in graph[node]:
                if not check[next_node]:
                    cnt += 1
                    check[next_node] = True
                    que.append(next_node)
        outdegree[i] = cnt
    
    for i in range(1, n+1):
        que = deque()
        check = [False] * (n+1)
        check[i] = True
        cnt2 = 0
        que.append(i)
        while que:
            node = que.popleft()
            for pre_node in prev[node]:
                if not check[pre_node]:
                    cnt2 += 1
                    check[pre_node] = True
                    que.append(pre_node)
        indegree[i] = cnt2
    
    rs = 0
    for i in range(1, n+1):
        if indegree[i] + outdegree[i] == n-1:
            rs += 1
        
    return rs
    
    