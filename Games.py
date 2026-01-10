games=int(input())
homes=[]
aways={}
c=0
for i in range(games):
    home,away=input().split()
    aways[away]=aways.get(away,0)+1
    homes.append(home)
for h in homes:
    if h in aways:
        c+=aways[h]
print(c)
