'''
def dfs(a, b, idx, info, n, m):
    global rs
    if idx == len(info):
        if a < n and b < m:
            rs = min(rs, a)
        return
    if a >= n or b >= m or a >= rs:
        return
    
    dfs(a+info[idx][0], b, idx+1, info, n, m)
    dfs(a, b+info[idx][1], idx+1, info, n, m)
    
    
def solution(info, n, m):
    global rs
    rs = float('inf')
    
    dfs(0, 0, 0, info, n, m)
    
    if rs == float('inf'):
        return -1
    else:
        return rs
'''
def dfs(a, b, idx, info, n, m, dp):
    global rs
    if idx == len(info):
        if a < n and b < m:
            rs = min(rs, a)
        return
    
    if (a, b, idx) not in dp:
        dp.add((a, b, idx))
    else:
        return
    
    if a >= n or b >= m or a >= rs:
        return
    
    dfs(a+info[idx][0], b, idx+1, info, n, m, dp)
    dfs(a, b+info[idx][1], idx+1, info, n, m, dp)
    
    
def solution(info, n, m):
    global rs
    rs = float('inf')
    
    dp = set()
    dfs(0, 0, 0, info, n, m, dp)
    
    if rs == float('inf'):
        return -1
    else:
        return rs