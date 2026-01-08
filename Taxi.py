groups=int(input())
children=list(map(int,input().split()))
ones=children.count(1)
twos=children.count(2)
threes=children.count(3)
fours=children.count(4)

taxis=fours


pairs=min(threes,ones)

taxis+=pairs

threes-=pairs
ones-=pairs

taxis+=threes

pairs=twos//2

taxis+=pairs
twos%=2

if twos:
    taxis+=1
    ones-=min(ones,2)


if ones>0:
    taxis+=(ones+3)//4
print(taxis)

