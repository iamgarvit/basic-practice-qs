n,m=map(int,input().split())
tv_list=sorted(list(map(int,input().split())))
earning=0
for i in range(m):
    if(tv_list[i]<0):
        earning+=abs(tv_list[i])
print(earning)