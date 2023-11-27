def gp_check(l,r):
    for i in range(len(l)-1):
        if(l[i]*r!=l[i+1]):
            return False
    return True
l1=list(map(float,input().split()))
r1=float(input())
print(gp_check(l1,r1))