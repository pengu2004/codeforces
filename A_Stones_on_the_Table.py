n=int(input())
stones=list(input())
count=0
for i in range(1,len(stones)):
    if stones[i-1]==stones[i]:
        count+=1
print(count)

