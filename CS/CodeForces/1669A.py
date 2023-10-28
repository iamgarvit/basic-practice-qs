n=int(input())
for i in range(n):
    x=int(input())
    if(x<=1399):
        print("Division 4")
    if(x>1399 and x<=1599):
        print("Division 3")
    if(x>1599 and x<=1899):
        print("Division 2")
    if(x>=1900):
        print("Division 1")