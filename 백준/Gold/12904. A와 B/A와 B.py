import sys
input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())

while len(A) < len(B):
    if B[-1] == 'A':
        B.pop()
    else:
        B.pop()
        B.reverse()
if A != B:
    print(0)
else:
    print(1)
        