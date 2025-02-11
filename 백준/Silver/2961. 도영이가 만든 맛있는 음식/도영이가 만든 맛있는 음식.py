import sys
input = sys.stdin.readline

N = int(input())
food = []
for i in range(N):
    a, b = map(int, input().split())
    food.append((a,b))

rs = sys.maxsize

check = [False] * N

def back(idx):
    global rs
    if idx == N:
        cnt = 0
        s, b = 1, 0
        for i in range(len(check)):
            if check[i] == True:
                s *= food[i][0]
                b += food[i][1]
                cnt += 1
        if cnt == 0:
            return
        rs = min(rs, abs(s-b))
        return rs

    check[idx] = True
    back(idx+1)
    check[idx] = False
    back(idx+1)
back(0)
print(rs)