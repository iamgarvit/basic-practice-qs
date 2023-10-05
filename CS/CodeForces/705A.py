n=int(input())
if(n!=1):
    for i in range(1,n):
        if(i%2!=0):
            print("I hate that", end= " ")
        else:
            print("I love that",end= " ")
    if(n%2!=0):
        print("I hate it")
    else:
        print("I love it")
else:
    print("I hate it")