n=int(input())
count=0
for i in range(n):
    a,b,c=map(int,input().split())
    d=a+b+c
    if(d>=2):
        count+=1
print(count)