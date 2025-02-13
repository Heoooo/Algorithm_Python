import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
t=int(input())
dy=[0,1,0,-1]
dx=[1,0,-1,0]
def dfs(y,x):
    global cnt
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<m:
            if graph[ny][nx]==1 and chk[ny][nx]==False:
                chk[ny][nx]=True
                dfs(ny,nx)

for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    chk=[[False]*m for _ in range(n)]
    
    for _ in range(k):
        a,b=map(int,input().split())
        graph[b][a]=1

    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and chk[i][j]==False:
                chk[i][j]=True
                dfs(i,j)
                cnt+=1
    print(cnt)