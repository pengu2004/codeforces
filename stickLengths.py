n=int(input())
length=list(map(int,input().split()))
length.sort()
ans=0
median=(length[len(length)//2])
for i in length:
    ans+=abs(i-median)
print(ans)

