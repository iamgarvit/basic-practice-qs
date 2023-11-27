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
def levy_conjecture(x,l):
    count=0
    for i in range(len(l)):
        for j in range(i,len(l)):
            if(x==(l[i]+2*l[j]) or x==(l[j]+2*l[i])):
                count+=1
    return count
n=int(input())
print(levy_conjecture(n,prime_list(n)))