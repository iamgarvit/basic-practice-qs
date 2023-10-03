def exponent(a,b):
    if(a==0):
        return 0
    elif(a==1):
        return 1
    else:
        if(b>0):
            if(b==1):
                return a
            else:
                return a*exponent(a,b-1)
        else:
            if(b==-1):
                return 1/a
            else:
                return (1/a)*exponent(a,b+1)
            
def sum_digit_power(n,x):
    if(n<0):
        c=abs(n)
        if(c<1):
            return 0
        else:
            return (-1)*(exponent(c%10,x)+sum_digit_power(c//10,x))
    else:
        if(n<1):
            return 0
        else:
            return exponent(n%10,x)+sum_digit_power(n//10,x)
n1=int(input())
x1=int(input())
print(round((float(sum_digit_power(n1,x1))),3))