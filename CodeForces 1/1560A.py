n=int(input())
for i in range(n):
    x=int(input())
    l=[]
    i=1
    while(len(l)<x):
        if(i%3==0 or i%10==3):
            i+=1
        else:
            l.append(i)
            i+=1
    print(l[len(l)-1])