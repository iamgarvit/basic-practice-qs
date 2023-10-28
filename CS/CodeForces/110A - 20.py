def count(x):
    count=0
    for i in str(x):
        if(i=='4' or i=='7'):
            count+=1
    if(count==0):
        return 1
    else:
        return count
def lucky(n):
    if(n==4 or n==7):
        return True
    if(n<1 and n!=0):
        return True
    else:
        if((n%10)==4 or (n%10)==7):
            return (True and lucky(n//10))
        else: 
            return False
n1=int(input())
if (lucky(count(n1))==True):
    print("YES")
else:
    print("NO")