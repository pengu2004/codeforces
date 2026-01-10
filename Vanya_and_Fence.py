friends,fence=map(int,input().split())
heights=list(map(int,input().split()))
c=0
for height in (heights):
    if height>fence:
        c+=2
    else:
        c+=1
print(c)

