import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    check = [False] * (N + 1)
    rs = 0

    for i in range(1, N + 1):
        if not check[i]: 
            path = []
            cur = i

            while not check[cur]:
                check[cur] = True
                path.append(cur)
                cur = nums[cur - 1] 
            
            if cur in path:
                cycle_start = path.index(cur)
                rs += len(path[cycle_start:])

    print(N - rs)
