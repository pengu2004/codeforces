for row in range(5):
    values=list(map(int,input().split()))
    for column in range(5):
        if values[column]==1:
            print(abs(3-(column+1))+abs(3-(1+row)))
