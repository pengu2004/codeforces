s=input()
count=1
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        count+=1
        if count==6:
            print("YES")
            exit()
    else:
        count=0
print("NO")
