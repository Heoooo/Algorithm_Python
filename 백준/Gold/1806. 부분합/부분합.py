import sys
input = sys.stdin.readline
n,s = map(int,input().split())
nums = list(map(int,input().split()))
left = 0
right = 0
min_len = 100000
hap = 0

while True:
    if hap >= s:
        min_len = min(min_len,right-left)
        hap -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        hap += nums[right]
        right += 1
if min_len == 100000:
    print(0)
else:
    print(min_len)