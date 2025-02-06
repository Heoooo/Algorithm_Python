import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))

def one(graph):
    return graph[::-1]

def two(graph):
    tmp_graph = [[0]*M for _ in range(N)]
    for i in range(N):
        tmp_graph[i] = graph[i][::-1]
    return tmp_graph

def three(graph):
    return list(map(list, zip(*graph[::-1])))

def four(graph):
    return list(map(list, (zip(*graph))))[::-1]

def five(graph):
    tmp_graph = [[0]*M for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            tmp_graph[i][j+M//2] = graph[i][j]
            tmp_graph[i][j] = graph[i+N//2][j]
            tmp_graph[i+N//2][j] = graph[i+N//2][j+M//2]
            tmp_graph[i+N//2][j+M//2] = graph[i][j+M//2]
    return tmp_graph

def six(graph):
    tmp_graph = [[0]*M for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            tmp_graph[i][j] = graph[i][j+M//2]
            tmp_graph[i][j+M//2] = graph[i+N//2][j+M//2]
            tmp_graph[i+N//2][j] = graph[i][j]
            tmp_graph[i+N//2][j+M//2] = graph[i+N//2][j]
    return tmp_graph

for cmd in cmds:
    if cmd==1:
        graph = one(graph)
    elif cmd==2:
        graph = two(graph)
    elif cmd==3:
        graph = three(graph)
        N, M = M, N
    elif cmd==4:
        graph = four(graph)
        N, M = M, N
    elif cmd==5:
        graph = five(graph)
    else:
        graph = six(graph)
     
for g in graph:
    print(*g)

