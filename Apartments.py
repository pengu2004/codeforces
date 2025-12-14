n, m, k = map(int, input().split())
applicants=sorted(list(map(int,input().split())))
appartments=sorted(list(map(int,input().split())))
print(applicants,appartments)
count=0
i,j=0,0
while i<n and j<m:
    if applicants[i]-appartments[j]>k:
        j+=1
    elif appartments[j]-applicants[i]>k:
        i+=1
    else:
        count+=1
        i+=1
        j+=1
print(count)


