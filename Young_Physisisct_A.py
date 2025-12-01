n=int(input())
vectors=[]
a,b,c=0,0,0
for i in range(n):
    vectors.append(list(map(int,input().split())))
for k in vectors:
    a+=k[0]
    b+=k[1]
    c+=k[2]
if a==b==c==0:
    print("YES")
else:
    print("NO")
