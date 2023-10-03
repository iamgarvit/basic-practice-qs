def hailstone(n):
    if(n==1):
        return None
    else:
        if(n%2==0):
            n=int(n/2)
            print(n, end=' ')
            return hailstone(n)
        else:
            n=3*n+1
            print(n, end=' ')
            return hailstone(n)

x=int(input())
hailstone(x)