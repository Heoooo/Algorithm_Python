def solution(n, tops):
    a = [0] * (n+1)
    b = [0] * (n+1)
    
    if tops[0] == 1:
        a[1] = 1
        b[1] = 3
    else:
        a[1] = 1
        b[1] = 2
        
    for i in range(2, n+1):
        if tops[i-1] == 1:
            a[i] = (a[i-1] + b[i-1]) % 10007
            b[i] = (2*a[i-1] + 3*b[i-1]) % 10007
        else:
            a[i] = (a[i-1] + b[i-1]) % 10007
            b[i] = (a[i-1] + 2*b[i-1]) % 10007
    
    rs = (a[n] + b[n]) % 10007
    return rs