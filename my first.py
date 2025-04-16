x=int(input())   
for i in range(x):
    y=list(map(int,input().split()))
    print(min(y),max(y))