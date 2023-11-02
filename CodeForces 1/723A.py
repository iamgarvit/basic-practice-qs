l=sorted(list(map(int,input().split())))
sum=0
for i in range(3):
    sum+=abs(l[1]-l[i])
print(sum)