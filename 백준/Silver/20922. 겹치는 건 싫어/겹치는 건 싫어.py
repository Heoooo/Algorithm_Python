import sys
input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(map(int, input().split()))
cnt = [0] * (max(nums)+1)

start = 0
end = 0
rs = 0

while True:
    if end == N:
        break

    if cnt[nums[end]] < K:
        cnt[nums[end]] += 1
        end += 1

    else:
        cnt[nums[start]] -= 1
        start += 1
    rs = max(end-start, rs)
print(rs)
