def solution(m, n, startX, startY, balls):
    rs = []
    def cal(y, x):
        tmp = (startY - y)**2 + (startX - x)**2
        return tmp
    for ballx, bally in balls:
        tmp = float('inf')
        if not(startY == bally and startX > ballx):
            y1 = bally
            x1 = -ballx
            tmp = min(tmp, cal(y1, x1))
        if not(startX == ballx and startY > bally):
            y2 = -bally
            x2 = ballx
            tmp = min(tmp, cal(y2, x2))
        if not(startY == bally and startX < ballx):
            y3 = bally
            x3 = (m-ballx) * 2 + ballx
            tmp = min(tmp, cal(y3, x3))
        if not(startX == ballx and startY < bally):
            y4 = (n-bally) * 2 + bally
            x4 = ballx
            tmp = min(tmp, cal(y4, x4))
        rs.append(tmp)
    return rs
        
    
        