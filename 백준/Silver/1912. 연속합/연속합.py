import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
dp[n-1] = nums[n-1]

for i in range(n-2,-1,-1):
    dp[i] = max(dp[i+1] + nums[i], nums[i])
print(max(dp))