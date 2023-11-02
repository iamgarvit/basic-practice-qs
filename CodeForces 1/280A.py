def calc(x):
    return ((x*(x+1))//2)
def steps(y):
    count=0
    while(y>0 and y>=calc(count+1)):
        count+=1
        y=y-calc(count)
    return count
n=int(input())
print(steps(n))