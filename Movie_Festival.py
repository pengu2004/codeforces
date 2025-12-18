n = int(input())
movies = []

for _ in range(n):
    s, e = map(int, input().split())
    movies.append((e, s))

movies.sort()  # sort by end time

count = 0
last_end = 0

for e, s in movies:
    if s >= last_end:
        count += 1

print(count)
