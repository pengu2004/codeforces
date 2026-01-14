book_pages=int(input())
page_rate=list(map(int,input().split()))
start=0
while book_pages>0:
    book_pages-=page_rate[start%7]
    start+=1
if start%7==0:
    print(7)
else:
    print((start)%7)

