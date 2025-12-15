n,m=map(int,input().split())
customers=sorted(list(map(int,input().split())))  
tickets=sorted(list(map(int,input().split())))
i,j=0,0
while  j<m:
    if customers[i]>=tickets[j]:
        print(customers[i])
        i+=1
        j+=1
    else:
        print(-1)
        j+=1

