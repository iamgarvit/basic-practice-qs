n=int(input())
for i in range(n):
    s1=input()
    x=int(s1)
    y=len(s1)
    if(x<10):
        print((10*(x-1))+1)
    else:
        count=10*(x%10-1)
        for i in range(y+1):
            count+=i
        print(count)