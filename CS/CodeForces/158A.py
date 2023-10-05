x,y=map(int,input().split())
list1=list(map(int,input().split()))
count=0
for i in list1:
    a=list1[y-1]
    if(i>0):
        if(i>=a):
            count+=1
print(count)