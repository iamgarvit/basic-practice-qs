def distinct(s):
    l=[]
    while s>=1:
        l.append(s%10)
        s=s//10
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]==l[j]):
                return False
    return True
n=int(input())
for i in range(n+1,10**10):
    if(distinct(i)==True):
        print(i)
        break