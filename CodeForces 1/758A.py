n=int(input())
l=list(map(int,input().split()))
sum=0
x=max(l)
for i in l:
    sum= sum + x-i
print(sum)