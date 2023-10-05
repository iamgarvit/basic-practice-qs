l1=list(map(int,input().split('+')))
l2=sorted(l1)
if(len(l2)>1):
    for i in range(len(l2)-1):
        print(l2[i],end='+')
    print(l2[len(l2)-1])
else:
    print(l2[0])