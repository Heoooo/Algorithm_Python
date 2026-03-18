import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
dist = [0] * 200001

que = deque()
que.append((N, 1))
while que:
    cur, cnt = que.popleft()
    if cur == K:
        break
    n_cur1 = cur + 1
    n_cur2 = cur - 1
    n_cur3 = cur * 2
    
    if 0 <= n_cur1 <= 200000 and dist[n_cur1] == 0:
        dist[n_cur1] = cnt
        que.append((n_cur1, cnt+1))
        
    if 0 <= n_cur2 <= 200000 and dist[n_cur2] == 0:
        dist[n_cur2] = cnt
        que.append((n_cur2, cnt+1))
        
    if 0 <= n_cur3 <= 200000 and dist[n_cur3] == 0:
        dist[n_cur3] = cnt
        que.append((n_cur3, cnt+1))
print(dist[K])
