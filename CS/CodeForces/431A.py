a1,a2,a3,a4=map(str,input().split())
s1=input()
cal=0
for i in s1:
    if(i=='1'):
        cal+=int(a1)
    elif(i=='2'):
        cal+=int(a2)
    elif(i=='3'):
        cal+=int(a3)
    else:
        cal+=int(a4)
print(cal)