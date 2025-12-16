n=int(input())
times=[]
for i in range(n):
    s,e=map(int,input().split())
    times.append((s,1))
    times.append((e,-1))
times.sort()
count=0
max_count=0
for _,v in times:
    count+=v
    max_count=max(count,max_count)
print(max_count)


