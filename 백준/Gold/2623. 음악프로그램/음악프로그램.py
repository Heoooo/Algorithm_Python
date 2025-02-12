import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    nums = list(map(int, input().split()))
    for i in range(1, len(nums)-1):
        graph[nums[i]].append(nums[i+1])
        indegree[nums[i+1]] += 1

rs = []
que = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        que.append(i)

while que:
    node = que.popleft()
    rs.append(node)
    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            que.append(next_node)

if len(rs) == N:
    for i in rs:
        print(i)
else:
    print(0)
