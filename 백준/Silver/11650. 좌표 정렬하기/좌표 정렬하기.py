import sys
input = sys.stdin.readline
N = int(input())
rs = []
for _ in range(N):
    x, y = map(int, input().split())
    rs.append((x,y))
rs.sort(key = lambda x:(x[0], x[1]))
for x, y in rs:
    print(x, y)
