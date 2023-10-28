def sqst(s1):
    if(len(s1)%2==1):
        return 'NO'
    else:
        if(s1[0:len(s1)//2]==s1[len(s1)//2:]):
            return 'YES'
        else:
            return 'NO'
n=int(input())
for i in range(n):
    s=input()
    print(sqst(s))