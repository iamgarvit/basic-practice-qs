def prime_check(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
def next_prime(y):
    while True:
        if(prime_check(y+1)==True):
            return y+1
        else:
            return next_prime(y+1)
n,m=map(int,input().split())
if(next_prime(n)==m):
    print("YES")
else:
    print("NO")