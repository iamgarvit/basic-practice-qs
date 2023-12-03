def gcd(a,b):
    if(b>a):
        return gcd(b,a)
    if(a%b==0):
        return b
    return gcd(b,a%b)
n1,n2=map(int,input().split())
print(gcd(n1,n2))