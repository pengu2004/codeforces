n,x=map(int,input().split())
childs=list(map(int,input().split()))
childs.sort(reverse=True)
start=0
stop=len(childs)-1
count=0
while start<=stop:
    if childs[start]+childs[stop]<=x:
        count+=1
        start+=1
        stop-=1
    else:
        count+=1
        start+=1


print(count)
