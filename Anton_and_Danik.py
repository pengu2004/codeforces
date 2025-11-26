games=input()
results=input()
map={"Anton":0,"Danik":0}
for i in results:
    if i=="A":
        map["Anton"]+=1
    else: 
        map["Danik"]+=1
if map["Anton"]>map["Danik"]:
    print("Anton")
elif map["Danik"]>map["Anton"]:
    print("Danik")
else:
    print("Friendship")

    
