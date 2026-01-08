count,time=map(int,input().split())
queue=list(input())
for j in range(time):
    for i in range(len(queue)):
        if queue[i]=="B" and i<count-1:
            print(queue[i],i)
            queue[i],queue[i+1]=queue[i+1],queue[i]
print("".join(queue))



