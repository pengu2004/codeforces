import math
test_cases=int(input())
for i in range(test_cases):
    total=int(input())
    if  math.floor(total/3)*1 + math.ceil(total/3)*2 ==total:
        print(math.floor(total/3),math.ceil(total/3))
    else:
        print(math.ceil(total/3),math.floor(total/3))
