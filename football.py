lines=int(input())
counter={}
for i in range(lines):
    values=input()
    counter[values]=counter.get(values,0)+1
print(max(counter,key=counter.get))
