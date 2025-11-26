Counter={}
games=int(input())
results=input()
for i in results:
    Counter[i]=Counter.get(i,0)+1
    if Counter["A"]>Counter["D"]:
        print("Anton")
    elif Counter["D"]>Counter["A"]:
        print("Danik")
    else:
        print("Friendship")
