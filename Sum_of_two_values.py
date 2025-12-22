n,target=map(int,input().split())
values=list(map(int,input().split()))
sum_map={}
for i in range(len(values)):
    if target-values[i] in sum_map:
        print(str(sum_map[target-values[i]]+1)+" "+str(i+1))
        exit()
    else:
        sum_map[values[i]]=i
print("IMPOSSIBLE")
