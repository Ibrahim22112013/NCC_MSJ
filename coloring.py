x=int(input())
for i in range(x):
    b=int(input())
    k=list(map(int,input().split()))
    h=0
    for j in range(int(len(k)/2)):
        M=max(k)
        m=min(k)
        h+=(M-m)
        k.remove(M)
        k.remove(m)
    print(h)    