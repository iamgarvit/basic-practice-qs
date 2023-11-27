#ambigous
l=list(map(int,input().split()))
n=int(input())
def rotate_clockwise(l,n):
    for i in range(len(l)-1):
        if(i!=n-1 or i!=n-2):
            l[i],l[i+1]=l[i+1],l[i]
        if(n!=0 or n!=len(l)-1):
            l[0],l[len(l)-1]=l[len(l)-1],l[0]
    return l
print(rotate_clockwise(l,n))