s1=input()
s2=input()
s=""
for i in range(len(s1)):
    if(s1[i]!=s2[i]):
        s=s+'1'
    else:
        s=s+'0'
print(s)