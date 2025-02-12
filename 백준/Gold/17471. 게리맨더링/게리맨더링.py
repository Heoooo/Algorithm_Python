from collections import deque
N = int(input())
person = [0] + list(map(int, input().split()))
edge = [[] for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    tmp.pop(0)
    edge[i].extend(tmp)

def bfs(arr):
    que = deque()
    que.append(arr[0])
    check = [False] * (N+1)
    check[arr[0]] = True
    cnt = 1
    tmp = person[arr[0]]
    while que:
        node = que.popleft()
        for next_node in edge[node]:
            if next_node in arr and check[next_node] == False:
                check[next_node] = True
                tmp += person[next_node]
                cnt += 1
                que.append(next_node)
    if cnt == len(arr):
        return tmp


def choice(cnt, tmp):
    global rs
    if cnt == tmp:
        arr1 = []
        arr2 = []
        for i in range(1, N+1):
            if check[i] == False:
                arr1.append(i)
            else:
                arr2.append(i)
        rs1 = bfs(arr1)
        rs2 = bfs(arr2)
        if rs1 and rs2:
            rs = min(rs, abs(rs1 - rs2))
        return

    for i in range(1, N+1):
        if check[i] == False:
            check[i] = True
            choice(cnt, tmp+1)
            check[i] = False
            
rs = float('inf')      
for i in range(1, N//2+1):
    check = [False] * (N+1)
    choice(i, 0)
if rs == float('inf'):
    print(-1)
else:
    print(rs)
