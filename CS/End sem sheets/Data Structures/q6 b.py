def is_prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
def prime_list(x):
    l=[]
    for i in range(2,x):
        if(is_prime(i)==True):
            l.append(i)
    return l
def semi_prime(l,x):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]*l[j]==x):
                return True
    return False
n=int(input())
print(semi_prime(prime_list(n),n))