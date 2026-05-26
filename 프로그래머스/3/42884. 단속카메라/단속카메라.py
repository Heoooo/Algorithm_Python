def solution(routes):
    routes.sort(key=lambda x:x[1])
    print(routes)
    
    end = routes[0][1]
    rs = 1
    for i in range(1, len(routes)):
        if end >= routes[i][0]:
            continue
        else:
            end = routes[i][1]
            rs += 1
    return rs