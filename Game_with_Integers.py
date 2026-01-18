test_cases=int(input())
for i in range(test_cases):
    val=int(input())
    if val%3==1 or val%3==2:
        print("First")
    else:
        print("Second")
