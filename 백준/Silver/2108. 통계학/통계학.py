import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
num = []
rs1 = 0
for _ in range(N):
    a = int(input())
    num.append(a)
    rs1 += a
print(round(rs1/N))

num.sort()
print(num[N//2])

cnt = Counter(num).most_common()
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(abs(max(num) - min(num)))