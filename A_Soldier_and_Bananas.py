first_banana,money,want=map(int,input().split())
ans=first_banana
for i in range(2,want+1):
    ans+=(i*first_banana)
if ans-money<=0:
    print(0)
else:
    print(ans-money)