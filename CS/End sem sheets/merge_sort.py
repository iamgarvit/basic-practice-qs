def merge_sort(l):
    if(len(l)<=1):
        return l
    m=len(l)//2
    Sorted_left=merge_sort(l[0:m])
    Sorted_right=merge_sort(l[m:])
    return (merge(Sorted_left,Sorted_right))

def merge(l1,l2):
    l3=[]
    i,j=0,0
    while i<len(l1) and j<len(l2):
        if(l1[i]<=l2[j]):
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    l3.extend(l1[i:])
    l3.extend(l2[j:])
    return l3

print(merge_sort(list(map(int,input().split()))))