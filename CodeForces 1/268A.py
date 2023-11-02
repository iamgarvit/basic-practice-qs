n=int(input())
collection=[]
for i in range(n):
    l1=list(map(int,input().split()))
    collection.append(l1)
count=0
for k in range(n):
    for j in range(n):
        if(k==j):
            continue
        else:
            if(collection[k][0]==collection[j][1]):
                count+=1
print(count)