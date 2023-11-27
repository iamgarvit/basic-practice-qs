l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
p=int(input())
def l_norm(l1,l2,p):
    sum=0
    for i in range(len(l1)):
        sum+=abs((l1[i]-l2[i])**p)
    return sum**(1/p)
print(l_norm(l1,l2,p))