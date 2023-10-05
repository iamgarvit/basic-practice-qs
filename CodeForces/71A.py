def longword(word1):
    if(len(word1)>10):
        a=word1[0]
        b=str(len(word1)-2)
        c=word1[len(word1)-1]
        print(a+b+c)
    else:
        print(word1)
    
    

n=int(input())
for i in range(n):
    x=input()
    longword(x)