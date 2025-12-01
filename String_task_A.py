s=input()
start=0
end=len(s)
vowels={"a","e","i","o","u","y"}
result=[]
while start<end:
    if s[start].lower() in vowels:
        start+=1
    else:
        result.append(".")
        result.append(s[start].lower())
        start+=1
print("".join(result))
