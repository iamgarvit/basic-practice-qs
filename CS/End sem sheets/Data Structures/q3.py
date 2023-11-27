l=list(map(int,input().split(",")))
r=int(input())
c=[]
for i in l:
    c.append(l)
for i in range(len(l)):
    z=i+r
    z=z%(len(l))
    c[z]=l[i]
print(c)