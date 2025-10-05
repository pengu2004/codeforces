n=int(input())
dp=[]
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1,n+1):
    dp[i] = 0
    for j in range(1, 7):
        if i - j >= 0:
            dp[i] += dp[i - j]
            print(dp,i,j)

print(dp[n] % 1000000007)