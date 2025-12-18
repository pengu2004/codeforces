n=int(input())
nums=list(map(int,input().split()))

sum_val=nums[0]
val=0
for i in range(n):
    val+=nums[i]
    sum_val=max(val,sum_val)
    if val<=0:
        val=0
print(sum_val)


