test_cases=int(input())
for i in range(test_cases):
    nums=int(input())
    values=list(map(int,input().split()))
    if [values[0]]+sorted(values[1:])==sorted(values):
        print("Yes")
    else:
        print("NO")
