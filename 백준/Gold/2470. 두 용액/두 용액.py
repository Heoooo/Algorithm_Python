import sys
import math
input = sys.stdin.readline
n = int(input())
liq = list(map(int, input().split()))
start = 0
end = n - 1
liq.sort()

hap = abs(liq[start] + liq[end])
rs = [liq[start], liq[end]]

while start < end:
    diff = liq[end] + liq[start]

    if abs(diff) < hap:
        hap = abs(diff)
        rs = [liq[start], liq[end]]
        if hap == 0:
            break
    if diff < 0:
        start += 1
    else:
        end -= 1
    
print(rs[0], rs[1])