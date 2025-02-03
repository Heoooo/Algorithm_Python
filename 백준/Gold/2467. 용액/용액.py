import sys
input = sys.stdin.readline
N = int(input())
liquid = list(map(int, input().split()))
rs = float('inf')
'''
brute force = n^2
두  값을 찾는 경우, 배열 정렬 상태 -> 투포인터
left + right
rs와 abs(total)음수인 경우 : left +1
양수인 경우: right - 1
while (left < right)
'''
left = 0
right = N-1
total = 0
rs1, rs2 = 0, N-1
while (left < right):
    total = liquid[left] + liquid[right]
    if abs(total) < rs:
        rs = abs(total)
        rs1, rs2 = left, right
        if total == 0:
            break
    if total < 0:
        left += 1
    else:
        right -= 1
print(liquid[rs1], liquid[rs2])
