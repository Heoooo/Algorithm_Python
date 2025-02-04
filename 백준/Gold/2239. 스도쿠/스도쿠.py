import sys
input = sys.stdin.readline
graph = [list(map(int, input().strip())) for _ in range(9)]

def check1(i, j, num): #가로, 세로 검사
    for k in range(9):
        if graph[i][k] == num or graph[k][j] == num:
            return False
    return True

def check2(y, x, num): #칸 검사
    si = (y//3)*3
    sj = (x//3)*3
    for i in range(3):
        for j in range(3):
            if graph[si+i][sj+j] == num:
                return False
    return True

def back():
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                for k in range(1, 10):
                    if check1(i, j, k) and check2(i, j, k):
                        graph[i][j] = k
                        if back():
                            return True
                        graph[i][j] = 0
                return False
    return True
back()
for i in range(9):
    print(*graph[i],sep='')
