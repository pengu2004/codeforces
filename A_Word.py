word=str(input())
count,upper=0,0
for char in word:
    if char.islower():
        count+=1
    else:
        upper+=1
if upper<=count:
    print(word.lower())
else:
    print(word.upper())