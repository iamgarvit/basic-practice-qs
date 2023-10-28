n=int(input())
for i in range(n):
    time=0
    h,m=map(int,input().split())
    time= (23-h)*60 + 60-m
    print(time)