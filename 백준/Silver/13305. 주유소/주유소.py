import sys
input = sys.stdin.readline

N = int(input())
load = list(map(int, input().split()))
price = list(map(int, input().split()))

rs = 0
min_price = price[0]
for i in range(N-1):
    if min_price > price[i]:
        min_price = price[i]
    rs += (min_price * load[i])
print(rs)