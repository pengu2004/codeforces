test_cases=int(input())
for i in range(test_cases):
    count=int(input())
    values=list(map(int,input().split()))
    freq_map ={}
    for i in values:
        freq_map[i]=freq_map.get(i,0)+1
    if  min(freq_map.values()) >=count//2  and len(freq_map)<=2:
        print("Yes")
    else:
        print("No")
