n=int(input())
l1=list(map(int,input().split()))
s=0
for i in l1:
    s+=i
print(s/(len(l1)))