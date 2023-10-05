maxlevel=int(input())
check=0
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.pop(0)
l2.pop(0)
listf=list(set(sorted(l1+l2)))
for i in range(1,maxlevel+1):
    if i in listf:
        check+=1
    else:
        print("Oh, my keyboard!")
        break
if check==maxlevel:
    print("I become the guy.")