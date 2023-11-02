n=int(input())
l1=list(map(int,input().split()))
level="EASY"
for i in l1:
    if(i==1):
        level="HARD"
print(level)