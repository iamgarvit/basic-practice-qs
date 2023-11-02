n=int(input())
count_mishka=0
count_chris=0
for i in range(n):
    m,c=map(int,input().split())
    if(m>c):
        count_mishka+=1
    if(m<c):
        count_chris+=1
if(count_mishka>count_chris):
    print('Mishka')
elif(count_mishka<count_chris):
    print('Chris')
else:
    print("Friendship is magic!^^")