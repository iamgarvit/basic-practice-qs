def computefactorial(n):
    if(n==1):
        return 1
    else: 
        return n*computefactorial(n-1)

def computeCombination(n,r):
    return int(computefactorial(n)/((computefactorial(r))*computefactorial(n-r)))

n=int(input())
r=int(input())
print(computeCombination(n,r))