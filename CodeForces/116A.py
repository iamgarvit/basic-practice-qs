n=int(input())
maxcount=0
currentcount=0
for i in range(n):
    out,inc=map(int,input().split())
    currentcount= currentcount - out + inc
    if(maxcount<=currentcount):
        maxcount=currentcount
print(maxcount)