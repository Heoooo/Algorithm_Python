import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

rs1, rs2 = 0, 0

def count(y, x, k):
    global rs1,  rs2
    zero, one = 0, 0
    for i in range(y, y+k):
        for j in range(x, x+k):
            if graph[i][j] == 0:
                zero += 1
            else:
                one += 1
    if zero == k*k:
        rs1 += 1
        return
    elif one == k*k:
        rs2 += 1
        return
    else:
        count(y+k//2, x, k//2)
        count(y, x+k//2, k//2)
        count(y, x, k//2)
        count(y+k//2, x+k//2, k//2)
count(0, 0, N)
print(rs1)
print(rs2)