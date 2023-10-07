n=int(input())
s=input()
s=s.lower()
l=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
for i in s:
    if(i in l):
        l.remove(i)
if(len(l)==0):
    print('YES')
else:
    print('NO')