num,subs=map(int,input().split())
for _ in range(subs):
    if num>=10:
        if num%10!=0:
            num-=1
        else:
            num//=10
    else:
        num-=1
print(num)