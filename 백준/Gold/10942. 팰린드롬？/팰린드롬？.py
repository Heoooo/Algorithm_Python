import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
DP = [[0] * N for _ in range(N)] #DP[i][j] = i번째 수 부터 j번재 수까지 팰린드롬인지
for i in range(N):  #숫자 하나는 무조건 팰린드롬
    DP[i][i] = 1
for i in range(N-1):    #숫자 두개 확인
    if nums[i] == nums[i+1]:
        DP[i][i+1] = 1

for k in range(3, N+1): #숫자 3개부터 최대 N개 팰린드롬 확인
    for i in range(N-k+1):  
        j = i+k-1
        if nums[i] == nums[j]:
            if DP[i+1][j-1] == 1:
                DP[i][j] = 1

for _ in range(M):
    s, e = map(int, input().split())
    print(DP[s-1][e-1])

