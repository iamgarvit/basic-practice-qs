n=int(input())
for i in range(n):
    x=int(input())
    l=sorted(list(map(int,input().split())))
    print(abs(l[0]-l[x-1]))