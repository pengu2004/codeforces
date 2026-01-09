
n = int(input())
arr = list(map(int, input().split()))

even = []
odd = []

for i, x in enumerate(arr):
    if x % 2 == 0:
        even.append(i + 1)  
    else:
        odd.append(i + 1)

print(even[0] if len(even) == 1 else odd[0])
