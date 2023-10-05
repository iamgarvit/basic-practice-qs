x=input("")
str1=""
count=0
for i in x:
    if(i in str1):
        continue
    else:
        count=count+1
        str1=str1+i
if(count%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")