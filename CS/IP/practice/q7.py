def square_of_num(x):
    if(x==1):
        return 1
    else:
        return square_of_num(x-1)+ 2*x-1
    
n=int(input())
print(square_of_num(n))