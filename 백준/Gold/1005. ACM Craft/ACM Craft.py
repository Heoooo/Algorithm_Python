import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    check = [0] * (N+1)

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    W = int(input())

    rs = 0
    que = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            que.append(i)
            check[i] = D[i-1]

    while que:
        node = que.popleft()
        for next_node in graph[node]:
            indegree[next_node] -= 1
            check[next_node] = max(check[next_node], check[node]+D[next_node-1])
            if indegree[next_node] == 0:
                que.append(next_node)
                
    print(check[W])
        
    
             
