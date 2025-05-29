from collections import deque
def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    check = [-1] * (n+1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    que = deque()
    que.append(1)
    check[1] = 0
    
    tmp = 0
    while que:
        node = que.popleft()
        for next_node in graph[node]:
            if check[next_node] == -1:
                check[next_node] = check[node] + 1
                tmp = check[next_node]
                que.append(next_node)
    
    rs = 0
    for t in check:
        if tmp == t:
            rs += 1
    return rs