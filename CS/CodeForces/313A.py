n=int(input())
if(n>=0):
    print(n)
else:
    s1=str(n)
    s=''
    if(s1[len(s1)-1]>s1[len(s1)-2]):
        for i in range(len(s1)-1):
            s=s+s1[i]
    else:
        for i in range(len(s1)-2):
            s=s+s1[i]
        s=s+s1[len(s1)-1]
    x=int(s)
    print(x)