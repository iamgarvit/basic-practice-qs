def func(a,b):
    if(a==1 or a==2):
        return 1
    else:
        if((a-2)%b==0):
            return (a-2)//b+1
        else:
            return (a-2)//b+2
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print(func(n,x))