value,sub_count=map(int,input().split())
for i in range(1,sub_count+1):
    if value%10==0:
        value=value//10
    else:
        value-=1
print(value)
