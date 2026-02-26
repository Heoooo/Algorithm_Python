from collections import deque
n,m=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
S=[[-1]*m for _ in range(n)]
q=deque()
q.append((x1-1,y1-1))
S[x1-1][y1-1]=0
dx,dy=[0,0,1,-1],[1,-1,0,0]
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and S[nx][ny]==-1:
            if D[nx][ny]=='0':
                q.appendleft((nx,ny))
                S[nx][ny]=S[x][y]
            else:
                q.append((nx,ny))
                S[nx][ny]=S[x][y]+1
print(S[x2-1][y2-1])