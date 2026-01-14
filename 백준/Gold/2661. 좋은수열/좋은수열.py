N = int(input())

def check(arr):
    for i in range(1, len(arr)//2 + 1):
        if arr[-i:] == arr[-2*i:-i]:
            return False
    return True

def back(cnt):
    if cnt == N:
        print(''.join(map(str, rs)))
        exit()
    for i in range(1, 4):
        rs.append(i)
        if check(rs):
            back(cnt+1)
        rs.pop()
rs = []
back(0)
            
