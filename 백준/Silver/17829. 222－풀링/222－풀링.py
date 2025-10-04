N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
tmp_graph = graph

while N != 1:
    new_graph = [[0]*(N//2) for _ in range(N//2)]
    for i in range(0,N,2):
        for j in range(0,N,2):
            tmp = []
            tmp.append(tmp_graph[i][j])
            tmp.append(tmp_graph[i+1][j])
            tmp.append(tmp_graph[i][j+1])
            tmp.append(tmp_graph[i+1][j+1])

            tmp.sort()
            new_graph[i//2][j//2] = tmp[-2]
    tmp_graph = new_graph
    N = N//2
print(tmp_graph[0][0])
