import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
N, M = len(str1), len(str2)

DP = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if str2[i - 1] == str1[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
print(DP[M][N])

lcs = []
i, j = M, N
while i > 0 and j > 0:
    if str2[i - 1] == str1[j - 1]:
        lcs.append(str2[i - 1])
        i -= 1
        j -= 1
    elif DP[i - 1][j] > DP[i][j - 1]:
        i -= 1
    else:
        j -= 1

print("".join(reversed(lcs)))
