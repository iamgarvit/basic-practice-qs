l=list(map(int,input().split()))
for i in range(len(l)):
    if(l[i]==1):
        l.append(l.pop(i))         
print(l)