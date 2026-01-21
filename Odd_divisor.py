import math
test_cases=int(input())
for v in range(test_cases):
    i=int(input())
    if i==2:
        print("no")
    elif math.floor(math.log(i,2))==math.log(i,2) :
        print("no")
    else:
        print("yes")
