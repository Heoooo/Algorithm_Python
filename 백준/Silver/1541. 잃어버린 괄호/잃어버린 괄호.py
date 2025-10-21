import sys
input = sys.stdin.readline
s = input().split('-')
rs = []
for i in s:
    hap = 0
    tmp = i.split('+')
    for j in tmp:
        hap += int(j)
    rs.append(hap)
n = rs[0]
for i in range(1,len(rs)):
    n -= rs[i]
print(n)