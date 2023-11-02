n=int(input())
def is_power(n):
    if(n>1):
        return is_power(n/2)
    else:
        if(n==1):
            return True
        else:
            return False
for i in range(n):
    n1=int(input())
    if(n1%2!=0):
        print("YES")
    else:
        if(is_power(n1)==False):
            print("YES")
        else:
            print("NO")