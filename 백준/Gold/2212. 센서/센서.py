import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
s = list(map(int, input().split()))

if K >= N:
    print(0)
    sys.exit()

s.sort()
dist = []
for i in range(N-1):
    dist.append(s[i+1]-s[i])
dist.sort(reverse=True)

for _ in range(K-1):
    dist.pop(0)
print(sum(dist))