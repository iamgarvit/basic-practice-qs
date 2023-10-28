n=int(input())
perf=list(map(int,input().split()))
current_max=perf[0]
current_min=perf[0]
amazing_count=0
for i in range(1,len(perf)):
    if(perf[i]>current_max):
        current_max=perf[i]
        amazing_count+=1
    if(perf[i]<current_min):
        current_min=perf[i]
        amazing_count+=1
print(amazing_count)