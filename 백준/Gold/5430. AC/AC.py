import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    AC = input().strip()
    N = int(input())
    arr = deque(input().strip()[1:-1].split(','))

    if N == 0:
        arr = deque()

    flag = True
    r = 0
    for i in AC:
        if i == 'R':
            r += 1
        elif i == 'D':
            if len(arr) == 0:
                print('error')
                flag = False
                break
            else:
                if r % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if flag == True:
        if r%2 == 0:
            print('['+','.join(arr)+']')
        else:
            arr.reverse()
            print('['+','.join(arr)+']')
                