import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
T = int(input())

def union(a, b):    #두 집합의 합
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return root_a
    else:   #b집합을 a에 집어넣음
        parent[root_b] = root_a
        friend[root_a] += friend[root_b]
        return root_a

def find(a): #루트 노드 찾기
    if parent[a] == a:  #내 자신이 루트 노드
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]  #재귀를 통해서 최종 루트 노드 찾기

for _ in range(T):
    N = int(input())
    parent = dict() #parent[a] = b : a의 루트노드는 b
    friend = dict() #firend[a] = b : a의 집합 b명 속해있다
    
    for _ in range(N):
        a, b = map(str, input().split())
    
        if a not in parent:
            parent[a] = a
            friend[a] = 1
        if b not in parent:
            parent[b] = b
            friend[b] = 1
        root = union(a, b)
        print(friend[root])
    
