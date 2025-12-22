test_cases=int(input())
for _ in range(test_cases):
    n,k=map(int,input().split())
    nums=list(map(int,input().split()))
    if sorted(nums)==nums:
        print("YES")
    else:
        if k>1:
            print("Yes")
        else:
            print("NO")

