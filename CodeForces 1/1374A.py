n=int(input())
for i in range(n):
    x,y,n=map(int,input().split())
    r=n%x
    if(y==0):
        print(n-r)
    else:
        if(r<y):
            print(n-(x-y)-r)
        if(r>y):
            print(n-(r-y))
        if(r==y):
            print(n)