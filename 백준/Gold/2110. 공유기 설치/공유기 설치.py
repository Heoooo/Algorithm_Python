import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    h = int(input())
    house.append(h)

house.sort()
start = 1
end = house[N-1] - house[0]

rs = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    last_inst = house[0]
    for i in range(N):
        if house[i] - last_inst >= mid:
            cnt += 1
            last_inst = house[i]
    if C <= cnt:
        rs = mid
        start = mid + 1
    elif cnt < C:
        end = mid - 1
print(rs)