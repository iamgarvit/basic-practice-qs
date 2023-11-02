n=int(input())
def calc(x):
    l=[]
    i=0
    while x>=1:
        if(x%10!=0):
            l.append((x%10)*(10**i))
        i+=1
        x=x//10
    print(len(l))
    for i in l:
        print(i,end=" ")
    print()
for i in range(n):
    n1=int(input())
    calc(n1)