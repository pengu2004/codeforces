l=["h","e","l","l","o"]
s=input()
found_count=0
for i in s.lower():
    if  found_count<5 and i == l[found_count]:
        found_count+=1
if found_count>=5:
    print("YES")
else:
    print("NO")
        

