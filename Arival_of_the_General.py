soldiers=int(input())
heights=list(map(int,input().split()))
tallest=0
shortest=0
heights_map={}
for h in range(len(heights)):
        heights_map.setdefault(heights[h],[]).append(h)
ans=(abs((len(heights)-1)-max(heights_map[min(heights_map)]))+abs(0-min(heights_map[max(heights_map)])))
if max(heights_map[min(heights_map)])<min(heights_map[max(heights_map)]):
    print(ans-1)
else:
    print(ans)
