n=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
for i in range(len(l1)):
    print(l1[i],end=' ')