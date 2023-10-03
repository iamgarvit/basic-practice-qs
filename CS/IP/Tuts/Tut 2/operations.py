while True:
    print('''Choose your preffered operation:
          
      1.Addition
      2.Subtraction
      3.Multipilcation
      4.Division
      5.Modulus
      6.Exit''')
    n=int(input())
    if(n==1):
        n1=int(input("Enter First number: "))
        n2=int(input("Enter second number: "))
        print(n1+n2)
    elif(n==2):
        n1=int(input("Enter First number: "))
        n2=int(input("Enter second number: "))
        print(n1-n2)
    elif(n==3):
        n1=int(input("Enter First number: "))
        n2=int(input("Enter second number: "))
        print(n1*n2)
    elif(n==4):
        n1=int(input("Enter First number: "))
        n2=int(input("Enter second number: "))
        print(n1/n2)
    elif(n==5):
        n1=int(input("Enter First number: "))
        n2=int(input("Enter second number: "))
        print(n1%n2)
    elif(n==6):
        break 