n=int(input())
for i in range(n):
    l=sorted(list(map(int,input().split())))
    if(l[2]==l[0]+l[1]):
        print('YES')
    else:
        print('NO')