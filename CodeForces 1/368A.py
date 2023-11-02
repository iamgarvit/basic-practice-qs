def color_check(x,y,c):
    for i in x:
        for j in range(y):
            if(i[j] in c):
                return '#Color'
    return '#Black&White'
color=['Y','M','C']
n,m=map(int,input().split())
l1=[]
for i in range(n):
    l=input().split()
    l1.append(l)
print(color_check(l1,m,color))