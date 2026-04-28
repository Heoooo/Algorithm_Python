from collections import deque
def solution(n, infection, edges, k):
    edge = [[] for _ in range(n+1)]
    check = [False] * (n+1)
    check[infection] = True
    
    for x, y, t in edges:
        edge[x].append((y, t))
        edge[y].append((x, t))
        
    def spread(current_check, pipe):
        next_check = list(current_check)
        que = deque()
        
        for i in range(1, n+1):
            if next_check[i]:
                que.append(i)
        
        while que:
            node = que.popleft()
            for next_node, ptype in edge[node]:
                if ptype == pipe and next_check[next_node] == False:
                    next_check[next_node] = True
                    que.append((next_node))
        return next_check
    
    def dfs(current_check, cnt):
        if cnt == k:
            tmp = 0
            for i in range(1,n+1):
                if current_check[i]:
                    tmp += 1
            return tmp
        
        rs = 0
        for i in range(1, 4):
            nvirus = spread(current_check, i)
            rs = max(rs, dfs(nvirus, cnt+1))
        return rs
    return dfs(check, 0)
            
        
