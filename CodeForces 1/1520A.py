n=int(input())
for i in range(n):
    x=int(input())
    s=input()
    if(x==1 or x==2):
        print("YES")
    else:
        countcon=0
        countdis=0
        y=x
        for i in range(x):
            for j in range(i+1,x):
                if(s[i]==s[j]):
                    countcon+=1
                else:
                    y=j+1
                    break
            while y<len(s):
                if(s[y]==s[i]):
                    countdis+=1
                    break
                else:
                    y+=1
        if(countdis>0):
            print("NO")
        else:
            print("YES")