l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    if(l[i] in l[i+1:]):
        count+=1
print(count)
