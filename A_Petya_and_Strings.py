str1=input()
str2=input()
flag=0
for i in range(len(str1)):
    sum1=ord(str1[i].lower())
    sum2=ord(str2[i].lower())
    if sum1==sum2:
        continue

    else:
        if sum1<sum2:
            print(-1)
            flag=1
            break
        else:
            print(1)
            flag=1
            break

if flag==0:
    print(0)