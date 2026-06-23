def solution(numbers):
    rs = []
    N = len(numbers)
    stack = []
    for i in range(N-1, -1,-1):
        while stack and numbers[i] >= stack[-1]:
            stack.pop()
        
        if stack:
            rs.append(stack[-1])
        else:
            rs.append(-1)
        
        stack.append(numbers[i])
    rs = rs[::-1]
    return rs