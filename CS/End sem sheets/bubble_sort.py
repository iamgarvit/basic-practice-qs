def bubble_sort(l):
    for i in range(1,len(l)):
        bubbleup(i,len(l),l)
    return l
        
def bubbleup(lo,hi,l):
    for j in range(lo,hi):
        if(l[j-1]>l[j]):
            l[j-1],l[j]=l[j],l[j-1]
            
l1=list(map(int,input().split()))
print(bubble_sort(l1))