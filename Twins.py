coins = int(input())
coin_list = list(map(int, input().split()))

coin_list.sort(reverse=True)

total = sum(coin_list)
my_sum = 0
count = 0

for c in coin_list:
    my_sum += c
    count += 1
    if my_sum > total - my_sum:
        break

print(count)
