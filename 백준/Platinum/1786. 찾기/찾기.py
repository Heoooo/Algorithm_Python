import sys
input = sys.stdin.readline
T = input().rstrip()
P = input().rstrip()
rs = [0] * len(P)
idx = 0
for i in range(1, len(P)):
    while idx > 0 and P[i] != P[idx]:
        idx = rs[idx-1]
       
    if P[i] == P[idx]:
        idx += 1
        rs[i] = idx

k = 0
find = []
for i in range(len(T)):
    while k > 0 and T[i] != P[k]:
        k = rs[k-1]
        
    if T[i] == P[k]:
        if k == len(P)-1:
            find.append(i-len(P)+2)
            k = rs[k]
        else:
            k += 1
            
print(len(find))
print(' '.join(map(str, find)))
