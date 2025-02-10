import sys
input = sys.stdin.readline
str1 = input().strip()
str2 = input().strip()
DP = [[""]*(len(str1)+1) for _ in range(len(str2)+1)]
for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            DP[i+1][j+1] = DP[i][j]+str2[i]
        else:
            if len(DP[i][j+1]) > len(DP[i+1][j]):
                DP[i+1][j+1] = DP[i][j+1]
            else:
                DP[i+1][j+1] = DP[i+1][j]
print(len(DP[-1][-1]))
print(DP[-1][-1])
