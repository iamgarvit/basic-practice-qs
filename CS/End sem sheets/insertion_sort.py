def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while (j>=0 and key<l[j]):
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
    return l

print(insertion_sort(list(map(int,input().split()))))