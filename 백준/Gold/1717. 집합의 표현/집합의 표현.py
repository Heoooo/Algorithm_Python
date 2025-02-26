import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
parent = [0] * (N+1)

def union(a, b):    #두 집합의 합
    root_a = find(a)
    root_b = find(b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


def find(a): #루트 노드 찾기
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

for i in range(1, N+1): #부모 배열 초기화
    parent[i] = i

for _ in range(M):
    k, a, b = map(int, input().split())
    if k == 0:
        union(a, b)
    elif k == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
