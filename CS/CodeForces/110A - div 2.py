def func(players):
    players_sorted=sorted(players)
    max1=players_sorted[3]
    max2=players_sorted[2]
    p1=0
    p2=0
    if(players[0]>players[1]):
        p1=players[0]
    else:
        p1=players[1]
    if(players[2]>players[3]):
        p2=players[2]
    else:
        p2=players[3]
    if((p1==max1 and p2==max2) or (p1==max2 and p2==max1)):
        print("YES")
    else:
        print("NO")
n=int(input())
for i in range(n):
    p=list(map(int,input().split()))
    func(p)