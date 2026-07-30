def solution(x, y, n):
    check = [99999] * (y+1)
    check[x] = 0
    for i in range(x, y+1):
        if i % 2 == 0:
            check[i] = min(check[i//2]+1, check[i])
        if i % 3 == 0:
            check[i] = min(check[i//3]+1, check[i])
        if i - n >= x:
            check[i] = min(check[i-n]+1, check[i])
    if check[y] == 99999:
        return -1
    else:
        return check[y]