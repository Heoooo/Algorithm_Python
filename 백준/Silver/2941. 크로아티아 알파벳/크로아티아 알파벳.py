import sys
c=['c=','c-','dz=','d-','lj','nj','s=','z=']
n=sys.stdin.readline().strip()
for i in c:
        n=n.replace(i,' ')
print(len(n))