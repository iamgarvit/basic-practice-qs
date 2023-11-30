def selection_sort(l):
    low=0
    while (low<len(l)):
        for i in range(low+1,len(l)):
            if(l[i]<l[low]):
                l[i],l[low]=l[low],l[i]
        low+=1
    return l
        
print(selection_sort(list(map(int,input().split()))))