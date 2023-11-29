def second_maximum(l):
    a=l[0]
    b=l[0]
    for i in range(len(l)):
        if(l[i]>b):
            if(l[i]>a):
                a,b=l[i],a
            else:
                b=l[i]
    return b
def second_minimum(l):
    a=l[0]
    b=l[0]
    for i in range(len(l)):
        if(l[i]<b):
            if(l[i]<a):
                a,b=l[i],a
            else:
                b=l[i]
    return b
l1=list(map(int,input().split()))
print("second maximum:",second_maximum(l1))
print("second minimum", second_minimum(l1))