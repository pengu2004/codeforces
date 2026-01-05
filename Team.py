questions=int(input())
correct_ans=0
for q in range(questions):
    a,b,c=(map(int,input().split()))
    if a+b+c>=2:
        correct_ans+=1
print(correct_ans)

