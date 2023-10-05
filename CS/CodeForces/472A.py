def prime(n):
    ans=True
    for i in range(2,n):
        if(n%i==0):
            ans=False
    return(ans)
n=int(input())
for i in range(4,n-4):
    if(prime(i)==False and prime(n-i)==False):
        print(i,n-i)
        break