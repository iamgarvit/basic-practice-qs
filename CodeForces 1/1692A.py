n=int(input())
for i in range(n):
    count=0
    l=list(map(int,input().split()))
    for i in l:
        if(i>l[0]):
            count+=1
    print(count)
    