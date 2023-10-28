def func(a,b,c,n):
    d=max(a,b,c)
    A=d-a
    B=d-b
    C=d-c
    if(n<(A+B+C)):
        return 'NO'
    else:
        n=n-(A+B+C)
        if n%3==0:
            return 'YES'
        else:
            return 'NO'
t=int(input())
for i in range(t):
    a1,b1,c1,n1=map(int,input().split())
    print(func(a1,b1,c1,n1))