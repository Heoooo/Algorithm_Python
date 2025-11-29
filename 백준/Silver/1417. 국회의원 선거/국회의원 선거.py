N = int(input())
arr = []
ds = int(input())
for _ in range(N-1):
    a = int(input())
    arr.append(a)
arr.sort()
cnt = 0
if N == 1:
    print(0)
    exit()
while ds <= arr[-1]:
    ds += 1
    arr[-1] -= 1
    cnt += 1
    arr.sort()
print(cnt)
