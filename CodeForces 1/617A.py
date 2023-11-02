n=int(input())
ans=0
if(n%5==0):
    ans=int(n/5)
else:
    ans=int((n/5)+1)
print(ans)