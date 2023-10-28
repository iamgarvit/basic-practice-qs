n=int(input())
for i in range(n):
    check=0
    z=int(input())
    remainder=z%2020
    quotient=z//2020
    if quotient>=remainder:
        check=((quotient-remainder)*2020)+(remainder*2021)
    if check==z:
        print("YES")
    else:
        print("NO")