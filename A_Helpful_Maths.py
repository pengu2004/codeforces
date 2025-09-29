ans=list(map(int,input().split("+")))
#bubble sort
n=len(ans)
for i in range(n):
    for j in range(n-i-1):
        if ans[j]>ans[j+1]:
            ans[j],ans[j+1]=ans[j+1],ans[j]
    ans[n - i - 1] = str(ans[n - i - 1])
print("+".join(ans))

