import sys
input = sys.stdin.readline

N = int(input())
plus = []
minus = []
rs = 0
for _ in range(N):
    a = int(input())
    if a > 1:
        plus.append(a)
    elif a <= 0:
        minus.append(a)
    else:
        rs += a

plus.sort(reverse = True)
minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        rs += plus[i]
    else:
        rs += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        rs += minus[i]
    else:
        rs += (minus[i] * minus[i+1])
print(rs)