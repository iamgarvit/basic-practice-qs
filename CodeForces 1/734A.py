n=int(input())
str1=input()
counta=0
countd=0
for i in str1:
    if(i=='A'):
        counta+=1
    elif(i=='D'):
        countd+=1
    else:
        continue
if(counta>countd):
    print("Anton")
elif(countd>counta):
    print("Danik")
else:
    print("Friendship")