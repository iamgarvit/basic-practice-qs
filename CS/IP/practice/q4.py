def countdigit(x):
    if(x<1):
        return 0
    else:
        return 1 + countdigit(x//10)
    
n1=int(input())
print(countdigit(n1))