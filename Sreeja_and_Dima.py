cards=int(input())
values=list(map(int,input().split()))
s,d=0,0
start,end=0,cards-1
i=0
while start<=end:
    if i%2==0 and  values[start]>=values[end]:
        s+=values[start]
        start+=1
    elif i%2!=0 and  values[start]>=values[end]:
        d+=values[start]
        start+=1
    elif i%2==0 and  values[start]<=values[end]:
        s+=values[end]
        end-=1
    elif i%2!=0 and  values[start]<=values[end]:
        d+=values[end]
        end-=1
    i+=1
print(s,d)
    

