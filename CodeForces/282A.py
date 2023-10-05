n=int(input())
x=0
for i in range(n):
    str1=input()
    if('+' in str1):
        x+=1
    else:
        x-=1
print(x)