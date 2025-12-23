t=int(input()) #number of test cases
for i in range(t):

    n,p=map(int,input().split())
    travel=[0,]
    max_distance=0
    travel.extend(list(map(int,input().split()))) 
    travel.append(p)
    for stop in range(1,len(travel)):
        if stop<len(travel)-1:
            max_distance=max(max_distance,travel[stop]-travel[stop-1])
        else:
            max_distance=max(max_distance,(travel[stop]-travel[stop-1])*2)

    print(max_distance)
    travel=[]

