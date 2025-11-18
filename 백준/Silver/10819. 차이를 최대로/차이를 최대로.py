import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
check = [False] * N

mx = 0
def back(arr):
    global mx
    if len(arr) == N:
        tmp = 0
        for i in range(N-1):
            tmp += abs(arr[i] - arr[i+1])
        mx = max(tmp, mx)
        return

    for i in range(N):
        if check[i] == False:
            check[i] = True
            back(arr+[num[i]])
            check[i] = False

back([])
print(mx)