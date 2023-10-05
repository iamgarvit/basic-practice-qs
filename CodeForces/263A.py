countr=0
countc=0
for i in range(5):
    list1=list(map(int,input().split()))
    for j in range(5):
        if (list1[j]==1):
            countr= i +1
            countc= j+1
a=abs(countr-3)
b=abs(countc-3)
print(a+b)