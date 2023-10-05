n,h=map(int,input().split())
l1=list(map(int,input().split()))
w=0
for i in l1:
    if(i>h):
        w+=2
    else:
        w+=1
print(w)