def func(a,b,c):
    if(a>b):
        count=0
        while(a>b):
            if(a-c>=b):
                a=a-c
                b=b+c
                count+=1
            else:
                for i in range(c,0,-1):
                    if(a-i>=b):
                        a=a-i
                        b=b+i
                        count+=1
        return(count)
    else:
        count=0
        while(b>a):
            if(b-c>=a):
                b=b-c
                a=a+c
                count+=1
            else:
                for i in range(c,0,-1):
                    if(b-i>=a):
                        b=b-i
                        a=a+i
                        count+=1
        return(count)
n=int(input())
for i in range(n):
    n1,n2,n3=map(int,input().split())
    print(func(n1,n2,n3))