from collections import Counter
def solution(points, routes):
    point = [(0,0)] + points
    pos = []         
    

    for route in routes:
        time = 0
        for j in range(len(route)-1):
            starty, startx = point[route[j]]
            endy, endx = point[route[j+1]]
        
            while starty != endy:
                pos.append((time, starty, startx))
                if starty < endy:
                    starty += 1
                else:
                    starty -= 1
                time += 1
            
            while startx != endx:
                pos.append((time, endy, startx))
                if startx < endx:
                    startx += 1
                else:
                    startx -= 1
                time += 1     
        pos.append((time, starty, startx))
    
    rs = 0
    count = Counter(pos)

    for k in count.values():
        if k >= 2:
            rs += 1
    return rs
                    
    