n=int(input())
fx=0
fy=0
fz=0
for i in range(n):
    x1,y1,z1=map(int,input().split())
    fx+=x1
    fy+=y1
    fz+=z1
if(fx==0 and fy==0 and fz==0):
    print('YES')
else:
    print("NO")