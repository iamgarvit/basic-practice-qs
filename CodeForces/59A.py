str1=input()
countu=0
countl=0
for i in str1:
    if(i.isupper()==True):
        countu+=1
    elif(i.islower()==True):
        countl+=1
if(countu>countl):
    print(str1.upper())
else:
    print(str1.lower())