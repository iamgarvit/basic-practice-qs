n1,n2=map(int,input().split())
for i in range(n2):
    if(n1%10==0):
        n1=n1/10
    else:
        n1=n1-1
print(int(n1))