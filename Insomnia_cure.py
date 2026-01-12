count=0
sheep_freq=[]
for i in range(4):
    sheep_freq.append(int(input()))
total_sheep=int(input())
for i in range(1,total_sheep+1):
    if any(i%v==0 for v in sheep_freq):
        count+=1
print(count)
