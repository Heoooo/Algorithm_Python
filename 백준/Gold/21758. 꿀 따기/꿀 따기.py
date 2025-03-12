import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
hap=[0] * N
hap[0] = nums[0]
rs = 0

for i in range(1, N):
    hap[i] += hap[i-1]+nums[i]

#최대로 꿀을 먹으려면 벌통이 양 끝에 있거나 가운데 있어야 함

#벌통이 맨 오른쪽에 있는 경우 (벌 한마리는 맨 왼쪽 고정, 한마리만 i값으로 위치 변경하면서)
for i in range(1, N-1):
    rs = max(rs, (hap[N-1]-nums[0]-nums[i]) + (hap[N-1]-hap[i]))

#벌통이 맨 왼쪽에 있는 경우 (벌 한마리는 오른쪽 고정, 한마리만 i값으로 위치 변경하면서)
for i in range(1, N-1):
    rs = max(rs, (hap[N-1]-nums[N-1]-nums[i]) + hap[i-1])

#벌통이 가운데 있는 경우(벌 두마리는 양쪽 끝 고정, 벌통 위치만 i로 변경)
for i in range(1, N-1):
    rs = max(rs, (hap[i]-nums[0]) + (hap[N-2]-hap[i-1]))
print(rs)

