s=input().lower()
l=['a','e','i','o','u','y']
s1=''
for i in s:
    if(i in l):
        continue
    else:
        s1=s1+'.'+i
print(s1)