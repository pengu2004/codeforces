nums=str(input())
count=0
for num in nums:
    if '4' in num  or '7' in num:
        count+=1
if count%4==0 or count%7==0:
    print('YES')
else:
    print("NO")