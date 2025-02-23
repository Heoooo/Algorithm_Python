import sys
input = sys.stdin.readline
string = input().strip()
stack = []
tmp = 1
rs = 0
for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
        tmp *= 2

    elif string[i] == '[':
        stack.append('[')
        tmp *= 3

    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            rs = 0
            break
        if string[i-1] == '(':
            rs += tmp
        stack.pop()
        tmp = tmp//2
    else:
        if not stack or stack[-1] == '(':
            rs = 0
            break
        if string[i-1] == '[':
            rs += tmp
        stack.pop()
        tmp = tmp//3
if stack:
    print(0)
else:
    print(rs)
            
