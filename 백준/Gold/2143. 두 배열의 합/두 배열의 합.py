from itertools import combinations
import sys
input = sys.stdin.readline
T = int(input())
N = int(input())
nums1 = list(map(int, input().split()))
M = int(input())
nums2 = list(map(int, input().split()))
rs = 0
num = {}
for i in range(N):
    tmp = 0
    for j in range(i, N):
        tmp = sum(nums1[i:j+1])
        if tmp not in num:
            num[tmp] = 1
        else:
            num[tmp] += 1

for i in range(M):
    tmp = 0
    for j in range(i, M):
        tmp = sum(nums2[i:j+1])
        if T - tmp in num:
            rs += num[T-tmp]
print(rs)
