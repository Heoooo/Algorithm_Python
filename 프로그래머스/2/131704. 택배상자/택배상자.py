def solution(order):
    stack = [] #보조 벨트
    rs = 0
    N = len(order)
    for i in range(1, N+1):
        stack.append(i)
        
        while stack and stack[-1] == order[rs]:
            stack.pop()
            rs += 1
    return rs