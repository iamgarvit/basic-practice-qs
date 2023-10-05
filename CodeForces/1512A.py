testcases=int(input())
for i in range(testcases):
    d=0
    lenarray=int(input())
    l=list(map(int,input().split()))
    z=l[0]
    for j in range(lenarray-1):
        a=l[j-1]
        b=l[j]
        c=l[j+1]
        if a!=b or b!=c:
            if a!=b: 
                if a==c:
                    d=b
                elif b==c:
                    d=a
            if b!=c: 
                if b==a:
                    d=c
                elif c==a:
                    d=b
    print((l.index(d))+1)