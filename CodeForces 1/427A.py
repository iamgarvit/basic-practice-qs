n=int(input())
crime_police=list(map(int,input().split()))
crime_untreated=0
current_police=0
for i in crime_police:
    if(i==-1):
        if(current_police>0):
            current_police-=1
        else:
            crime_untreated+=1
    else:
        current_police+=i
print(crime_untreated)