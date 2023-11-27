def is_prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
n=int(input())
count=0
for i in range(2,n):
    if(is_prime(i)==True):
        count+=1
print(count)