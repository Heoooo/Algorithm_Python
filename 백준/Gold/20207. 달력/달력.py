import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 1001

min_value = float('inf')
max_value = 0
for _ in range(N):
    s, e = map(int, input().split())
    min_value = min(min_value, s)
    max_value = max(max_value, e)
    for i in range(s, e+1):
        cnt[i] += 1

w, h = 0, 0
rs = 0
for k in range(min_value, max_value+2):
    if cnt[k] != 0:
        w += 1
        h = max(h, cnt[k])
    else:
        rs += w*h
        w, h = 0, 0

print(rs)
