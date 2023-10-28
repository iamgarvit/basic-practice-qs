n=int(input())
for i in range(n):
    x=int(input())
    sum1=0
    sum2=0
    for i in range(3):
        sum1+= x%10
        x=x//10
    for j in range(3):
        sum2+= x%10
        x=x//10
    if(sum1==sum2):
        print("YES")
    else:
        print("NO")