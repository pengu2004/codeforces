total_soldiers=int(input())
soldiers_list=list(map(int,input().split()))
old_min=float("inf")
for l in range(1,total_soldiers+1):
    new_min=abs(soldiers_list[(l-1%total_soldiers)]-soldiers_list[(l%total_soldiers)])
    if new_min<old_min:
        old_min=new_min
        a,b=(l-1%total_soldiers),(l%total_soldiers)
print(a+1,b+1)
