l1=list(map(int,input().split()))
d1=int(input())
def ap_check(l,d):
    for i in range(len(l)-1):
        if(l[i]+d!=l[i+1]):
            return False
    return True
print(ap_check(l1,d1))