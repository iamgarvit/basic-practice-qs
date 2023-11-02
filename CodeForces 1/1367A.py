n=int(input())
for i in range(n):
    x=input()
    z=""
    z+=(x[0:2])
    for j in range(2,(len(x)+1)):
        if (j%2)!=0:
            z+=(x[j])
    print(z)