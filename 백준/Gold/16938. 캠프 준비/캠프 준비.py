import sys
input = sys.stdin.readline
max_size = sys.maxsize

N, L, R, X = map(int, input().split())
nums = list(map(int, input().split()))

rs = 0
def choice(idx, count, tmp, min_k, max_k):
    global rs
    if idx == N:
        if count >= 2 and L <= tmp and tmp <= R and max_k - min_k >= X:
            rs += 1
        return

    choice(idx+1, count+1, tmp+nums[idx], min(min_k, nums[idx]), max(max_k, nums[idx]))
    choice(idx+1, count, tmp, min_k, max_k)

choice(0, 0, 0, max_size, 0)
print(rs)
    
