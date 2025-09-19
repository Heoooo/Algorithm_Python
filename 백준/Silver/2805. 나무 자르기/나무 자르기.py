import sys
input = sys.stdin.readline
n,m = map(int,input().split())
trees = list(map(int,input().split()))
rs = 0
start = 0
end = max(trees)

while (start<=end):
    tmp = 0
    mid = (start+end) // 2
    for tree in trees:
        if tree > mid:
            tmp += tree - mid

    if tmp < m:
        end = mid - 1
    else:
        rs = mid
        start = mid + 1
print(rs)   